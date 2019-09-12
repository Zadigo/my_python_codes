import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

QUESTIONS_DIR_PATH = os.path.join(BASE_PATH, 'questions')

MEMORY_PATH = [
    os.path.join(BASE_PATH, 'memory.json')
]
