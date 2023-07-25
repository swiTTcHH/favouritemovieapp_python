movie = []

def add_movie():
    name = input("enter a movie name ")
    director = input("Enter a director name ")
    yr = input("Enter a release date ")
    movies = {
        "title": name,
        "director": director,
        "release_yr": yr
    }
    movie.append(movies)
    print(movie)
        
def view_movie(): 
    for itme in movie:
        print(f"Movie name is {itme['title']}, it was released in {itme['release_yr']}, director is {itme['director']}")
        
def find_movie():
    search = input("What are you Searching for?")
    for itme in movie:
        if search.lower() in itme['title'].lower():
            print(f"The movie you have searched for is {itme['title']}, release date is {itme['release_yr']}, director is {itme['director']}")
        
        else:
            print("No such movie in database")

while True:
    user_input = input("""Enter "a" to Add a  new movie, "v" to View movies in your list, "f" to Find a movie in your list, "q" to Terminate: """)

    if user_input == "a":
        print(add_movie())
        
    elif user_input == "v":
        print(view_movie())
        
    elif user_input == "f":
        print(find_movie())
    
    elif user_input == "q":
        exit()
        
    else:
        print("Wrong command please try again")
