import re
from ..errors.empty_text_error import EmptyTextError


class GetNumberOfWords:
    def __init__(self, text: str):
        self.text = text

    def _text_to_list(self):
        return re.split(r"[ '`]", self.text)

    def get_number_words(self):
        try:
            if not self.text or len(self.text) == 0:
                raise EmptyTextError()

            return len(self._text_to_list())
        except Exception as exception:
            raise exception

