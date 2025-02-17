"""Q1: A banking application allows users to withdraw money. The function withdraw(balance,
amount) should check if the withdrawal amount is greater than the balance. If yes, it should
raise an exception "Insufficient funds", otherwise return the new balance."""

def amount_withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    user_balance = 10000
    withdrawal_amount = int(input("Enter your Withdrwal amount: RM "))
    user_new_balance = amount_withdraw(user_balance, withdrawal_amount)
    print(f"You have withdrawn successfully RM {withdrawal_amount}, Now your New balance: RM {user_new_balance}")
except ValueError as e:
    print(e)