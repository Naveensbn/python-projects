# =========== banking program in python==============
def show_balance(balance):
    print('===============================')
    print(f"your balance is {balance:.2f}rs./")
    # print('===============================')


def deposit():
    print('===============================')

    Amount=float(input(f"enter your deposit amount:"))
    if Amount < 0:
        print("that's not a valid amount")
        return 0
    else:
        return Amount


def withdraw(balance):
    print('===============================')

    Amount =int(input("enter withdrawn amount:"))
    if Amount>balance:
        print("insufficient funds")
        return 0
    elif Amount < 0:
        print("amount must be greater then 0")
        return 0

    else:
        return Amount


def main():
    balance = 1000
    is_running=True

    while is_running:
        print('===============================')
        print("------------Banking program-----------------")
        print("1.show balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        print('===============================')

        choice=int(input("enter your choice(1-4).."))
        if choice==1:
            show_balance(balance)
        elif choice==2:
            balance+=deposit()
            # deposit()
        elif choice==3:
            balance-=withdraw(balance)
            # withdraw()
        elif choice==4:
            is_running=False
        else:
            print('********************************')
            print("please enter valid choice")
            print('*********************************')

    print('--------------------------------------')
    print("Thank you! please visit again")
    print('--------------------------------------')


if __name__ == '__main__':
    main()
