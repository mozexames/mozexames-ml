import unittest

from src.models.bounds import Bounds

class TestBounds(unittest.TestCase):
  def test_init(self):
    bounds = Bounds(1, 2, 3, 4)

    self.assertEqual(bounds.left, 1)
    self.assertEqual(bounds.top, 2)
    self.assertEqual(bounds.right, 3)
    self.assertEqual(bounds.bottom, 4)

  def test_within(self):
    original_bounds = Bounds(0, 0, 100, 100)

    """is within"""
    other_bounds_that_are_equal = Bounds(0, 0, 100, 100).as_tuple()
    self.assertEqual(original_bounds.within(other_bounds_that_are_equal), True)

    other_bounds_that_are_within = Bounds(25, 25, 50, 50).as_tuple()
    self.assertEqual(original_bounds.within(other_bounds_that_are_within), True)

    """is not within"""
    other_bounds_that_are_not_partially_within = Bounds(0, 0, 100, 200).as_tuple()
    self.assertEqual(original_bounds.within(other_bounds_that_are_not_partially_within), False)

    other_bounds_that_are_not_completely_within = Bounds(-10, -10, 200, 200).as_tuple()
    self.assertEqual(original_bounds.within(other_bounds_that_are_not_completely_within), False)
