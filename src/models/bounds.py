from dataclasses import dataclass
import ipdb

@dataclass
class Bounds:
  left: int
  top: int
  right: int
  bottom: int

  def within(self, other_bounds: tuple[int | None, int | None, int | None, int | None]) -> bool:
    left, top, right, bottom = other_bounds

    within_left = (left is None) or (left >= self.left)
    within_top = (top is None) or (top >= self.top)
    within_right = (right is None) or (right <= self.right)
    within_bottom = (bottom is None) or (bottom <= self.bottom)

    return within_left and within_top and within_right and within_bottom

  def as_tuple(self) -> tuple[int, int, int, int]:
    return (self.left, self.top, self.right, self.bottom)
