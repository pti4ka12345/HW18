from HW18.dao.director import DirectorDAO
from HW18.dao.model.director import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.director_dao.get_all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")
