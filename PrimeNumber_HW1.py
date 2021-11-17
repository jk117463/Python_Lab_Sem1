print("Enter the Limit untill which Prime numbers needs to be listed  : ")
limit = int(input())

print(" List of prime numbers till %s are " % limit)

for i in range(2, limit):
    ind = 0 # Indicator variable set value as 0
    j = 2
    while j <= int(i/2): # To continuosly divide by consecutive number from 2 till half of its value
        if i % j == 0: # If remainder is 0, that means it is not prime number, so setting indicator to 1, ignoring rest of possible divisions  and breaking onto upper loop
            ind = 1
            break
        j = j + 1
    if ind == 0: #If indicator is still 0, that means it is a prime number
        print(i)