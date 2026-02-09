transactions = eval(input("Transactions (list of dicts): "))
balance = {}
for t in transactions:
    aid = t['account_id']
    amount = t['amount'] if t['type'] == 'CREDIT' else -t['amount']
    balance[aid] = balance.get(aid, 0) + amount
max_balance = max(balance, key=balance.get) if balance else None
print(f"Final balance: {balance}")
print(f"Max balance: {max_balance} ({balance[max_balance] if max_balance else 0})")