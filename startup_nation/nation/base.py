import json
import os
from random import choice

from startup_nation.nation.caches import questions_cache
from startup_nation.nation.memory import questions_asked, Memory
from startup_nation.nation.conf import QUESTIONS_DIR_PATH

memory = Memory()

def questionner(filename=None):
    """It is the base definition used to retrieve a question
    in a random manner from the questions files.

    Result
    ------

        {
            "id": 7,
            "reference": "9f8f32600d9e",
            "subject": "...",
            "question": "...",
            "answers": [],
            "tag": "..."
        }

        It returns a dictionnary that can be used in other
        to ask a question to the user via an API call or
        simply through your Django or Flask applicaiton
        for example.
    """
    # if not memory.file_exists(filename):
    #     pass

    # For testing purposes
    path = os.path.join(QUESTIONS_DIR_PATH, 'questions.json')

    with open(path, 'r', encoding='utf-8') as f:
        json_object = json.load(f)
        # Create a copy of the quesions contained
        # in the JSON file so that we don't depend
        # on the original file anymore
        questions = json_object['questions'].copy()

    @questions_cache
    def list_of_questions():
        return questions

    # Get the cached questions
    cached_questions = list_of_questions()

    # Get the number of questions
    number_of_questions = len(cached_questions)

    if number_of_questions == 0:
        pass

    def randomizer():
        """A small function that gets a random
        question within the list of questions

        Result
        ------

            {
                id: 1
            }
        """
        return cached_questions[
            choice(range(0, number_of_questions))
        ]

    # Get a random number
    question = cached_questions[
        choice(range(0, number_of_questions))
    ]

    # Check if the question was already
    # asked and return it as is -; this is a cache/json file
    # that dynamically stores a question that was asked
    verified_question = questions_asked(question)
    if not verified_question:
        # Generate a new question
        question = randomizer()

    # return verified_question
    return question

def questionner_input():
    answer = input(f"Question: {questionner()['question']} \n")
