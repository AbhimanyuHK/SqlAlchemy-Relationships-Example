from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db_config import DBConfig
from one_to_many.models.team import TeamModel


class PlayerModel(DBConfig.ONE_TO_MANY_DECLARATIVE_BASE):
    """Data model for players."""
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey(TeamModel.id), nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)

    # Relationships
    team = relationship(TeamModel, backref="players", cascade="save-update")
