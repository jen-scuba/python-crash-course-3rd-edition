# a list of sandwich orders to fill
sandwich_orders = ["steak-n-cheese", "pastrami", "ham-n-cheese","pastrami", "turkey club", "pastrami", "chicken club"]
completed_sandwiches = []

print("No Pastrami today! We have run out of pastrami.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich != 'pastrami':
        print(f"The {current_sandwich.title()} sandwich is being made.")
    
        completed_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches have been completed. ")
for sandwich in completed_sandwiches:
    print(sandwich.title())