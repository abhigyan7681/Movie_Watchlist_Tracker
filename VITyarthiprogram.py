movies = []

while True:
    print("\n--- MOVIE TRACKER MENU ---")
    print("1. Add a new movie")
    print("2. Show all movies")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        name = input("Movie Name: ")
        rating = input("Rating (0-10): ")
        
        movie_entry = {
            "title": name,
            "score": rating
        }
        movies.append(movie_entry)
        print(f"Saved: {name}")

    elif choice == "2":
        print("\n--- YOUR WATCH LIST ---")
        for m in movies:
            print(f"Movie: {m['title']} | Rated: {m['score']}/10")
            
    elif choice == "3":
        print("Goodbye!")
        break 
        
    else:
        print("Invalid choice, try again.")
