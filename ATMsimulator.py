correct_pin = "1234"
balance = 10000
attempts = 3
deposit = 20000
pin = input("Enter the pin: ")

while attempts > 0 and pin != correct_pin:

    attempts -= 1

    if attempts > 0:
        print("Incorrect Pin. Try Again.", "Attempts Left:", attempts)
        pin = input("Enter the pin: ")

    else:
        print("Card Blocked")

if pin == correct_pin:
    print("Balance:", balance)
    print("Deposit:", deposit)
    balance = balance + deposit
    print("New Balance:", balance)

    withdraw = 50000
    print("Withdraw:", withdraw)

    if withdraw > balance:
        print("Insufficient Balance")
    else:
        balance = balance - withdraw
        print("New Balance:", balance)




