favorite_places = {
    'smith':['new york','germany','roma']
    }
favorite_places2 = {
    'johnson':['hawaii','santorini','bali']
    }
favorite_places3 = {
    'willie':['maldives','karuizawa','queenstown']
    }
##print(favorite_places)
for name1,places1 in favorite_places.items():
##    print(f"{name1.title()} {places1.title()}")
    print(f"{name1.title()} liked place {places1.title()}")
    print(f"{places1.title()}")
