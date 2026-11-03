# Reflection
# Reflection

# 1. I used the traceback to help me find the first bug.
# Debugging helped me understand how to find errors in my code.

# 2. apply_discount takes a price and a tier. It checks the tier
# and returns the price after applying the correct discount.

# 3. AI disclosure:
# I used ChatGPT to help explain Python concepts and understand
# errors. I tested the code to check that I understood how it 


#exersise 1 

def calculate_tax(price, rate):
    return price * rate 

tax1= calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%:):{tax1:.2f}")
print(f"Tax on $250 at 8%:):{tax1:.2f}")
print("Another tax: ${calculate_tax(150, 0.05)}")

#exersise 2 
def apply_discount(price, teir):
    if teir == "gold":
        return price * 0.85
    elif teir == "silver":
        return price * 0.90
    elif teir == "bronze":
        return price * 0.95
    else:
        return price 

    price = 200
    teirs =  ["gold", "silver", "bronze", "none"]

    for tier in tiers:
        print(f"{teir}: ${apply_discount(price,teir)}:.2f")


#-----exersise 3 ---


discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax= calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#---- Exersise 4 -----

orders = [(2000, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    final = final_price(price, tier, 0.07)
    print(f"Order: ${price:.2f}, Tier: {tier}, Final Price ${final:.2f}")



#------Exersise 6 -----

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)