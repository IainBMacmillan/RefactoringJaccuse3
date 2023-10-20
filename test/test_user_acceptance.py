import sys
import filecmp
from unittest import mock
from source.jaccuse import jaccuse_game
from test.initial_test_data import test_data


"""
Need to prep GameClock.display_time_remaining to set test to True in order 
to give consistent output for file assertion
"""

scripts_folder: str = 'test/UAT_tests/test_scripts/'
results_folder: str = 'test/UAT_tests/actual/'
compare_folder: str = 'test/UAT_tests/expected/'


def routine_for_uat(file):
    sys.stdin = open(f'{scripts_folder}{file}', 'r')
    sys.stdout = open(f'{results_folder}{file}', 'w')
    jaccuse_game(test_data)
    sys.stdin.close()
    sys.stdout.close()

    assert filecmp.cmp(f'{results_folder}{file}',
                       f'{compare_folder}{file}',
                       shallow=False)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_1_quit_game(mock_write):
    # only one response
    file = 'user_test_1.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_2_liar_knows_zophie(mock_write):
    # very high likelihood of failing as liar selects answer from 8 options which are incorrect
    file = 'user_test_2.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_3_honest_knows_zophie(mock_write):
    # 50/50 chance of passing as random choice of place or item
    file = 'user_test_3.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_4_culprit_knows_zophie(mock_write):
    # only one answer, culprit won't give themself up
    file = 'user_test_4.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_5_suspect_accused_twice(mock_write):
    # only one response
    file = 'user_test_5.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_6_accuse_the_culprit(mock_write):
    # only one response
    file = 'user_test_6.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_7_accuse_3_suspects(mock_write):
    # only one response
    file = 'user_test_7.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_8_honest_asked_about_themself(mock_write):
    # only one response for test 8, 9, 10
    file = 'user_test_8.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_9_liar_asked_about_themself(mock_write):
    # only one response for test 8, 9, 10
    file = 'user_test_9.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_10_culprit_asked_about_themself(mock_write):
    # only one response for test 8, 9, 10
    file = 'user_test_10.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_11_honest_answers_about_clue(mock_write):
    # 50/50 chance of passing as random choice of place or item
    file = 'user_test_11.txt'
    routine_for_uat(file)


@mock.patch('source.jaccuse.GameClock.get_time_remaining', return_value='Time left for patch testing')
def test_12_liar_answers_about_clue(mock_write):
    # very high likelihood of failing as liar selects answer from 8 options which are incorrect
    file = 'user_test_12.txt'
    routine_for_uat(file)
