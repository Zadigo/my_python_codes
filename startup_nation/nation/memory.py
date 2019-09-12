import json
import os
from startup_nation.nation.conf import QUESTIONS_DIR_PATH, MEMORY_PATH

class Memory:
    """A wrapper class that initializes in order to store
    the current files located in the questions directory.

    This class is a convinience class for better manipulating
    the objects located under that folder.
    """
    def __init__(self, *args):
        directory = list(os.walk(QUESTIONS_DIR_PATH))
        self.all_files = directory[0][2]

    @property
    def files_paths(self):
        files_paths = [
            os.path.join(QUESTIONS_DIR_PATH, filename) for filename in self.all_files
        ]
        return files_paths

    def file_exists(self, filename):
        """
        Checks whether a file exists or not in the
        questions directory.

        Parameters
        ----------

        The filename should just be a simple name
        without the extension.
        """
        if filename + '.json' in self.all_files:
            return True
        return False

def questions_asked(question):
    with open(MEMORY_PATH[0], 'r+', encoding='utf-8') as f:
        # We need to read the file
        # that serves as the application
        # memory
        json_object = json.load(f)
        
        # Get all the previous questions that were asked
        previous_questions = json_object['questions_asked']
        # Check the references against the current reference

        # Makes no sense to check if there
        # were no previous questions asked.
        # Just let the normal process happen by
        # appending a question to the list
        if len(previous_questions) == 0:
            pass
        else:
            for reference in previous_questions:
                if json_object['reference'] == reference:
                    # The question was already asked
                    # in which case we have to get
                    # another question
                    return False

        if isinstance(question, dict):
            # Get question's reference
            question_object = {
                'reference': question['reference']
            }

            # Send the appended question in the list
            # to the memory
            json_object['questions_asked'].append(question_object)
            # json.dump(json_object, f, indent=4)

    return question
