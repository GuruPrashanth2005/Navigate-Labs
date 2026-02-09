user1_movies = {m.strip() for m in input("User 1 movies (comma-separated): ").split(",")}
user2_movies = {m.strip() for m in input("User 2 movies (comma-separated): ").split(",")}
common = user1_movies & user2_movies
either = user1_movies ^ user2_movies
print(f"\nCommon movies: {common if common else 'None'}")
print(f"Watched by either but not both: {either if either else 'None'}")
