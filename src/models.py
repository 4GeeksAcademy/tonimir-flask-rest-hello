from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship




db = SQLAlchemy()






class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorite_characters = relationship("FavoriteCharacter", back_populates="user")
    favorite_planets = relationship("FavoritePlanet", back_populates="user")
    favorite_vehicles = relationship("FavoriteVehicle", back_populates="user")


    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname
            
        }


class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    skin_color: Mapped[str] = mapped_column(String(20))
    eye_color: Mapped[str] = mapped_column(String(20))
    hair_color: Mapped[str] = mapped_column(String(20))
    height: Mapped[int] = mapped_column(nullable=True)
    mass: Mapped[int] = mapped_column(nullable=True)

    favorites = relationship("FavoriteCharacter", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "hair_color" : self.hair_color,
            "height" : self.height,
            "mass" : self.mass
        }
    

class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(50))
    terrain: Mapped[str] = mapped_column(String(50))
    climate: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[str] = mapped_column(String(50))
    rotation_period: Mapped[int] = mapped_column(nullable=True)
    orbital_period: Mapped[int] = mapped_column(nullable=True)
    gravity: Mapped[str] = mapped_column(String(50))
    surface_water: Mapped[int] = mapped_column(nullable=True)

    favorites = relationship("FavoritePlanet", back_populates="planet", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "diameter" : self.diameter,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "gravity" : self.gravity,
            "surface_water" : self.surface_water
        }


class Vehicle(db.Model):
    __tablename__ = "vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120))
    manufacturer: Mapped[str] = mapped_column(String(120))
    cost_in_credits: Mapped[str] = mapped_column(String(50))
    max_atmosphering_speed: Mapped[str] = mapped_column(String(50))
    crew: Mapped[str] = mapped_column(String(50))
    passengers: Mapped[int] = mapped_column(nullable=True)
    cargo_capacity: Mapped[int] = mapped_column(nullable=True)
    consumables: Mapped[str] = mapped_column(String(120))

    favorites = relationship("FavoriteVehicle", back_populates="vehicle", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables
        } 

class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)

    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
    

class FavoriteVehicle(db.Model):
    __tablename__ = "favorite_vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicle.id"), nullable=False)

    user = relationship("User", back_populates="favorite_vehicles")
    vehicle = relationship("Vehicle", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }