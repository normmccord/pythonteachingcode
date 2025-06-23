# P1M2 Norman McCord

# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return f"Norman McCord, the fish you're selling is a {fish} and you want ${price} for it? Wow!!!"

fish_entry = input("What fish are you selling: ")
price_entry = input("And what's the price: ")

print(fishstore(fish_entry, price_entry))
