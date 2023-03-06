from models.recognized_word import RecognizedWord
from models.point import Point
from models.size import Size
from models.bounds import Bounds

class TesseractImageDataParser:
  def __init__(self, image_data):
    self.image_data = image_data

  def parse(self) -> list[RecognizedWord]:
    result: list[RecognizedWord] = []

    words: list[str] = self.get_all_words()
    for index, word in enumerate(words):
      point = self.get_point(index)
      size = self.get_size(index)
      line_number = self.get_line_number(index)

      recognized_word = RecognizedWord(
        point=point,
        size=size,
        text=word,
        line_number=line_number
      )
      result.append(recognized_word)
    return result

  def get_all_words(self) -> list[str]:
    return self.image_data.get('text')

  def get_x(self, at_index: int) -> int:
    return self.image_data.get('left')[at_index]

  def get_y(self, at_index: int) -> int:
    return self.image_data.get('top')[at_index]

  def get_width(self, at_index: int) -> int:
    return self.image_data.get('width')[at_index]

  def get_height(self, at_index: int) -> int:
    return self.image_data.get('height')[at_index]

  def get_point(self, at_index: int) -> Point:
    return Point(
      x=self.get_x(at_index),
      y=self.get_y(at_index)
    )

  def get_size(self, at_index: int) -> Size:
    return Size(
      width=self.get_width(at_index),
      height=self.get_height(at_index)
    )

  def get_line_number(self, at_index: int) -> int:
    return self.image_data.get('line_num')[at_index]
