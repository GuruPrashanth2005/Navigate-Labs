papers = eval(input("Papers (paper_id: [keywords]): "))
all_keywords = set().union(*papers.values()) if papers else set()
common_keywords = set(papers[next(iter(papers))]).intersection(*papers.values()) if papers and len(papers) > 1 else (set(papers[next(iter(papers))]) if papers else set())
paper_keyword_counts = {p: len(keywords) for p, keywords in papers.items()}
max_paper = max(paper_keyword_counts, key=paper_keyword_counts.get) if paper_keyword_counts else None
print(f"Total unique keywords: {len(all_keywords)}")
print(f"Common to all: {common_keywords if common_keywords else 'None'}")
print(f"Max keywords: {max_paper} ({paper_keyword_counts[max_paper] if max_paper else 0})")