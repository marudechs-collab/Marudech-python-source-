password = input("Enter you pass word; ")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("You password is storong!")
else:
    print("You password is not strong")