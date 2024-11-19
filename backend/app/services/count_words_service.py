import re
from ..errors.empty_text_error import EmptyTextError


class GetNumberOfWords:
    """
        A class to process text, clean special characters, and calculate the number of words.

        Attributes:
            text (str): The input text to be processed.
    """
    def __init__(self, text: str):
        self.text = text

    def _text_to_list(self):
        """
            Converts the current text into a list of words by splitting it using delimiters
                such as spaces (` `), backticks (`` ` ``), or single quotes (`'`).

            Returns:
                list[str]: A list of words extracted from the text.
        """
        return re.split(r"[ '`]", self.text)

    def _clean_text(self):
        """
            Cleans the text by:
            - Removing punctuation characters like `.,!@?#$%&`.
            - Trimming leading and trailing whitespace.

            Effects:
                Updates the instance variable `self.text` with the cleaned text.
        """
        self.text = self.text.translate(str.maketrans('', '', '.,!@?#$%&')).strip()

    def get_number_words(self):
        """
            Calculates the number of words in the text after cleaning it.

            Returns:
                int: The number of words in the text.

            Raises:
                EmptyTextError: If the text is empty or only contains whitespace.
                Exception: If an unexpected error occurs during processing.
        """
        try:
            if not self.text or len(self.text) == 0:
                raise EmptyTextError()

            self._clean_text()
            return len(self._text_to_list())
        except Exception as exception:
            raise exception

