import requests

def get_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    res = requests.get(url).json()

    if res.get("Response") == "True":
        plot = res.get("Plot", "N/A")
        poster = res.get("Poster", "N/A")
        genre = res.get("Genre", "N/A")
        rating = res.get("imdbRating", "N/A")
        return plot, poster, genre, rating
    else:
        return "N/A", "N/A", "N/A", "N/A"
