from bitcoinlib.wallets import Wallet, wallet_exists, wallet_delete
from bitcoinlib.mnemonic import Mnemonic

from json import dump

mnemonic = Mnemonic()


class WalletBitcoin:
    def __init__(self, name: str) -> None:
        self.name = name
        self.address = self.load()

    def create(self):
        words = mnemonic.generate(strength=256)
        wallet = Wallet.create(self.name, keys=words, network="bitcoin")

        address = wallet.get_key().address

        data = {"name": self.name, "address": address, "words": words}
        with open("wallet.json", "w", encoding="utf-8") as file:
            dump(data, file, indent=4)
        return address

    def load(self) -> str:
        if wallet_exists(self.name):
            return Wallet(self.name).get_key().address
        return self.create()


if __name__ == "__main__":
    wallet_name = input("Digite um nome para sua carteira: ")
    if wallet_name:
        wallet = WalletBitcoin(wallet_name)
        print(f"Carteira criada: {wallet.address}")
