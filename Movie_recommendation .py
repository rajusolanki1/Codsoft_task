movies = [
    {"title": "Avatar", "genre": "Sci-Fi"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "The Matrix", "genre": "Sci-Fi"},
    {"title": "Titanic", "genre": "Romance"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "Avengers: Endgame", "genre": "Action"},
    {"title": "John Wick", "genre": "Action"},
    {"title": "The Conjuring", "genre": "Horror"},
    {"title": "Annabelle", "genre": "Horror"},
    {"title": "Finding Nemo", "genre": "Animation"}
]

print("Available Movies:")
for movie in movies:
    print("-", movie["title"], "(", movie["genre"], ")")

user_movie = input("\nEnter your favorite movie: ")

genre = None
for movie in movies:
    if movie["title"].lower() == user_movie.lower():
        genre = movie["genre"]
        break

if genre:
    print("\nRecommended Movies:")
    for movie in movies:
        if movie["genre"] == genre and movie["title"].lower() != user_movie.lower():
            print("-", movie["title"])
else:
    print("\nMovie not found in the database.")
