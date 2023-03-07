from models.bounds import Bounds, PartialBounds
from models.recognized_word import RecognizedWord

class RecognizedWordsWithinBounds:
  def __init__(self, recognized_words: list[RecognizedWord], bounds: Bounds | PartialBounds):
    self.recognized_words = recognized_words
    self.bounds = bounds

  def get(self) -> list[RecognizedWord]:
    # Filter out any recognized words outside the specified limit bounds
    return list(filter(lambda rw: rw.bounds.within(self.bounds), self.recognized_words))

