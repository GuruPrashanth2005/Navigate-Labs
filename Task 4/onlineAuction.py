bids = eval(input("Bids (list of tuples): "))
max_bid_per_bidder = {}
for bidder, amount in bids:
    max_bid_per_bidder[bidder] = max(max_bid_per_bidder.get(bidder, 0), amount)
highest_bid = max(bids, key=lambda x: x[1]) if bids else (None, 0)
print(f"Highest bid per bidder: {max_bid_per_bidder}")
print(f"Highest single bid: {highest_bid[0]} ({highest_bid[1]})")