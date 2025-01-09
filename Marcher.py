import random
import xlsxwriter
import matplotlib.pyplot as plt

class Produit:
    def __init__(self, nom, description, prix_initial, quantite):
        self.nom = nom
        self.description = description
        self.tva = 10
        self.prix = prix_initial
        self.quantite = quantite
        self.abondance = True
        self.demande = True


class Vendeur:
    def __init__(self, nom):
        self.nom = nom
        self.capital = 500000
        self.inventaire = []
        self.satisfaction=1
        self.impots = 0
        
    def set_prix(self, produit:Produit):
        marge = random.randint(0,int((produit.prix*self.satisfaction)/100))
        tva= int(((produit.prix*produit.tva)/100))
        produit.prix += (marge+tva)
        
        
    def ajouter_produit(self, produit:Produit):
        if self.capital >= produit.prix:
            self.capital -= produit.prix
            self.set_prix(produit)
            self.inventaire.append(produit)
            return True
        return False

    def proposer_produit(self):
        produit_choisi= random.choice(self.inventaire)
        return produit_choisi

    def accepter_offre(self, produit:Produit, offre):
        if offre >= produit.prix:  # Accepte si l'offre moins 90% du prix
            self.capital += offre
            self.impots+= int(((produit.prix*produit.tva)/100))
            produit.quantite -= 1
            if produit.quantite <= 0:
                self.inventaire.remove(produit)
            return True
        return False

    def payer_frais(self):#chaque 29
        loyer = 20000
        frais= 30000
        if self.capital <= 360000:
            self.impots += int(20*self.capital/100)
        elif self.capital < 1440000:
            self.impots += int(30*self.capital/100)
        elif self.capital >= 1440000:
            self.impots += int(35*self.capital/100)
        self.capital -= (loyer+frais+self.impots)
        self.impots = 0

class Acheteur:
    def __init__(self, nom, budget):
        self.nom = nom
        self.budget = budget
        self.panier = []

    def faire_offre(self, produit:Produit):
        if self.budget >= produit.prix:
            #Offre aléatoire de 80% et 100% du prix
            if produit.abondance:
                ratio_offre=0
            if produit.demande:
                ratio_offre=0
            offre = random.randint(int(produit.prix*80/100),produit.prix)
            return offre
        return 0

    def acheter_produit(self, produit, prix):
        if self.budget >= prix:
            self.budget -= prix
            self.panier.append(produit)
            return True
        return False

class Marche:
    def __init__(self):
        self.vendeurs = []
        self.acheteurs = []
        self.historique = []

    def demarrer_simulation(self, jours):
        for jour in range(1,jours):
            for acheteur in self.acheteurs:
                if jour%30==0:
                    acheteur.budget += salaire
                for vendeur in self.vendeurs:
                    if jour%29==0:
                        vendeur.payer_frais()
                    for produit in vendeur.inventaire:
                        offre = acheteur.faire_offre(produit)
                        decision=vendeur.accepter_offre(produit, offre)
                        if decision:
                            acheteur.acheter_produit(produit, offre)
                        self.historique.append((jour,
                        vendeur.nom,vendeur.capital,vendeur.impots,
                        produit.nom,produit.prix,
                        produit.tva,produit.prix,
                        acheteur.nom,acheteur.budget,round(offre,1),
                        decision,round(offre-produit.prix,1)))
                       
    
    def plot_historique(self):
        # Affichage de l'historique des transactions
        days=[]
        capital=[]
        budget=[]
        impot= []
        for transaction in self.historique:
            days.append(transaction[0])
            capital.append(transaction[2])
            impot.append(transaction[3])
            budget.append(transaction[9])
            
        plt.plot(days,capital, color='b', label ="Vendeur Capital")
        plt.plot(days,impot, color='r', label ="Vendeur Impot")
        plt.plot(days,budget, color='g', label ="Acheteur Budget")
        plt.title("Market Data Project")
        plt.xlabel("Jours")
        plt.ylabel("Argent")
        plt.grid()
        plt.legend()
        plt.show()


class StockData:
	def __init__(self, historique):
		row=0
		col=0
		workbook = xlsxwriter.Workbook('MarketData.xlsx')
		worksheet = workbook.add_worksheet()
		# Add header row
		header_row = ["ID_Operation","Jour", "Vendeur","Capital","Impots","Produits","Prix_initial" ,"TVA","Prix", "Acheteur","Budget", "Offre", "Decision", "Difference"]
		for i, header in enumerate(header_row):
			worksheet.write(row, i, header)
		row += 1
		# Write data for each transaction of Market 
		for n in range(len(historique)):
			worksheet.write(row, col , n)
			worksheet.write(row, col+1, historique[n][0])
			worksheet.write(row, col+2, historique[n][1])
			worksheet.write(row, col+3, historique[n][2])
			worksheet.write(row, col+4, historique[n][3])
			worksheet.write(row, col+5, historique[n][4])
			worksheet.write(row, col+6, historique[n][5])
			worksheet.write(row, col+7, historique[n][6])
			worksheet.write(row, col+8, historique[n][7])
			worksheet.write(row, col+9, historique[n][8])
			worksheet.write(row, col+10, historique[n][9])
			worksheet.write(row, col+11, historique[n][10])
			worksheet.write_boolean(row, col+12, historique[n][11])
			worksheet.write(row, col+13, historique[n][12])
			row+=1
		workbook.close()

produits=[
["Pomme", "Rouge et juteuse", 250, 10],
["Poire", "Jaune et sucrée", 400, 5],
["Tomate", "Rouge ", 150, 5],
["Patate", "Jaune du Oued", 100, 5],
["Onion", "très bonne", 70, 5],
["Poulet", "vidée et frais", 390, 15],
["Carotte", "bonne qualité", 90, 50],
["Sardine", "pêche du Collo", 650, 5],
["banane", "NA", 360, 5],
["orange", "NA", 250, 5],
["fraise", "NA", 450, 5],
["raisin", "NA", 350, 5],
["cerise", "NA", 1050, 5],
["ananas", "NA", 950, 5],
["mangue","NA", 950, 5],
["concombre", "NA", 150, 5],
["salade","NA", 90, 5],
["aubergine", "NA", 110, 5],
["potimarron","NA", 180, 5],
["lait", "NA", 25, 5],
["yaourt", "NA", 50, 5],
["fromage", "NA", 150, 5],
["crème","NA", 170, 5],
["beurre","NA", 280, 5],
["agneau","NA", 2350, 5],
["veau","NA", 1850, 5],
["saumon","NA", 1350, 5],
["thon","NA", 950, 5],
["cabillaud","NA", 2050, 5],
["truite","NA", 1650, 5],
["maquereau","NA", 1750, 5],
["crevette","NA", 4500, 5],
["moule","NA", 950, 5],
["huître","NA", 1250, 5],
["calmar","NA", 1450, 5],
["crabe","NA", 1050, 5]]
# Création des instances
salaire= 30000
nom_acheteurs=["Eco","Massil","Zouzou","Massilia","Maissa"]


marche = Marche()
random.shuffle(produits)
vendeur = Vendeur("Ali")
for produit in produits:
    vendeur.ajouter_produit(Produit(produit[0],produit[1],produit[2],produit[3]))
#
marche.vendeurs.append(vendeur)
acheteur= Acheteur(random.choice(nom_acheteurs), salaire)
marche.acheteurs.append(acheteur)

# Démarrage de la simulation
marche.demarrer_simulation(100)
st=StockData(marche.historique)
marche.plot_historique()
