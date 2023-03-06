import unittest
from dataclasses import fields, is_dataclass
from tests.factories.point_factory import PointFactory
from tests.factories.size_factory import SizeFactory
from src.models.recognized_word import RecognizedWord
import ipdb

class TestRecognizedWord(unittest.TestCase):
  def test_init(self):
    point = PointFactory.stub(x=10, y=10)
    size = SizeFactory.stub(width=20, height=20)

    recognized_word = RecognizedWord(point, size, 'Hi', 1)

    self.assertEqual(len(fields(recognized_word)), 5)
    self.assertEqual(is_dataclass(recognized_word), True)

    self.assertEqual(recognized_word.point, point)
    self.assertEqual(recognized_word.size, size)
    self.assertEqual(recognized_word.text, 'Hi')
    self.assertEqual(recognized_word.line_number, 1)
    self.assertEqual(recognized_word.bounds.left, 10) # point.x
    self.assertEqual(recognized_word.bounds.top, 10) # point.y
    self.assertEqual(recognized_word.bounds.right, 30) # point.x + size.width
    self.assertEqual(recognized_word.bounds.bottom, 30) # point.y + size.height
