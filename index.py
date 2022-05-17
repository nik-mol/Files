from pprint import pprint
import os

BASE_PATH = os.getcwd()
LOGS_NAME = 'recipes'
FILE_NAME = 'recipes.txt'

full_path = os.path.join(BASE_PATH, LOGS_NAME, FILE_NAME)

# print(full_path)

def recipes():
  with open(full_path, 'r',) as file_obj:
    cook_book = {}
    foot = file_obj.readline().strip()
    for line in file_obj:
      quantyti = int(line.strip())
      lines = []
      for items in range(quantyti):
        data = file_obj.readline().strip().split(' | ')
        lines.append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})
        
      cook_book[foot] = lines 
      file_obj.readline()
      foot = file_obj.readline().strip()
    # file_obj.write('5455555')
    pprint(cook_book, sort_dicts=False)
    

recipes()