import re

class QuestionNumberParser:
  def __init__(self, text: str):
    self.text = text

  def parse(self) -> int | None:
    # A question number consists of two characters: a number followed by a comma.
    # E.g: "1.", "2.", etc..
    matched_items = re.match('^\d+\.', self.text)
    if matched_items:
      # Return the first character which is the number part as an int.
      matched_item = matched_items[0]
      return int(matched_item[0])
    else:
      # Text did not match a valid question number.
      return None

  def valid(self) -> bool:
    # Return whether or not this is a valid question number text
    return bool(self.parse())
