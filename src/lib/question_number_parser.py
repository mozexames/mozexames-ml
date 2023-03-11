from ossaudiodev import SNDCTL_COPR_HALT
import re
from tkinter import OFF

class QuestionNumberParser:
  LETTER_NUMBER_SIMILARITY_MAP = {
    'o': 0,
    'd': 0,
    'i': 1,
    'l': 1,
    's': 5,
    'b': 8,
  }

  def __init__(self, text: str):
    self.text = text

  def parse(self) -> int | None:
    # A question number consists of two parts: a number followed by a comma.
    # E.g: "1.", "2.", etc..

    match = re.match(r'(?P<number>\d+|\w+)\.', self.text, re.IGNORECASE)
    if match:
      # Process the characters found to potentially be a number, as int, transforming any number-looking
      # letters (if any) to its number equivalent.
      potential_number_chars = match.group('number')
      return self._process_characters_as_int(potential_number_chars)
    else:
      # Text did not match a valid question number.
      return None

  def valid(self) -> bool:
    # Return whether or not this is a valid question number text
    return bool(self.parse())

  def _process_characters_as_int(self, potential_number_chars: str) -> int | None:
    """
    Handle common misclassifications for characters that are visually similar.

    :example:
    These characters looks the same in some fonts, E.g: Times New Roman

    - `l` and `l`
    - `I` and `I`
    - `S` and `S`
    - `O` and `O`
    - `Q` and `Q`
    - `D` and `D`
    - `B` and `B`
    """

    try:
      # Lower the potential number chars, so its easy to map the number-looking letter similaritise
      lowered_potential_number_chars = potential_number_chars.lower()

      auto_corrected_chars_list = list(
        map(lambda char: str(self.LETTER_NUMBER_SIMILARITY_MAP.get(char, char)), lowered_potential_number_chars)
      )

      auto_corrected_number_chars = ''.join(auto_corrected_chars_list)
      return int(auto_corrected_number_chars)
    except:
      # Failed to auto correct all chars as int, fallback to NaN
      return None

