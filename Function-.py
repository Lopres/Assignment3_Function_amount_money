def get_the_amount_of_money():
    Money_Func = int(input("How much money do you have :"))
    return Money_Func

def get_the_price_of_the_apple():
    Apples_Func = int(input("How much is the apple? :"))
    return Apples_Func

def get_the_apples_you_can_get():
    apples_you_can_get = (Money // price_of_apple)
    return apples_you_can_get

def compute_amount(Money, Apples, price_of_apple):
    remaining_money = (Money & (apples_you_can_get // Apples))
    return remaining_money

def display_remaining_money(remaining_money):
    print(f"You can buy {apples_you_can_get} and your changed is {remaining_money}")










# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
Money = get_the_amount_of_money()
Apples = get_the_price_of_the_apple()
# Display the maximum number of apples that you can buy and the remaining money that you will have.
price_of_apple = 20
apples_you_can_get = get_the_apples_you_can_get()
remaining_money = compute_amount(Money, Apples, price_of_apple)
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.
display_remaining_money(remaining_money)