import os, re

def get_local_files(directory):
    LOCAL_FILES = list(os.walk(os.path.dirname(__file__)))[0][-1]
    PATTERNS = [
        r'(setup\.(json|txt|py))',
    ]

    for LOCAL_FILE in LOCAL_FILES:
        var = re.search(PATTERNS[0], LOCAL_FILE)
        if var:
            setup_path=os.path.join(directory,var.group(0))


# get_local_files(os.path.dirname(__file__))