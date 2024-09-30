# ASCII art logo
logo = """
___________
\\ /
)_______(
| """""""|_.-._,.---------.,_.-._
| | | | | | '' -.
| | _ | | _   
_ | | _.. - '
| _______ | '-'
`'---------'`
'-'
)"""""""(
 / _________ \\
    `'-------'`
    . - ------------.
jgs / _______________ \\
 \\
 \\
"""

def find_highest_bidder(bidding_dictionary):
    """Determines the highest bidder from the bidding dictionary."""
    winner = ""
    highest_bid = 0

    # Loop through each bidder in the dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]  # Access the bid amount for each bidder
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    # Print the winner with the highest bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Display the logo
print(logo)

# Dictionary to store bids
bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # Add name and bid to the bids dictionary
    bids[name] = price

    # Ask if there are other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n"* 20)
print("\nThanks for participating!")


