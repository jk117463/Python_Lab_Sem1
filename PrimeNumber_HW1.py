
def check_user_input(input): #Function to validate input
    try:
        # Convert it into integer
        val = int(input)
        if val >= 0:
            print("Input is an integer number. Number = ", val)
            return True
        else:
            print("Input is negative number. Number = ", val)
            return False
    except ValueError:
        print("Input is not an integer number. Pls reenter")
        return False

validinput = False
while validinput == False:
    print("Enter the Limit until which Prime numbers needs to be listed  : ")
    limit = input()
    validinput = check_user_input(limit)

if validinput == True:
    print("List of prime numbers till %s are " % limit)

    for i in range(2, int(limit)):
        ind = 0 # Indicator variable set value as 0
        j = 2
        while j <= int(i/2): # To continuosly divide by consecutive number from 2 till half of its value
            if i % j == 0: # If remainder is 0, that means it is not prime number, so setting indicator to 1, ignoring rest of possible divisions  and breaking onto upper loop
                ind = 1
                break
            j = j + 1
        if ind == 0: #If indicator is still 0, that means it is a prime number
            print(i)