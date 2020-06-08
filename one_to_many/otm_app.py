from one_to_many.models.player import DBConfig

from one_to_many.service.player_service import PlayerService
from one_to_many.service.team_service import TeamService

db_config = DBConfig()
print("Creating one to many tables")
db_config.ONE_TO_MANY_DECLARATIVE_BASE.metadata.create_all(db_config.engine)
db_config.connection().commit()

team_data = {
    "name": "RCB",
    "city": "Bengaluru"
}

ps = PlayerService()
ts = TeamService()

tm = ts.get_by_filter_all(**team_data)
if tm is None:
    tm = ts.save(**team_data)

for x in range(3):
    player_data = {
        "name": "Abhimanyu {}".format(x),
        "position": "Player",
        "team_id": tm.id,
        "tm": tm
    }

    ps.save(**player_data)

for p in ps.all():
    print(p.__dict__, p.team.__dict__)
