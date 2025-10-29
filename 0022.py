users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }

for username, user_into in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_into['first']} {user_into['last']}"
    location = user_into['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")
    
