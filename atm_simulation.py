#---ATM Simulation---

import csv
from datetime import datetime

#variables
balance = 1000
PIN = "1234"
attempt = 0
max_attempt = 3
file_name = 'Transaction.csv'

#functions
def check_balance():
    global balance
    print('Your available balance is', balance)
    transaction_log('Check Balance', 0, balance)

def deposit():
    global balance
    amount = float(input('Enter the amount to deposit here: '))
    balance += amount
    print('Deposit sucessful, your new balance is', balance)
    transaction_log('Deposit', amount, balance)

def withdraw():
    global balance
    amount = float(input('Enter the amount to withdraw here: '))
    if amount <= balance:
        balance -= amount
        print('Withdrawal successful, your new balance is', balance)
        transaction_log('Withdraw', amount, balance)
    else:
        print('Sorry, insufficient fund!!')
        transaction_log('Failed Withdrawal', amount, balance)

def change_pin():
    global PIN
    print('You are about to change your transaction PIN')
    old_pin = input('Enter your old PIN: ')
    if old_pin == PIN:
        new_pin = input('Enter your new PIN: ')
        confirm = input('Re-enter your new PIN: ')
        if confirm == new_pin:
            PIN = new_pin
            print('Your PIN has been changed sucessfully, new PIN is', PIN)
        else:
            print('Sorry, your new input PIN do not match')
    else:
        print('Incorrect PIN')

def transaction_log(action, amount, balance):
    with open(file_name, 'a', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), name, action, amount, balance])

def exit_transaction():
    print('Thank you for banking with us!')


#main function script
def main():
    global name, attempt, max_attempt, PIN
    name = input('Enter your username here: ')
    print(f'Hello {name}, Welcome to OLLABILL Global Bank')
    while attempt < max_attempt:
        user_pin = input('Enter your PIN here: ')
        if user_pin == PIN:
            while True:
                print(f'Hello {name}, welcome back.....')
                print('\n. ---OPTION MENU---')
                print('1. Check Balance')
                print('2. Deposit')
                print('3. Withdraw')
                print('4. Change PIN')
                print('5. Exit')

                option = input('Kindly enter your option number here: ')
                if option == '1':
                    check_balance()
                elif option == '2':
                    deposit()
                elif option == '3':
                    withdraw()
                elif option == '4':
                    change_pin()
                elif option == '5':
                    exit_transaction()
                    return
                else:
                    print('Invalid input, try again')
        else:
            attempt += 1
            print('Incorrect PIN, your attempt left:', max_attempt - attempt)
    if attempt == max_attempt:
        print('Your maximum attempt reached, account blocked for 24 hours')


if __name__ == '__main__':
    try:
        with open(file_name, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date and time', 'username', 'action', 'amount', 'balance'])
    except FileExistsError:
        pass
    main()