from Coin import Coin

class Wallet:
    def __init__(self, name):
        self.name = name
        self.id_account =12345
        self.balance =0
        self.currency ="DZ"
        self.transactions=[]
        self.crypto = []

    def get_balance(self):
        return self.balance

    def add_crypto(self, coin:Coin):
        self.crypto.append(coin)
        print("Add Crypto:",coin,"to",self.name,"Wallet")
            
    def echange_crypto(self, amount):
        for crypto in self.crypto:
            print("you have:",len(self.crypto),"coin(s) Crypto money")
            key = crypto.control_key
            crypto_value = crypto.get_value_from_key(key)
            self.balance += crypto_value
            print("Echange Crypto:",self.name,"Wallet",self.balance)
            self.crypto.remove(crypto)
            print("you have:",len(self.crypto),"coin(s) Crypto money")


    def add_money(self, amount):
        self.balance += amount
        transaction=("Add",self.id_account,self.name,amount,self.balance)
        self.transactions.append(transaction)
        print(transaction)
        print("- Adding:",amount,"to",self.name,"wallet's:",self.get_balance())


    def pay(self, price):
        if self.balance >= price:
            self.balance -= price
            transaction=("Buy",self.id_account,self.name,price,self.balance)
            self.transactions.append(transaction)
            print(transaction)
            print("-Buy with:",price,"your balance:",self.get_balance())
        else:
            print("- Credit insuffisant to buy you have:",self.get_balance())


    def send(self, other, amount):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            transaction=("Send",self.id_account,self.name,amount,self.balance)
            self.transactions.append(transaction)
            print(transaction)
            print("- Sending:",amount,"to",other.name,"wallet's:",self.get_balance())
        else:
            print("- Credit insuffisant to sending money",self.get_balance())

