while True:    #This simulates a Do Loop
    found = False
    index = 0
    print("Enter a charge account number: ")
    account = input()
    while len(account) < 7 or len(account) > 7:
        print("Charge account number must be 7 digits! Enter a charge account number: ")
        account = input()
    num = int(account)
    accountNumbers = [0] * (18)
    
    accountNumbers[0] = 5658845
    accountNumbers[1] = 4520125
    accountNumbers[2] = 7895122
    accountNumbers[3] = 8777541
    accountNumbers[4] = 8451277
    accountNumbers[5] = 1302850
    accountNumbers[6] = 8080152
    accountNumbers[7] = 4562555
    accountNumbers[8] = 5552012
    accountNumbers[9] = 5050552
    accountNumbers[10] = 7825877
    accountNumbers[11] = 1250255
    accountNumbers[12] = 1005231
    accountNumbers[13] = 6545231
    accountNumbers[14] = 3852085
    accountNumbers[15] = 7576651
    accountNumbers[16] = 7881200
    accountNumbers[17] = 4581002
    while found == False and index <= 18 - 1:
        if accountNumbers[index] == num:
            found = True
            print("The account number is valid")
        else:
            index = index + 1
    if found != True:
        print("The account number entered is not valid")
    print("Would you like to run the program again? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
