from Seller import Seller
from Buyer import Buyer


class Market:
    def __init__(self):
        self.sellers = []
        self.buyers = []
        self.surplus= 0

    def add_sellers(self, seller:Seller()):
        self.sellers.append(seller)

    def add_buyers(self, buyer:Buyer()):
        self.buyers.append(buyer)

    def start_deals(self):
        for seller in self.sellers:
            for buyer in self.buyers:
                seller.show_price()
                buyer.show_offer()
                seller.offer = buyer.offer
                self.surplus = seller.price-buyer.offer
                print("Price:",seller.price,"Offer:",buyer.offer,"Surplus:", self.surplus)
                if seller.selling:
                    print(seller.gender,":Thank you for buying",seller.product,"\n")
                else:
                    print(seller.gender,":I want to keep it for me!\n")
                
#
market=Market()

for _ in range(5):
    b=Buyer()
    market.add_buyers(b)

for _ in range(1):
    s=Seller()
    market.add_sellers(s)

for day in range(7):
    print("\n==========> Day:",day+1,"<==========")
    market.start_deals()

