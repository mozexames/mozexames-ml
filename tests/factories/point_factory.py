import factory
from src.models.point import Point

class PointFactory(factory.Factory):
  class Meta:
    model = Point

  x = factory.Faker('pyint', min_value=0, max_value=100)
  y = factory.Faker('pyint', min_value=0, max_value=100)

