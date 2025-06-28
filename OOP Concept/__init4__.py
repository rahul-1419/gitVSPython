class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    
    def menu(self):
        print("""
            What shuold you like to proceed
              1. Create pin
              2. Check balance
              3. Despoit amount
              4. Withdraw amount
              5. Exit
            """)
        
        user_input = int(input("Enter you want to proceed: "))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            print("check Balance")
        elif user_input == 3:
            print("Despoit amount")
        elif user_input == 4:
            print('Withdraw amount')
        elif user_input == 5:
            print("Good Bye")
        else:
            print('Enter 1 to 5 any Number to proceed your activity')
    
    def create_pin(self):
        pins = int(input("Enter Pin:"))
        self.pin = pins
        print('successful')



sbi = Atm()