from db_config import DBConfig
from one_to_many.models import TeamModel


class TeamService:

    def __init__(self):
        self.con = DBConfig().connection()

    def get_all(self):
        return self.con.query(TeamModel).all()

    def save(self, name, city):
        team = TeamModel()
        team.name = name
        team.city = city
        self.con.add(team)
        self.con.commit()
        return team

    def get_by_filter_all(self, name, city):
        return self.con.query(TeamModel).filter(
            TeamModel.name == name, TeamModel.city == city
        ).first()


if __name__ == "__main__":
    data = {
        "name": "RCB",
        "city": "Bengaluru"
    }
    for x in TeamService().get_by_filter_all(**data):
        print(x)
