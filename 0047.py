current_users = ['rpo','carl','smith','K','rock']
for current_user in current_users:
    print(current_user.title())
new_users = ['james','john','robert','michale','william']
for new_user in new_users:
    if new_user in new_users:
        print("Type another name.")
    else:
        print("This username is not used.")
