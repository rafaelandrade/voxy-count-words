

class EmptyTextError(Exception):
    """Base class for handle empty text"""

    def __init__(self):
        self.message = "Text input is required!"
        super().__init__(self.message)
