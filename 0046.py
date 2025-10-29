usernames = ['admin','carl','smith','K','rock']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hey! {username.title()} thank you for logging in again.")
else:
    print("We need to find some users!")
