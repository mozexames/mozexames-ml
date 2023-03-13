from typing import List
from .recognized_words_within_bounds import RecognizedWordsWithinBounds
from .question_number_parser import QuestionNumberParser
from models.bounds import Bounds
from models.recognized_word import RecognizedWord
from pydash import sort_by, find


class QuestionNumbersFinder:
  THRESHOLD_X = 32

  def __init__(self, recognized_words: List[RecognizedWord], paper_height: int) -> None:
    self.recognized_words = recognized_words
    self.paper_height = paper_height

    self.__cached_sample = None
    self.__cached_find = None

  def find(self) -> List[RecognizedWord]:
    """
    Find all question numbers in the paper.
    """

    if self.__cached_find is not None:
      return self.__cached_find

    question_numbers_column_limits = self.column_limits()
    if question_numbers_column_limits is None:
      return []

    possible_question_numbers = RecognizedWordsWithinBounds(self.recognized_words, question_numbers_column_limits).get()
    question_numbers = list(filter(lambda rw: QuestionNumberParser(rw.text).valid(), possible_question_numbers))
    return question_numbers

  def _sample_one(self) -> RecognizedWord | None:
    """
    Find and return one of the closest question numbers to the left edge of the paper.
    """

    if self.__cached_sample is not None:
      return self.__cached_sample

    # 1. Sort all recognized words by their "left" bound in ASC order
    recognized_words_sorted_by_left_bound = sort_by(self.recognized_words, 'bounds.left')

    # 2. Take one question number as a sample
    question_number: RecognizedWord | None = find(recognized_words_sorted_by_left_bound,
                                                 lambda rw: QuestionNumberParser(rw.text).valid())
    return question_number

  def column_limits(self) -> Bounds | None:
    """
    Determine the limits for question numbers in the paper.

    ```
    # For example, on the paper below, if we find any of the numbers,
    # and look up all the other text on the same column, we can determine
    # the rest. This is because any of the exam paper numbered list is indented at the same level.

    +--------------+
    | ; 1. ;       |
    | ; 2. ;       |
    | ; 3. ;       |
    | * 4. *       |
    | ; 5. ;       |
    | ; 6. ;       |
    | ; 7. ;       |
    | ; 8. ;       |
    +--------------+

    # E.g: Sampling one of the number (i.e. 4.) we can grab its X bounds add some threshold,
    # and look up from the beginning (top) of the paper, to the end (bottom) of the paper
    # for any text within the same column.
    ```
    """

    sample = self._sample_one()
    if sample is None:
      # TODO: maybe raise?
      return None

    sample_bounds = sample.bounds
    return Bounds(sample_bounds.left - self.THRESHOLD_X, 0, sample_bounds.right + self.THRESHOLD_X, self.paper_height)
