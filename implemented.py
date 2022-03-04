from HW18.dao.director import DirectorDAO
from HW18.dao.genre import GenreDAO
from HW18.dao.movie import MovieDAO
from HW18.service.director import DirectorService
from HW18.service.genre import GenreService
from HW18.service.movie import MovieService
from HW18.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
