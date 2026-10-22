import json
from pathlib import Path

FILE = Path("accounts.json")

class Account:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("المبلغ يجب أن يكون موجباً")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("الرصيد غير كافٍ")
        self.balance -= amount

    def to_dict(self):
        return {"owner": self.owner, "balance": self.balance}

class SavingsAccount(Account):
    def init(self, owner, balance=0, rate=0.05):
        super().init(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate

def save(accounts):
    data = {name: acc.to_dict() for name, acc in accounts.items()}
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

def load():
    if not FILE.exists():
        return {}
    data = json.loads(FILE.read_text())
    return {n: Account(d["owner"], d["balance"]) for n, d in data.items()}

accounts = load()
acc = accounts.setdefault("Ali", Account("Ali"))
acc.deposit(500)
try:
    acc.withdraw(1000)
except ValueError as e:
    print("خطأ:", e)
save(accounts)