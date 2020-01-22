import PyPDF2
from PyPDF2 import PdfFileWriter

def decrypt_pdf(path, page=0, password=None):
    """A simple program that takes a PDF file
    in order to return the text
    """
    with open(path, 'rb', encoding='utf-8') as f:
        source_file = PyPDF2.PdfFileReader(f)
        # The file might require a password.
        # In which case we need to provide one
        # for us to be able to read it
        is_encrypted = source_file.isEncrypted
        if is_encrypted:
            if password is not None:
                source_file.decrypt(password)
            else:
                raise TypeError('The file you provided is encrypted with '\
                        'a password. Received {password}'.format(password=password))
        page = source_file.getPage(0)
    return page or None

def copy_pages(file_names:list, new_file_name, passwords:list=None):
    """A function that takes PDF files and copies the pages into a new document"""
    with open(new_file_name, 'wb', encoding='utf-8') as new_file:
        raw_files = (open(file_name, 'rb', encoding='utf-8') for file_name in file_names if file_name.endswith('pdf'))
        source_files = (PyPDF2.PdfFileReader(raw_file) for raw_file in raw_files if raw_file)

        writer = PdfFileWriter()

        def set_pages(source_file, number_of_pages):
            """Sets the pages to copy in the new document"""
            for i in range(0, number_of_pages):
                page = source_file.getPage(i)
                writer.addPage(page)

        for source_file in source_files:
            set_pages(source_file, source_file.numPages)
            source_file.close()
        
        writer.write(new_file)
