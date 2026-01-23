# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
bidding_dictionary = {}
def bid(person, bidprice):
    bidding_dictionary[person] = bidprice #Name is the key price is the value.
    # TODO-3: Whether if new bids need to be added



bidding_time = True
while bidding_time:
    name = input("What is your name? ")
    price = int(input("Bidding price: $"))
    bid(person= name, bidprice=price)
    bid_continuation = input("Are there any other bidders?If so type 'yes' if not type 'no'.").lower()
    if bid_continuation == "yes":
        print("\n" *50)
    elif bid_continuation == "no":
        bidding_time = False
        print("\n" *50)
        winner = max(bidding_dictionary, key=bidding_dictionary.get)
        highest_bid = max(bidding_dictionary.values())
        print(f"The winner is: {winner} and He won with ${highest_bid}")



# TODO-4: Compare bids in dictionary



