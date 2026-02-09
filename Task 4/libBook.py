books = eval(input("Borrow records (list of dicts): "))
over7days = [b['student'] for b in books if b['days'] > 7]
book_count = {}
for b in books:
    book_count[b['book']] = book_count.get(b['book'], 0) + 1
print(f"Over 7 days: {set(over7days)}")
print(f"Book counts: {book_count}")
