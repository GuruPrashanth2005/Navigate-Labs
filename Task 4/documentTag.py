docs = eval(input("Documents (list of dicts): "))
tagless = [d['doc_id'] for d in docs if not d.get('tags') or len(d['tags']) == 0]
all_tags = set().union(*[set(d['tags']) for d in docs if d.get('tags')])
common_tags = set(docs[0]['tags']).intersection(*[set(d['tags']) for d in docs[1:]]) if len(docs) > 1 and all(d.get('tags') for d in docs) else (set(docs[0]['tags']) if docs and docs[0].get('tags') else set())
print(f"Tagless docs: {tagless if tagless else 'None'}")
print(f"Tags in every doc: {common_tags if common_tags else 'None'}")