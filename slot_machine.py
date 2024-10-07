#importing random to generate random numbers for slot machine 
import random
# maximum number of slot lines in our slot machine
MAX_LINES = 3
#maximum number of bet 
MAX_BET = 10000
#minimum number of bet
MIN_BET = 100
#minimum deposit amount
MIN_DEPOSIT = 1000
#maximum deposit amount
MAX_DEPOSIT = 10000
#number of rows and columns on slot machine

ROWS = 3
COLS = 3

#how many symbols in the slot machine
symbol_count = {
    
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#Function to actually enable slot machine to spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    #in each column we generate the values inside teh column       
    columns = [] #columns list
    #make a copy of the list of symbols
    current_symbols = all_symbols[:]
    for col in range(cols):
        column =[]
        for row in range (rows):
            value = random.choice(current_symbols) #choose from current symbols
            current_symbols.remove(value) # remove value from the list
            column.append(value) #add the value to our column
            
        columns.append(column) #Add column to columns list
        
    return columns

#Print columns
def print_slot_machine(columns):
    #change print format(transpose column list)
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="")
                
        print()
    
#Function responsible for collecting user input for cashg deposit from user
def deposit ():
    while True :
        amount = input ("What amount of cash would you like to deposit? ($1000 - 10000) $")
        if amount.isdigit():
            #check if input is actually a number
            amount = int(amount)
            # check if the amount is greater than zero
            if amount >= MIN_DEPOSIT and amount <= MAX_DEPOSIT:
                # if all conditions are met, break the loop
                break
            else:
                print (f"Amount must be between ${MIN_DEPOSIT} and ${MAX_DEPOSIT}.")
                # if all conditions are met, break the loop
        else:
            print ("Please enter a cash number.")
    return amount

#Function responsible for collecting the number of lines the user would like to bet on
def get_number_of_lines():
    while True :
        lines = input ("Enter the number of lines you would like to bet on (1 - " +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            #check if input is actually a number
            lines = int(lines)
            # check if the amount is greater than zero
            if 1<= lines <= MAX_LINES:
                # if all conditions are met, break the loop
                break
            else:
                print ("Choice must be within the limit")
        else:
            print ("Please enter a number.")
    return lines

#Function to get the bet on each line \
def get_bet():
    while True :
        amount = input ("What amount of cash would you like to bet? $")
        if amount.isdigit():
            #check if input is actually a number
            amount = int(amount)
            # check if the amount is with thw minimum and maximum bet
            if MIN_BET <= amount <= MAX_BET:
                # if all conditions are met, break the loop
                break
            else:
                print (f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print ("Please enter a cash number.")
    return amount
    
#function to rerun the game
def main():
    balance = deposit()
    lines = get_number_of_lines()
    #To make sure the bet is within the range of deposited amount
    while True :
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance :
            print(f"You do not have enough cash to bet, your current balance is ${balance}")
        else:
            break
    print (f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)

main()