import unittest
from dataclasses import fields, is_dataclass
from tests.factories.point_factory import PointFactory
from tests.factories.size_factory import SizeFactory
from src.models.recognized_word import RecognizedWord

class TestRecognizedWord(unittest.TestCase):
  def test_init(self):
    point = PointFactory.build(x=10, y=10)
    size = SizeFactory.build(width=20, height=20)
    subject = RecognizedWord(point, size, 'Hi', 1)

    self.assertEqual(len(fields(subject)), 5)
    self.assertEqual(is_dataclass(subject), True)

    self.assertEqual(subject.point, point)
    self.assertEqual(subject.size, size)
    self.assertEqual(subject.text, 'Hi')
    self.assertEqual(subject.line_number, 1)
    self.assertEqual(subject.bounds.left, 10) # point.x
    self.assertEqual(subject.bounds.top, 10) # point.y
    self.assertEqual(subject.bounds.right, 30) # point.x + size.width
    self.assertEqual(subject.bounds.bottom, 30) # point.y + size.height
