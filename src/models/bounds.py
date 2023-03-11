from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class Bounds:
  left: int
  top: int
  right: int
  bottom: int

  def within(self, other_bounds: 'PartialBounds | Bounds') -> bool:
    """
    Returns whether or not `this` instance of bounds is completely within an`other` instance of partial or fully defined bounds.

    ```
       0       10      20      30      40
     0 +-------+-------+-------+-------+------
       |
       |
    10 +       +---------------+
       |       | A             |
       |       |               |
    20 +       |       +-------+-------+
       |       |       | B     |       |
       |       |       |       |       |
    30 +       +-------+-------+       |
       |               |               |
       |               |               |
    40 +               +---------------+
       |
       |       On this example, Bounds B is not completely within Bounds A, so this method returns False
       |       on both bounds.


       0       10      20      30      40
     0 +-------+-------+-------+-------+------
       |
       |
    10 +       +---------------+
       |       | A             |
       |       |               |
    20 +       |               |
       |       |               |
       |       |               |
    30 +       |  +---------+  |
       |       |  | B       |  |
       |       |  |         |  |
    40 +       |  +---------+  |
       |       |               |
       |       |               |
    60 +       +---------------+
       |
       |       On this example, Bounds B is within Bounds A, so this method returns True for Bounds A.
    ```
    """
    if self == other_bounds:
      return True

    within_left = (other_bounds.left is None) or (self.left >= other_bounds.left)
    within_top = (other_bounds.top is None) or (self.top >= other_bounds.top)
    within_right = (other_bounds.right is None) or (self.right <= other_bounds.right)
    within_bottom = (other_bounds.bottom is None) or (self.bottom <= other_bounds.bottom)

    return within_left and within_top and within_right and within_bottom

  def as_tuple(self) -> Tuple[int, int, int, int]:
    """
    Returns the bounds as tuple ordered as `(left, top, right, bottom)`.
    """
    return (self.left, self.top, self.right, self.bottom)

  def __eq__(self, other: object) -> bool:
    """
    Returns whether or not `this` instance of bounds is equal to an`other` instance of bounds.
    """
    if not isinstance(other, Bounds):
      return False

    return (self.left == other.left and
            self.top == other.top and
            self.right == other.right and
            self.bottom == other.bottom)

@dataclass
class PartialBounds(Bounds):
  left: Optional[int] = None
  top: Optional[int] = None
  right: Optional[int] = None
  bottom: Optional[int] = None
