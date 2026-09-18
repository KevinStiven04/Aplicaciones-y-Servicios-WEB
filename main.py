

from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional,List
app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: ints
    reting: float
    category: str

class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    reting: float
    category: str


#app.title = "Mi primera aplicacion con FastAPI"
#app.version = "2.0"


movies = [{
    "id": 1,
    "title": "Avatar",
    "overview": "Es un exuberanter planete",
    "year": "2009",
    "reting": 7.8,
    "category": "Accion"
},
{   "id": 2,
    "title": "Avatar7777",
    "overview": "Es un exuberanter planete",
    "year": "2010",
    "reting": 7.8,
    "category": "Comedia"}]

@app.get('/', tags=['Home'])
def home():
    return "Hola mundo"

@app.get('/movies', tags=['Movies'])
def get_movies() -> List[Movie]:
    return movies


'''Parametros de tura son valores que pueden pasar por la URL '''

@app.get('/movies/{id}', tags=['Movies'])
def get_movies(id: int) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return movie
    return

'''Parametros QUERY:'''

@app.get('/moviesCA', tags=['Movies'])
def get_movies_by_category(category: str, year: int ) -> Movie:
    for movie in movies:
        if movie["category"] == category:
            return movie
    return []

'''Metodo POST'''

@app.post('/movies_Create', tags=['Movies'])
def create_movie(movie: Movie) -> List[Movie]:
    movies.append(movie.model_dump())
    return movies


'''Put and Delete'''

@app.put('/movies/{id}', tags=['Movies'])
def update_movie( id: int, movie: MovieUpdate ) -> List[Movie]:
    for item in movies:
        if item["id"]==id:
            item['title']= movie.title
            item['overview']=movie.overview
            item['year']=movie.year
            item['reting']=movie.reting
            item['category']=movie.category

    return movies

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id : int) -> List[Movie]:
    for movie in movies:
        if movie['id']==id:
            movies.remove(movie)

    return movies