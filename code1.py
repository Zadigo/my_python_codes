"""
This package is used to test the user
code that was provided in order to for
them to register on the website
"""

import re
import random
from datetime import datetime as dt

REGEX = r'Kurri\-20([0-9]{2})\d+w\@user'

def generate_code():
  """
  Generate a user code for them to be
  able to register on the website
  """
  base_code = 'Kurri\-{year}\{numbers}w\@user'
  rand_number = random.randrange(100000, 999000)
  
  generated_code = base_code.format(year=dt.now().year, numbers=rand_number)
  
  # with open('list_of_codes.txt', 'a', encode='utf_8') as f:
  #   f.writelines(generated_code)
  #   f.writelines('\n')
    
  return generated_code

print(generate_code())
