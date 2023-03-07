import unittest
from src.lib.recognized_words_within_bounds import RecognizedWordsWithinBounds
from tests.factories.bounds_factory import BoundsFactory
from tests.factories.point_factory import PointFactory
from tests.factories.recognized_word_factory import RecognizedWordFactory
from tests.factories.size_factory import SizeFactory

class TestRecognizedWordsWithinBounds(unittest.TestCase):
  def setUp(self):
    """
    ```
       0       10      20      30      40
     0 +-------+-------+-------+-------+----
       |
       |
    10 +       +-------+
       |       | rw_1  |
       |       |       |
    20 +       +-------+-------+
       |               | rw_2  |
       |               |       |
    30 +               +-------+
       |
       |
    40 +
       |
       |
    ```
    """

    default_size = SizeFactory.build(width=10, height=10)

    self.rw_1 = RecognizedWordFactory.build(point=PointFactory.build(x=10, y=10),
                                            size=default_size)

    self.rw_2 = RecognizedWordFactory.build(point=PointFactory.build(x=20, y=20),
                                            size=default_size)

    self.recognized_words = [self.rw_1, self.rw_2]

  def test_init(self):
    bounds = BoundsFactory.build()
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds)

    self.assertEqual(subject.recognized_words, self.recognized_words)
    self.assertEqual(subject.bounds, bounds)

  def test_get(self):
    """#get()"""

    """
    Given limits that only contains `rw_1`, calling `#get()` only returns `rw_1`.
    """
    bounds_that_only_contains_rw_1 = BoundsFactory.build(left=5, top=5, right=25, bottom=25)
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds_that_only_contains_rw_1)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 1)
    self.assertEqual(recognized_words_within_bounds[0], self.rw_1)

    """
    Given limits that only contains `rw_2`, calling `#get()` only returns `rw_2`.
    """
    bounds_that_only_contains_rw_2 = BoundsFactory.build(left=15, top=15, right=35, bottom=35)
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds_that_only_contains_rw_2)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 1)
    self.assertEqual(recognized_words_within_bounds[0], self.rw_2)

    """
    Given partial limits, calling `#get()` returns the ones within.
    """
    partial_bounds_that_only_contains_rw_2 = BoundsFactory.build(left=15, top=15)
    subject = RecognizedWordsWithinBounds(self.recognized_words, partial_bounds_that_only_contains_rw_2)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 1)
    self.assertEqual(recognized_words_within_bounds[0], self.rw_2)

    """
    Given limits that contains both `rw_1` and `rw_2`, calling `#get()` returns both.
    """
    bounds_that_contains_all = BoundsFactory.build(left=0, top=0, right=45, bottom=45)
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds_that_contains_all)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 2)
    self.assertListEqual(recognized_words_within_bounds, [self.rw_1, self.rw_2])

    """
    Given limits that contains one but partially, calling `#get()` does not return it.
    """
    bounds_that_contains_all = BoundsFactory.build(left=0, top=0, right=15, bottom=15)
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds_that_contains_all)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 0)

    """
    Given limits that contains none, calling `#get()` does not return any of them.
    """
    bounds_that_contains_none = BoundsFactory.build(left=0, top=0, right=10, bottom=10)
    subject = RecognizedWordsWithinBounds(self.recognized_words, bounds_that_contains_none)

    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 0)

    """
    Given limits that exactly matches `rw_1` or `rw_2` bounds, calling `#get()` returns it.
    """
    subject = RecognizedWordsWithinBounds(self.recognized_words, self.rw_1.bounds)
    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 1)
    self.assertEqual(recognized_words_within_bounds[0], self.rw_1)

    subject = RecognizedWordsWithinBounds(self.recognized_words, self.rw_2.bounds)
    recognized_words_within_bounds = subject.get()
    self.assertEqual(len(recognized_words_within_bounds), 1)
    self.assertEqual(recognized_words_within_bounds[0], self.rw_2)
