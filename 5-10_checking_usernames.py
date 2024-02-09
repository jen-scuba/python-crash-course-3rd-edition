current_users = ["admin", "jen", "dan", "lauren", "abbey"]
new_users = ["nick","Abbey","jill","DAN"]

for newbie in new_users:
    if newbie.casefold() in current_users:
        print(f"The username {newbie} has been taken, please pick a different username.")
    else:
        print(f"{newbie} is available.")
