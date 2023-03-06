import factory
from src.models.recognized_word import RecognizedWord
from tests.factories.bounds_factory import BoundsFactory
from tests.factories.point_factory import PointFactory
from tests.factories.size_factory import SizeFactory

class RecognizedWordFactory(factory.Factory):
  class Meta:
    model = RecognizedWord

  point = factory.SubFactory(PointFactory)
  size = factory.SubFactory(SizeFactory)
  text = factory.Faker('word')
  line_number = factory.Faker('pyint', min_value=0, max_value=3)


