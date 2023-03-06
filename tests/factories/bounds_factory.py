import factory
from src.models.bounds import Bounds

class BoundsFactory(factory.Factory):
  class Meta:
    model = Bounds

  left = 0
  top = 0
  right = 100
  bottom = 100
