name = input("What's your name?")
income = int(input("How much do you earn each month?"))
expenses = int(input("How much do you spend each month for rent, utilities, internet and phone bill?"))
vexpences = input("What about Vriable expences(groceries, transportation and intertainment)")
savings = int(input("How much do you save each month?"))
apayment = input("What is your apartment down payment goal?")
month = input("How many months are left until your desired purchase?")


print(f"Name:{name}")
print(f"Monthly net income:{income}")
print(f"Expenses:{expenses}")
print(f"Variable expenses:{vexpences}")
print(f"Current savings amount:{savings}")
print(f"Apartment down payment goal:{apayment}")
print(f"Months until desired purchase:{month}")


s = input("What's your total monthly spending (sum of all categories)?")
sav = input("What's your monthly savings after expenses?")
savr = int(input("What's your saving rate percentage"))
pros = input("How much do you want to save after target month?")
mos = int(input("What's your total saving goal?"))
goals = int(input("How much extra money do you need to reach your goal?"))
qu = input("Is your monthly saving enough for your goal? ")
qu2 = input("What are you planning to do if it is shortfall or surplus?")


print(f"Total monthly expenses (sum of all categories){s}")
print(f"Monthly savings (income - expenses){sav}")
print(f"Savings rate percentage (savings / income * 100){savr}")
print(f"Projected savings after target months (monthly_savings * months){pros}")
print(f"Total projected amount (current_savings + projected_savings){mos}")
print(f"Monthly savings needed to reach goal (total_needed / months){goals}")
print(f"Additional monthly savings needed (can be negative if already sufficient){qu}")
print(f"Shortfall or surplus (total_projected - goal, negative = shortfall, positive = surplus){qu2}")


if expenses >= income:
    print("Your expenses are higher than your income")
if savings < 20:
    print("You have to save more")
if savr >= 20 and savr < 30:
    print("You are saving enough money")
if savr >= 30:
    print("You are saving more than needed")
if mos >= goals:
    print("You have to work hard")
