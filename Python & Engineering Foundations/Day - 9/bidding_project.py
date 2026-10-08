import os

bidding = {}

def clear_terminal():
    # 'nt' means Windows, otherwise it's Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def best_bidder(bid):
    bidder = ''
    best_bid = 0
    for key,val in bid.items():
        if val > best_bid:
            best_bid = val
            bidder = key

    return bidder, best_bid

while True:
    name = input("Enter your Name: ")
    bid = int(input("What's your bid? $"))
    bidding[name] = bid
    want_to_bid = input("Does anyone else wanna bid?")
    if want_to_bid.lower() == 'yes':
        clear_terminal()
        continue
    else:
        clear_terminal()
        break

best_bid_name, best_bid_price = best_bidder(bidding)

print(f"The Winner is {best_bid_name} with a bid of ${best_bid_price}")