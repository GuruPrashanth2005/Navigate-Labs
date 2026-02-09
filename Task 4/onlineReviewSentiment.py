reviews = eval(input("Reviews (list of dicts): "))
sentiment_count = {}
for r in reviews:
    s = r['sentiment']
    sentiment_count[s] = sentiment_count.get(s, 0) + 1
max_sentiment = max(sentiment_count, key=sentiment_count.get) if sentiment_count else None
print(f"Sentiment counts: {sentiment_count}")
print(f"Most common: {max_sentiment}")