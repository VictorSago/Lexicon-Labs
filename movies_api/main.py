
from fastapi import FastAPI, HTTPException

app = FastAPI()

movies = [
    {"id": 1, "title": "Alien", "director": "Ridley Scott", "year": 1979},
    {"id": 2, "title": "Blade Runner", "director": "Ridley Scott", "year": 1982},
    {"id": 3, "title": "The Matrix", "director": "Lana Wachowski", "year": 1999},
    {"id": 4, "title": "Fight Club", "director": "David Fincher", "year": 1999},
    {"id": 5, "title": "Dead Man", "director": "Jim Jarmusch", "year": 1995},
    {"id": 6, "title": "Pi", "director": "Darren Aronofsky", "year": 1998},
    {"id": 7, "title": "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "director": "Stanley Kubrick", "year": 1964},
    {"id": 8, "title": "Modern Times", "director": "Charles Chaplin", "year": 1936},
    {"id": 9, "title": "Monty Python's Life of Brian", "director": "Terry Jones", "year": 1979},
    {"id": 10, "title": "Inside Man", "director": "Spike Lee", "year": 2006}
]

@app.get("/movies")
def get_movies():
    return movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


# Step 2:
# An existing id gives code 200, a missing id gives code 404, and abc gives 422

