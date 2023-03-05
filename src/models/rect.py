from dataclasses import dataclass
from models.point import Point
from models.size import Size

@dataclass
class Rect:
  point: Point
  size: Size
