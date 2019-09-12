import os
import secrets
import json
from startup_nation.nation.conf import QUESTIONS_DIR_PATH

class Questions:
    """A class that shows all the questions that are
    available for the application.

    Description
    -----------

    The purpose of the this class is to allow you to get
    all the questions to create something else out of them.

    This class is just for convenience in manipulating the questions.


    Result
    ------

        [
            {
                id: 1,
                reference: 9f8f32600d9e,
                subject: subject
                question: Ask a question ?
                answers: [
                    {
                        id: 1,
                        answer: An answer
                    }
                ],
                tag: tag
            },
            ...
        ]
    """
    def __init__(self):
        directory = list(os.walk(QUESTIONS_DIR_PATH))
        self.all_files = directory[0][2]

        questions = []

        for f in self.all_files:
            full_path = os.path.join(QUESTIONS_DIR_PATH, f)
            file_object = open(full_path, 'r', encoding='utf-8')
            json_object = json.load(file_object)

            questions.append([json_object])

            file_object.close()

        self.questions = questions

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return str(self.questions)

    def __getitem__(self, index):
        return self.questions[index]

    # @staticmethod
    # def question_references(self, index):
    #     """Get the references for all the questions available for
    #     the application
    #     """
    #     references = [question['reference'] for question in self.questions]
    #     return references

def questions_file_generator(filename, subject, tag, answers=[]):
    path = 'C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\startup_nation\\questions.txt'
    generated_file_path = 'C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\startup_nation\\questions'

    generated_file = os.path.join(generated_file_path, filename + '.json')

    questions_wrapper = {
        "questions": []
    }

    with open(path, 'r', encoding='utf-8') as f:
        list_of_questions = f.readlines()

        for i in range(7, 12):
            question_wrapper = {
                "id": i,
                "reference": secrets.token_hex(6),
                "subject": subject,
                "question": list_of_questions[i],
                "answers": [],
                "tag": tag
            }
            questions_wrapper['questions'].append(question_wrapper)
        
        with open(generated_file, 'w', encoding='utf-8') as f:
            json.dump(questions_wrapper, f, indent=4)
