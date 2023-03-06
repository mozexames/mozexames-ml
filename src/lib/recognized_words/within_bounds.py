from models.recognized_word import RecognizedWord
from models.bounds import Bounds

class RecognizedWords:
  def __init__(self, recognized_words: list[RecognizedWord]):
    self.recognized_words = recognized_words

  def within_bounds(self, other_bounds: Bounds) -> list[RecognizedWord]:
    return list(filter(lambda rw: rw.bounds.within(other_bounds.as_tuple()), self.recognized_words))

