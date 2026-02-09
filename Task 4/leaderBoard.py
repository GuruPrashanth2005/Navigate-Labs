leaderboard = eval(input("Leaderboard (list of tuples): "))
players = [p for p, _ in leaderboard]
duplicates = [p for p in set(players) if players.count(p) > 1]
sorted_board = sorted(leaderboard, key=lambda x: x[1], reverse=True)
print(f"Duplicates: {duplicates if duplicates else 'None'}")
print(f"Valid: {len(duplicates) == 0}")
print(f"Sorted leaderboard: {sorted_board}")