# from PIL import Image, ImageDraw
import pytesseract
# from lib.root import Root
# from models.bounds import Bounds
# from lib.question_number_parser import QuestionNumberParser
# from lib.tesseract_image_data_parser import TesseractImageDataParser
# from lib.recognized_words_within_bounds import RecognizedWordsWithinBounds
# from models.recognized_word import RecognizedWord
# from pydash import sort_by, find
# import ipdb

print(pytesseract.get_tesseract_version())

# def find_top_limit(image_data) -> int:
#   all_words: list[str] = image_data['text']
#   candidates = ['margem', 'enunciado', 'responda']

#   index = index_of_any_of_these_in_list(candidates, all_words)
#   y = image_data['top'][index]
#   height = image_data['height'][index]
#   return y + height


# # def find_image_data_within_limits(bounds: Bounds, image_data: any):

# #   pass

# # # def find_nearest_numbered_list_item_bounds(image_data) -> Bounds:
# # #   all_words: list[str] = image_data['text']
# # #   index = 1

# # #   pass

# def index_of_any_of_these_in_list(candidates: list[str], items: list[str]):
#   lowered_items = map(lambda i: i.lower(), items)
#   index = -1
#   for candidate in candidates:
#     try:
#       index = list(lowered_items).index(candidate)
#       break
#     except ValueError:
#       # TODO: do something
#       index = -1
#   return index

# # Convert PDF to Image
# # pdf_file_path = Root.assets('exams', '2005-1a Epoca.pdf')
# # paths = pdf2image.convert_from_path(pdf_file_path, output_folder=Root.out(), fmt='JPEG', paths_only=True, dpi=300)

# image_path = Root.out('42eb49f3-a609-42c0-af01-8f53a3cb7b33-1.jpg')

# with Image.open(image_path) as image:
#   image_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang='eng+por')

#   recognized_words: list[RecognizedWord] = TesseractImageDataParser(image_data).parse()

#   # Find the closest question number from the left edge of the paper
#   # - Sort the recognized words data by their "left" bound in ASC order first
#   sorted_recognized_words = sort_by(recognized_words, 'bounds.left')
#   # - Find it
#   question_number_recognized_word: RecognizedWord | None = find(sorted_recognized_words, lambda rw: QuestionNumberParser(rw.text).valid())

#   if question_number_recognized_word:
#     drawing = ImageDraw.Draw(image)

#     bounds: Bounds = question_number_recognized_word.bounds
#     threshold = 16
#     limit_bounds: Bounds = Bounds(bounds.left - threshold, 0, bounds.right + threshold, image.height)

#     drawing.rectangle(limit_bounds.as_tuple(), outline=(255, 0, 0), width=4)

#     q2 = find(recognized_words, lambda x: x.text == '2.')
#     q3 = find(recognized_words, lambda x: x.text == '3.')
#     q4 = find(recognized_words, lambda x: x.text == '4.')

#     recognized_words_within_bounds = RecognizedWordsWithinBounds(recognized_words, limit_bounds).get()
#     ipdb.set_trace()
#     for recognized_word in recognized_words_within_bounds:
#       drawing.rectangle(recognized_word.bounds.as_tuple(), outline=(0, 255, 0), width=4)
#     else:
#       print('Did not recognize any words within given bounds', bounds)

#     output_image_path = Root.out('ml.png')
#     image.save(output_image_path, bitmap_format='png')
#     print('Image saved at:', output_image_path)
#   else:
#     print('Did not find any question number!')
#

  # 1. Find the first y limit from top of the page
  # i = find_nearest_numbered_list_item_index(image_data)
  # point = Point(image_data['left'][i], image_data['top'][i])
  # size = Size(image_data['width'][i], image_data['height'][i])

  # drawing = ImageDraw.Draw(image)
  # bounds = (point.x, point.y, point.x + size.width, point.y + size.height)
  # drawing.rectangle(bounds, outline=(0, 255, 0), width=4)

  # image.save(Root.out('ml.png'), bitmap_format='png')

  # level_count = len(image_data['level'])
  # drawing = ImageDraw.Draw(image)

  # for i in range(level_count):
  #   (x, y, w, h) = (
  #     image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
  #   )

  #   drawing.rectangle((x, y, x + w, y + h), outline=(0, 255, 0), width=4)

  # # Show the final image
  # image.save(Root.out('ml.png'), bitmap_format='png')
