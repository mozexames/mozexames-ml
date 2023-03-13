from typing import List, cast
from pdf2image import pdf2image

from .root import Root

class PdfToImageConverter:
  def __init__(self, pdf_path) -> None:
    self.pdf_path = pdf_path

  def convert(self, save_at: str = Root.out()) -> List[str]:
    paths = pdf2image.convert_from_path(self.pdf_path,
                                        output_folder=save_at,
                                        fmt='PNG',
                                        paths_only=True,
                                        dpi=600)

    # We know for sure that the type will be a List[str] because we've set the `paths_only` argument as `True`
    # so its safe to cast the type in order to force to what is correct.
    return cast(List[str], paths)




