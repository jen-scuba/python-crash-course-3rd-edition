# Poll users about their dream vacation location
responses = {}
polling_action = True

while polling_action:
    name = input("What is your name? " )
    response = input("If you could visit one place in the world, where would you go? " )
    
    # Store the response
    responses[name] = response
    
    # Find out if anyone else wants to take the poll
    repeat = input("Would you like to let someone else take the poll? (yes/no) ")
    if repeat == 'no':
        polling_action = False
        
# Polling is complete. Show the results.
print("/n--- Polling Results--- ")

for name, response in responses.items():
    print(f"{name.title()}'s dream vacation would be to visit {response.title()}. ")
