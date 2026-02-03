import time

class UniversalPayoutEngine:
    def __init__(self):
        self.market_price = 2.50 # Live PEG

    def convert_and_pay(self, user_id, usdt_amt, reason):
        print(f" [💸] PROCESSING PAYOUT: {user_id}")
        print(f"      Amount: ${usdt_amt:,.2f} USDT")
        print(f"      Rate:   ${self.market_price}/CDC")
        
        coins = usdt_amt / self.market_price
        print(f"      👉 SENT: {coins:,.4f} CODAC COINS to Wallet.")
        return coins
