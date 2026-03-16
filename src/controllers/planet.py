from src.models.planet import Planet
from typing import List

class PlanetController:
    @staticmethod
    def get_all_planets():
        # Return a list of all planets
        return [
            Planet(id=1, name="Earth", mass=5.972e24, radius=6371.0, description="Third planet from the Sun")
        ]

    @staticmethod
    def create_planet(request):
        # Create a new planet
        return Planet(id=2, name=request.name, mass=request.mass, radius=request.radius)
