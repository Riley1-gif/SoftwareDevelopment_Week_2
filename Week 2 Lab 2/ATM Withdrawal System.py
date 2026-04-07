def PinSystem():
    correct_pin = 1234

  
    pin = int(input("Enter Pin: "))
    if pin == correct_pin:
        ATMSystem()
    else:
        print("Incorrect!")
        PinSystem()


    
def ATMSystem():
    balance = 500
    withdraw_amount = int(input("Enter withdrawel amount: "))
 
    if withdraw_amount > balance:
        print("Insufficient Funds!")
    else:
        balance -= withdraw_amount
        print(f"Withdrawel successful! Remaining Balance: {balance}")


PinSystem()