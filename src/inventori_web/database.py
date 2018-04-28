from flask_sqlalchemy import SQLAlchemy
import Enum

db = SQLAlchemy()
Column = db.Column
Base = db.Base

# TODO: Code relationships

# Helper table for the m-m relationship of tools/reservation
reservation_helper = db.Table(
    "reservation_helper",
    db.Column(
        "reservation_id",
        db.Integer,
        db.ForeignKey("reservations.id"),
        primary_key=True
    ),
    db.Column(
        "tool_id",
        db.Integer,
        db.ForeignKey("tools.id"),
        primary_key=True
    )
)


class UsageFunctions(Enum):
    """Enum to list item functions"""
    unspecified = 0
    hand_tool = 1
    electric_tool = 2
    electronic_component = 3
    raw_metal = 4
    raw_plastic = 5
    computer_accesory = 6


class Consumable(Base):
    """Table that """
    __tablename__ = "consumables"
    id = Column(db.Integer, primary_key=True)
    team_id = Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    guardian_id = Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    location_id = Column(db.Ingeger, db.ForeignKey("locations.id"))
    quantity = Column(db.Integer, default=0)
    name = Column(db.String, unique=True)
    description = Column(db.String)
    function = Column(db.Enum(UsageFunctions))
    picture_path = Column(db.String)


class Tool(Base):
    __tablename__ = "tools"
    id = Column(db.Integer, primary_key=True)
    team_id = Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    guardian_id = Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    location_id = Column(db.Ingeger, db.ForeignKey("locations.id"))
    name = Column(db.String, unique=True, nullable=False)
    description = Column(db.String, nullable=False)
    function = Column(db.Enum(UsageFunctions))
    placa = Column(db.String)
    working_state_state = Column(db.String)
    working_state_description = Column(db.String)
    picture_path = Column(db.String)
    barcode_id = Column(db.String)


class Location(Base):
    __tablename__ = "locations"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, unique=True)
    description = Column(db.String)
    picture_path = Column(db.String)
    barcode_id = Column(db.String)


class Team(Base):
    __tablename__ = "teams"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, unique=True)
    description = Column(db.String)


class User(Base):
    __tablename__ = "users"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, unique=True)
    picture_path = Column(db.String)
    punishment = Column(db.String, default=False)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(db.Integer, primary_key=True)
    user_id = Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
