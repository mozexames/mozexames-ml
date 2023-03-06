import factory
from src.models.size import Size

class SizeFactory(factory.Factory):
  class Meta:
    model = Size

  width = factory.Faker('pyint', min_value=0, max_value=100)
  height = factory.Faker('pyint', min_value=50, max_value=100)

