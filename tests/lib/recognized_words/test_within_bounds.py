# import unittest

# from src.lib.recognized_words.within_bounds import RecognizedWords
# from src.models.recognized_word import RecognizedWord
# from tests.factories.bounds_factory import BoundsFactory
# from tests.factories.point_factory import PointFactory
# from tests.factories.recognized_word_factory import RecognizedWordFactory
# from tests.factories.size_factory import SizeFactory

# class TestRecognizedWordsWithinBounds(unittest.TestCase):
#   def setUp(self):
#     default_size = SizeFactory.stub(width=10, height=10)

#     rw_1 = RecognizedWordFactory.stub(point=PointFactory.stub(x=10, y=10),
#                                       size=default_size)
#     rw_2 = RecognizedWordFactory.stub(point=PointFactory.stub(x=20, y=20),
#                                       size=default_size)

#     self.recognized_words = [rw_1, rw_2]

#   # def test_init(self):
#   #   bounds = Bounds(1, 2, 3, 4)

#   #   self.assertEqual(bounds.left, 1)
#   #   self.assertEqual(bounds.top, 2)
#   #   self.assertEqual(bounds.right, 3)
#   #   self.assertEqual(bounds.bottom, 4)

#   # def test_within(self):
#   #   original_bounds = Bounds(0, 0, 100, 100)

#   #   """is within"""
#   #   other_bounds_that_are_equal = Bounds(0, 0, 100, 100).as_tuple()
#   #   self.assertEqual(original_bounds.within(other_bounds_that_are_equal), True)

#   #   other_bounds_that_are_within = Bounds(25, 25, 50, 50).as_tuple()
#   #   self.assertEqual(original_bounds.within(other_bounds_that_are_within), True)

#   #   """is not within"""
#   #   other_bounds_that_are_not_partially_within = Bounds(0, 0, 100, 200).as_tuple()
#   #   self.assertEqual(original_bounds.within(other_bounds_that_are_not_partially_within), False)

#   #   other_bounds_that_are_not_completely_within = Bounds(-10, -10, 200, 200).as_tuple()
#   #   self.assertEqual(original_bounds.within(other_bounds_that_are_not_completely_within), False)
