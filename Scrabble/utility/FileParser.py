import csv
import os


class FileParser:

    def __init__(self):
        self._word_container = []

    @classmethod
    def _format_word(self, word):
        """
        Description
        -----------
        Private class method to format input `word` string by
        removing all new-line and dash characters. All words
        are also converted to lower-case.
        """
        return str(word).replace('\n', '').replace('-', '').lower()

    @classmethod
    def _empty_file_check(self, file_path):
        return os.path.getsize(file_path) > 0

    def readf(self, file_path):
        """
        Description
        -----------
        Public class method to read in input text file and return
        a list of string elements. Function returns Python
        list `_word_container`.
        """
        if self._empty_file_check(file_path):
            with open(file=file_path, mode='r') as text_file:
                for word in text_file:
                    self._word_container.append(self._format_word(word))
        else:
            raise IOError
        return self._word_container
