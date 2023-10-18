from source.jaccuse_original_test import jaccuse_game
import sys
import filecmp

"""
Need to prep GameClock.display_time_remaining to set test to True in order 
to give consistent output for file assertion
"""

scripts_folder: str = 'test/UAT_tests/test_scripts/'
results_folder: str = 'test/UAT_tests/UAT_results/'
compare_folder: str = 'test/UAT_tests/UAT_expected_results/'


def routine_for_uat(file):
    sys.stdin = open(f'{scripts_folder}{file}', 'r')
    sys.stdout = open(f'{results_folder}{file}', 'w')
    jaccuse_game()

    sys.stdin.close()
    sys.stdout.close()

    assert filecmp.cmp(f'{results_folder}{file}',
                       f'{compare_folder}{file}',
                       shallow=False)


def test_1_quit_game():
    # only one response
    file = 'user_test_1.txt'
    routine_for_uat(file)


def test_2_liar_knows_zophie():
    # very high likelihood of failing as liar selects answer from 8 options which are incorrect
    file = 'user_test_2.txt'
    routine_for_uat(file)


def test_3_honest_knows_zophie():
    # 50/50 chance of passing as random choice of place or item
    file = 'user_test_3.txt'
    routine_for_uat(file)


def test_4_culprit_knows_zophie():
    # only one answer, culprit won't give themself up
    file = 'user_test_4.txt'
    routine_for_uat(file)


def test_5_suspect_accused_twice():
    # only one response
    file = 'user_test_5.txt'
    routine_for_uat(file)


def test_6_accuse_the_culprit():
    # only one response
    file = 'user_test_6.txt'
    routine_for_uat(file)


def test_7_accuse_3_suspects():
    # only one response
    file = 'user_test_7.txt'
    routine_for_uat(file)


def test_8_honest_asked_about_themself():
    # only one response for test 8, 9, 10
    file = 'user_test_8.txt'
    routine_for_uat(file)


def test_9_liar_asked_about_themself():
    # only one response for test 8, 9, 10
    file = 'user_test_9.txt'
    routine_for_uat(file)


def test_10_culprit_asked_about_themself():
    # only one response for test 8, 9, 10
    file = 'user_test_10.txt'
    routine_for_uat(file)


def test_11_honest_answers_about_clue():
    # 50/50 chance of passing as random choice of place or item
    file = 'user_test_11.txt'
    routine_for_uat(file)


def test_12_liar_answers_about_clue():
    # very high likelihood of failing as liar selects answer from 8 options which are incorrect
    file = 'user_test_12.txt'
    routine_for_uat(file)
