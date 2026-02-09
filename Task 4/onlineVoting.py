votes = eval(input("Votes (list of tuples): "))
voters = [v for v, _ in votes]
invalid = [v for v in set(voters) if voters.count(v) > 1]
vote_count = {}
for _, c in votes:
    vote_count[c] = vote_count.get(c, 0) + 1
print(f"Invalid voters: {invalid if invalid else 'None'}")
print(f"Vote count: {vote_count}")