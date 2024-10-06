#maximum number of slot lines in our slot machine
MAX_LINES = 3

#Function responsible for collecting user input for cashg deposit from user
def deposit ():
    while True :
        amount = input ("What amount of cash would you like to deposit? $")
        if amount.isdigit():
            #check if input is actually a number
            amount = int(amount)
            # check if the amount is greater than zero
            if amount > 0:
                # if all conditions are met, break the loop
                break
            else:
                print ("Amount must be greater than 0")
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
    
#function to rerun the game
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print (balance, lines)

main()