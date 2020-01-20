accounts = {}


def welcome():
    print('Welcome to my bank')
    user_input = int(input('1 to create account, 2 for transaction: '))
    if user_input == 1:
        return create_accounts()
    elif user_input == 2:
        return transaction()
    else:
        print('Press 1 to create an account or 2 to carry out a transaction')


def create_accounts():
    balance = 0.0
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    if email not in accounts.keys():
        print('Your account has been created')
        accounts[email] = {'password': password, 'balance': balance}
        return transaction()
    else:
        print('An account with those details has been created')
        return create_accounts()


def transaction():
    """
    press 1: check balance
    press 2: deposit
    press 3: withdraw
    press 4: transfer
    :return:
    """
    user_email = input('Enter email: ')
    user_password = input('Enter password: ')
    if user_email not in accounts.keys():
        print('Incorrect password')
        return create_accounts()
    else:
        print('Authentication Successful')

        print('What can we help you with?')
        action = int(input('For balance Press 1: '
                           'For deposit Press 2: '
                           'For withdrawal Press 3: '
                           'For Transfers Press 4: '))

        if action == 1:
            return account_balance(user_email)

        elif action == 2:
            return deposit(user_email)

        elif action == 3:
            return withdraw(user_email)

        elif action == 4:
            return transfer(user_email)
        else:
            print('Not a valid number')
            return create_accounts()


def account_balance(user_email):
    balance = accounts[user_email]['balance']
    print('Your account balance is', balance)
    return transaction()


def deposit(user_email):
    print('Welcome to Deposits')
    amount = float(input('Enter amount: '))
    balance = accounts[user_email]['balance']
    accounts[user_email]['balance'] = balance + amount
    current_balance = accounts[user_email]['balance']
    print('Your new balance is {}'.format(current_balance))
    return transaction()


def withdraw(user_email):
    balance = accounts[user_email]['balance']
    if balance <= 0.0:
        print('Account is negative or zero')
        return deposit()
    print('Make withdrawal')
    amount = float(input('How much do you want to withdraw: '))
    if amount > balance:
        print('Insufficient funds')
        return withdraw()
    else:
        withdrawal = amount
        balance = accounts[user_email]['balance'] - withdrawal
        print('You have withdrawn {}'.format(withdrawal))
        print('Your new account balance is {}'.format(balance))
        return transaction()


def transfer(user_email):
    balance = accounts[user_email]['balance']
    amount = float(input('amount to withdraw: '))
    receiver = input('Enter receiver email: ')
    if amount > balance:
        print('Insufficient funds')
        return deposit()
    else:
        accounts[user_email]['balance'] = balance - amount
        current_balance = accounts[user_email]['balance']
        receiver_balance = accounts[receiver]['balance']
        accounts[receiver]['balance'] = receiver_balance + amount

        print('You transferred' + str(amount) + 'to' + receiver)
        print('Your new account balance is {}'.format(current_balance))

        return transaction()


welcome()

