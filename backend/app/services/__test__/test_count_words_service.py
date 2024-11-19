import pytest

from backend.app.services.count_words_service import GetNumberOfWords


@pytest.mark.parametrize("text, result",
                         [("Hello World", 2),
                          ("It`s test", 3),
                          ("You walk the edge of that abyss every night, "
                           "but you haven't fallen in, and I thank heavens for that", 21),
                          ("Word with pontuation......... ,,,,, ......", 3),
                          ("    Test space before sentence", 4),
                          ("Test with special characters @#!@", 4)
                          ])
def test_count_words(text, result):
    get_number_words = GetNumberOfWords(text=text)

    assert get_number_words.get_number_words() == result
