import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_question_with_custom_max_selections():
    question = Question(title='q1', max_selections=2)

    assert question.max_selections == 2

def test_create_choice_with_correct_answer():
    question = Question(title='q1')

    choice = question.add_choice('a', True)

    assert choice.is_correct

def test_create_choice_with_empty_text():
    question = Question(title='q1')

    with pytest.raises(Exception):
        question.add_choice('')

def test_create_choice_with_text_longer_than_100_characters():
    question = Question(title='q1')

    with pytest.raises(Exception):
        question.add_choice('a' * 101)

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)

def test_add_choices_with_sequential_ids():
    question = Question(title='q1')

    first_choice = question.add_choice('a')
    second_choice = question.add_choice('b')

    assert first_choice.id == 1
    assert second_choice.id == 2

def test_remove_choice_by_id():
    question = Question(title='q1')
    choice = question.add_choice('a')

    question.remove_choice_by_id(choice.id)

    assert question.choices == []

def test_remove_choice_with_invalid_id():
    question = Question(title='q1')

    with pytest.raises(Exception):
        question.remove_choice_by_id(1)

def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a')
    question.add_choice('b')

    question.remove_all_choices()

    assert question.choices == []

def test_correct_selected_choices():
    question = Question(title='q1', max_selections=2)
    correct_choice = question.add_choice('a', True)
    incorrect_choice = question.add_choice('b')

    selected_correct_choices = question.correct_selected_choices(
        [correct_choice.id, incorrect_choice.id]
    )

    assert selected_correct_choices == [correct_choice.id]