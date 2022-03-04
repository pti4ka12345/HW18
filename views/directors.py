from flask_restx import Resource, Namespace

from HW18.dao.model.director import DirectorSchema
from HW18.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_director = director_service.get_all()
        return DirectorSchema(many=True).dump(all_director), 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        one_director = director_service.get_one(rid)
        return DirectorSchema().dump(one_director), 200
