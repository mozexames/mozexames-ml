import unittest
from src.models.bounds import Bounds, PartialBounds

class TestPartialBounds(unittest.TestCase):
  def test_init(self):
    subject = PartialBounds()

    self.assertEqual(subject.left, None)
    self.assertEqual(subject.top, None)
    self.assertEqual(subject.right, None)
    self.assertEqual(subject.bottom, None)

    """
    Partially initialized
    """
    self.assertEqual(PartialBounds(left=1).left, 1)
    self.assertEqual(PartialBounds(top=1).top, 1)
    self.assertEqual(PartialBounds(right=1).right, 1)
    self.assertEqual(PartialBounds(bottom=1).bottom, 1)

class TestBounds(unittest.TestCase):
  def test_init(self):
    subject = Bounds(1, 2, 3, 4)

    self.assertEqual(subject.left, 1)
    self.assertEqual(subject.top, 2)
    self.assertEqual(subject.right, 3)
    self.assertEqual(subject.bottom, 4)

  def test_within(self):

    """#within()"""

    subject = Bounds(10, 10, 30, 30)

    """
    Given the `subject` bounds that is within the other bounds, returns `True`
    """
    other_bounds_within_subject = Bounds(5, 5, 35, 35)
    self.assertEqual(subject.within(other_bounds_within_subject), True)

    """
    Given other bounds that is exactly as the `subject` bounds, returns `True`
    """
    other_bounds_exactly_as_subject = Bounds(10, 10, 30, 30)
    self.assertEqual(subject.within(other_bounds_exactly_as_subject), True)

    """
    Given no limits to the `subject` bounds, returns `True`
    """
    no_limits = PartialBounds()
    self.assertEqual(subject.within(no_limits), True)

    """
    Given the `subject` bounds that are within or exactly at the partial left, top, right or bottom limits, returns `True`
    """
    self.assertEqual(subject.within(PartialBounds(left=0)), True)
    self.assertEqual(subject.within(PartialBounds(left=10)), True)

    self.assertEqual(subject.within(PartialBounds(top=0)), True)
    self.assertEqual(subject.within(PartialBounds(top=10)), True)

    self.assertEqual(subject.within(PartialBounds(right=40)), True)
    self.assertEqual(subject.within(PartialBounds(right=30)), True)

    self.assertEqual(subject.within(PartialBounds(bottom=40)), True)
    self.assertEqual(subject.within(PartialBounds(bottom=30)), True)

    self.assertEqual(subject.within(PartialBounds(top=0, bottom=40)), True)
    self.assertEqual(subject.within(PartialBounds(top=10, bottom=30)), True)

    self.assertEqual(subject.within(PartialBounds(left=0, right=40)), True)
    self.assertEqual(subject.within(PartialBounds(left=10, right=30)), True)

    self.assertEqual(subject.within(PartialBounds(top=0, left=0)), True)
    self.assertEqual(subject.within(PartialBounds(top=10, left=10)), True)

    self.assertEqual(subject.within(PartialBounds(right=40, bottom=40)), True)
    self.assertEqual(subject.within(PartialBounds(right=30, bottom=30)), True)

    """
    Given the `subject` bounds that are outside the partial left, top, right or bottom limits, returns `False`
    """
    self.assertEqual(subject.within(PartialBounds(left=11)), False)
    self.assertEqual(subject.within(PartialBounds(top=11)), False)
    self.assertEqual(subject.within(PartialBounds(right=29)), False)
    self.assertEqual(subject.within(PartialBounds(bottom=29)), False)

    """
    Given other bounds that is only partially within the `subject` bounds, returns `False`
    """
    other_bounds_partially_within_subject = Bounds(15, 15, 50, 50)
    self.assertEqual(subject.within(other_bounds_partially_within_subject), False)

    """
    Given other bounds that are not within the `subject` bounds, returns `False`
    """
    other_bounds_outside_subject = Bounds(40, 40, 50, 50)
    self.assertEqual(subject.within(other_bounds_outside_subject), False)

