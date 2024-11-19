from ..services.count_words_service import GetNumberOfWords


def count_words_controller(full_text: str) -> int:
    try:
        number_words = GetNumberOfWords(text=full_text)
        return number_words.get_number_words()
    except Exception as exception:
        print("exception ", exception)
        return {"error": exception.message}