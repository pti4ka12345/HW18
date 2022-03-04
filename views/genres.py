from flask_restx import Resource, Namespace

from HW18.dao.model.genre import GenreSchema
from HW18.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genres), 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        one_genre = genre_service.get_one(rid)
        return GenreSchema().dump(one_genre), 200
