from name_function import get_formatted_name


def test_first_last_name():
    """能否正确处理像Janis Joplin这样的姓名？"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


def test_first_last_middle_name():
    """能够处理中间名吗？"""

    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus'
    )
    assert formatted_name == 'Wolfgang Amadeus Mozart'
