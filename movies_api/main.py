
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


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


class Movie(BaseModel):
    title: str
    director: str
    year: int


def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")
# An existing id gives code 200, a missing id gives code 404, 
# and abc instead of an id gives code 422.


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    result = movies
    if director is not None:
        result = [m for m in result if director.lower() in m["director"].lower()]
    if year is not None:
        result = [m for m in result if m["year"] == year]
    return result


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)


@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id, **movie.model_dump()}
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update(movie.model_dump())
    return existing


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    movies.remove(find_movie(movie_id))
