from db_config import DBConfig
from one_to_many.models import PlayerModel, TeamModel


class PlayerService:

    def __init__(self):
        self.con = DBConfig().connection()

    def all(self):
        return self.con.query(PlayerModel).all()

    def save(self, **kwargs):
        try:
            pm = PlayerModel()
            pm.name = kwargs.get("name")
            pm.position = kwargs.get("position")
            pm.team_id = kwargs.get("team_id")
            self.con.add(pm)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            raise e


if __name__ == "__main__":
    PlayerService().save()
