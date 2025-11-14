# 5. Simple Login System
users = {"admin": "1234", "user1": "password", "john": "hello"}
while True:
    print("\n=== Login System ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print(f"Welcome {username}! Login successful.")
        break
    else:
        print("Invalid username or password!")
        retry = input("Try again? (y/n): ").lower()
        if retry != 'y':
            print("Goodbye!")
            break