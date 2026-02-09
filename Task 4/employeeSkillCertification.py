certs = eval(input("Certifications (employee: set([certs])): "))
all_certs = set().union(*certs.values()) if certs else set()
common_certs = set(certs[next(iter(certs))]).intersection(*certs.values()) if certs and len(certs) > 1 else (set(certs[next(iter(certs))]) if certs else set())
unique_certs = {c: [e for e in certs if c in certs[e] and sum(1 for emp in certs if c in certs[emp]) == 1] for c in all_certs}
unique = {c: unique_certs[c] for c in unique_certs if len(unique_certs[c]) > 0}
print(f"Common certs: {common_certs if common_certs else 'None'}")
print(f"Unique certs: {unique if unique else 'None'}")