
---

# Secret Auction 🏆

Welcome to the **Secret Auction** project! This Python-based console program allows multiple users to place secret bids in an auction, and the program determines the winner based on the highest bid. The auction continues until all bidders have submitted their bids, and the results are displayed at the end.

## Features

- **Multiple Bidders**: The auction supports multiple participants who can place their bids secretly.
- **Highest Bidder Determination**: The program determines the winner by identifying the highest bid.
- **Simple Input/Output Interface**: Easy-to-use command-line interface to input names and bids.

## How It Works

1. The program will repeatedly ask users for their names and bid amounts.
2. After each bid, the user is prompted to check if there are more participants.
3. Once all bidders have placed their bids, the program will announce the winner (the one with the highest bid).

### Auction Flow
1. **Input your name and bid amount**.
2. **Decide if you want to add more bidders**.
3. **Display the highest bid** after all bids are entered.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PrernaUpadhyay/Secret_Auction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Secret_Auction
   ```
3. Run the Python script:
   ```bash
   python secret_auction.py
   ```

## Example

```bash
___________
\         /
)_______(
|"""""""|_.-._,---------.,_.-._
|       | | | |         | | | |
|_______| '-' '-'       '-' '-'

What is your name?: Alice
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no': yes

What is your name?: Bob
What is your bid?: $300
Are there any other bidders? Type 'yes' or 'no': no
The winner is Bob with a bid of $300
```

## Contributing

Feel free to fork the repository and submit pull requests with improvements, features, or bug fixes.

---

