"""
This package is used to test the user
code that was provided in order to for
them to register on the website
"""
import re
import random
from datetime import datetime as dt

REGEX = r'Kurri\-2018\d+w\@user'



class CodeValidation(object):
  
  ERRORS = []
  
  def __init__(self, string):
    self._string = string
  
  def test_length(self):
    if self._string != 15:
      self._send_errors('Vous devez entrez un code de 15')
      return False
    else:
      return True
  
  def test_pattern(self):
    if re.search(REGEX, self._string) is not None:
      return True
    else:
      self._send_errors('Votre code n\'est pas valide')
      return False, self.ERRORS
      
  def test_against_list(self, user_code):
    with open('list_of_codes.txt','r', encode='utf_8') as f:
      codes = [code for code in f.readlines()]
    
    for code in codes:
      if code == user_code:
        return True
      else:
        self._send_errors('Votre code n\'est pas un code valide')
        return False, self.ERRORS
      
  @classmethod
  def _send_errors(cls, value):
    cls.ERRORS.append(value)


def generate_code():
  """
  Generate a user code for them to be
  able to register on the website
  """
  base_code = 'Kurri\-{year}\{numbers}w\@user'
  rand_number = random.randrange(100000, 999000)
  
  generated_code = base_code.format(year=dt.now(), numbers=rand_number)
  
  with open('list_of_codes.txt', 'a', encode='utf_8') as f:
    f.writelines(generated_code)
    f.writelines('\n')
    
  return generated_code
