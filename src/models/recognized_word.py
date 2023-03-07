from dataclasses import dataclass, field
from .point import Point
from .size import Size
from .bounds import Bounds

@dataclass
class RecognizedWord:
  point: Point
  size: Size
  text: str
  line_number: int
  bounds: Bounds = field(init=False)

  def __post_init__(self):
    self.bounds = Bounds(self.point.x, self.point.y, self.point.x + self.size.width, self.point.y + self.size.height)


