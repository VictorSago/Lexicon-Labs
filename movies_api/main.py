
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel


load_dotenv()
API_KEY = os.getenv("API_KEY")

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


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


def check_key(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        # If the API_KEY is missing or is wrong
        raise HTTPException(status_code=401)


def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


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


@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id, **movie.model_dump()}
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update(movie.model_dump())
    return existing


@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, changes: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(changes.model_dump(exclude_unset=True))
    return movie


@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movies.remove(find_movie(movie_id))


# Part 1, Step 2
# An existing id gives code 200, a missing id gives code 404, 
# and abc instead of an id gives code 422.

# Part 2, Step 3
# An empty body changes nothing: The movie returned has the same information 
# as before the call.
# With the year written as a string the results are of two kinds: if it's an
# integer within quotes then it's converted to int, but if it's a string that 
# isn't a number, the method returns status code 422: Unprocessable Content.
# With an id that doesn't exist the method returns status code 404.

# Part 2, Step 4
# Use PUT when the client has the complete movie and wants to replace it, so every field must be sent
# and anything left out is lost. Use PATCH when the client only wants to change one or a few fields,
# so the rest of the movie stays as it was and the client doesn't need to know or resend it.

# Part 3, Step 5
# POST without a key or with a wrong key both result in status code 401.
# Using the correct key gives status code 201 and creates a new entry.
