"""
Demonstrando a preocupação da importância
da segurança ao usar threads.

Quando várias threads compartilham o mesmo 
conjunto de dados ao mesmo tempo
"""

import random
import threading
import time
from typing import List


class Account:
    def __init__(self, amount: int = 0) -> None:
        self.amount = amount


def main() -> None:
    accounts = create_accounts()
    total = sum(account.amount for account in accounts)

    print("Init transfers...")

    tasks = [
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
    ]

    [task.start() for task in tasks]
    [task.join() for task in tasks]

    print("Transfers completed!")

    validate_bank(accounts, total)


def services(accounts: List, total: int) -> None:
    for _ in range(1, 10000):
        c1, c2 = get_two_accounts(accounts)
        value = random.randint(1, 100)
        transfer(c1, c2, value)
        validate_bank(accounts, total)


def create_accounts() -> List[Account]:
    return [
        Account(amount=random.randint(5000, 10000)),
        Account(amount=random.randint(5000, 10000)),
        Account(amount=random.randint(5000, 10000)),
        Account(amount=random.randint(5000, 10000)),
        Account(amount=random.randint(5000, 10000)),
        Account(amount=random.randint(5000, 10000)),
    ]


def transfer(origin: Account, destiny: Account, value: int) -> None:
    if origin.amount < value:
        return

    origin.amount -= value
    time.sleep(0.001)
    destiny.amount += value


def validate_bank(accounts: List[Account], total: int) -> None:
    current = sum(account.amount for account in accounts)

    if current != total:
        print(f"Erro: inconsistent balance. {current:.2f} vs {total:.2f}", flush=True)
    else:
        print("Account balance checked successfully!")


def get_two_accounts(accounts: List[Account]):
    c1 = random.choice(accounts)
    c2 = random.choice(accounts)

    while c1 == c2:
        c2 = random.choice(accounts)

    return c1, c2


if __name__ == "__main__":
    main()
