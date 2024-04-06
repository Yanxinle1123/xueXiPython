import pytest

from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """一项可供所有测试功能使用的调查"""

    question = "您首先学会说什么语言？"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """测试单个响应是否已正确存储"""

    language_survey.store_response('英语')
    assert '英语' in language_survey.responses


def test_store_three_responses(language_survey):
    """测试三个单独的响应是否已正确存储"""

    responses = ['英语', '西班牙语', '汉语']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
