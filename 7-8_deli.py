# a list of sandwich orders to fill
sandwich_orders = ["steak-n-cheese", "pastromi", "ham-n-cheese", "club"]
completed_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"The {current_sandwich.title()} sandwich is being made.")
    
    completed_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches have been completed. ")
for sandwich in completed_sandwiches:
    print(sandwich.title())