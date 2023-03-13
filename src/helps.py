from PIL import Image, ImageDraw
import pytesseract
from lib.root import Root
from models.recognized_word import RecognizedWord
from lib.tesseract_image_data_parser import TesseractImageDataParser
from lib.question_numbers_finder import QuestionNumbersFinder


def do_stuff():
  image_path = Root.join('src', 'static', 'images', 'sample.jpg')
  with Image.open(image_path) as image:
    image_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang="por", config="--dpi 600")
    recognized_words: list[RecognizedWord] = TesseractImageDataParser(image_data).parse()
    drawing = ImageDraw.Draw(image)

    # Debug draw
    for rw in recognized_words:
      drawing.rectangle(rw.bounds.as_tuple(), outline=(255, 0, 0), width=4)

    finder = QuestionNumbersFinder(recognized_words, image.height)
    question_numbers = finder.find()

    print(f"Detected {len(question_numbers)} question numbers.")

    drawing.rectangle(finder.column_limits().as_tuple(), outline=(0, 255, 0), width=4)

    for question_number in question_numbers:
      print(question_number.text)
      drawing.rectangle(question_number.bounds.as_tuple(), outline=(0, 0, 255), width=4)

    # Save the drawing
    output_image_path = Root.join('src', 'static', 'images', 'out', 'ml.png')
    image.save(output_image_path, bitmap_format='png')
    print('Image saved at:', output_image_path)
