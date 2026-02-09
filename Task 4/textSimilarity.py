doc1 = set(input("Document 1 words: ").split())
doc2 = set(input("Document 2 words: ").split())
intersection = len(doc1 & doc2)
union = len(doc1 | doc2)
jaccard = intersection / union if union > 0 else 0
similar = "Yes" if jaccard >= 0.5 else "No"
print(f"Jaccard similarity: {jaccard:.2f}")
print(f"Similar: {similar}")