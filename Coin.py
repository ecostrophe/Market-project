import hashlib
import random

class Coin:
    next_order_number = 1  #le numéro d'ordre chronique
    def __init__(self, value):
        self.order_number = Coin.next_order_number
        Coin.next_order_number += 1
        self.value = value
        self.name = "Mass"
        self.coin_id = self._generate_unique_id()
        self.control_key = self._generate_control_key()

    def _generate_unique_id(self):
        unique_str = f"{self.order_number}-{self.value}-{id(self)}"
        return hashlib.sha256(unique_str.encode()).hexdigest()[:8]

    def _generate_control_key(self):
        # Générer une clé de contrôle basée sur l'ID et la valeur
        key_str = f"{self.coin_id}-{self.value}"
        return hashlib.sha256(key_str.encode()).hexdigest()

    def get_value_from_key(self, key):
        # Récupérer la valeur à partir de la clé de contrôle
        expected_key = self._generate_control_key()
        if key == expected_key:
            return self.value
        else:
            return None

    def __str__(self):
        return f"Numéro d'ordre : {self.order_number},ID : {self.coin_id}, \nValeur : {self.value} ({self.name}), \nClé de contrôle : {self.control_key}\n"

