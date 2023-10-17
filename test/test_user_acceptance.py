from source.jaccuse_original_test import jaccuse_game
import sys
import filecmp

scripts_folder: str = 'UAT_tests/test_scripts/'
results_folder: str = 'UAT_tests/UAT_results/'
compare_folder: str = 'UAT_tests/UAT_expected_results/'

"""
if running pytest from terminal get a FileNotFoundError: [Errno 2] No such file or 
directory: '\\prep_data\\results\\detective_notes_results_3.txt'
hence adding test\\ to folder locations below. 
if running from Pycharm, remove test\\ from folder locations below.
"""

prefix_folder: str = 'test/'

is_run_from_terminal: bool = False

if is_run_from_terminal:
    scripts_folder = f'{prefix_folder}{scripts_folder}'
    results_folder = f'{prefix_folder}{results_folder}'
    compare_folder = f'{prefix_folder}{compare_folder}'


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
    file = 'user_test_1.txt'
    routine_for_uat(file)


def test_2_liar_knows_zophie():
    file = 'user_test_2.txt'
    routine_for_uat(file)


def test_3_honest_knows_zophie():
    file = 'user_test_3.txt'
    routine_for_uat(file)


def test_4_culprit_knows_zophie():
    file = 'user_test_4.txt'
    routine_for_uat(file)


def test_5_suspect_accused_twice():
    file = 'user_test_5.txt'
    routine_for_uat(file)


def test_6_accuse_the_culprit():
    file = 'user_test_6.txt'
    routine_for_uat(file)


def test_7_accuse_3_suspects():
    file = 'user_test_7.txt'
    routine_for_uat(file)


def test_8_honest_asked_about_themself():
    file = 'user_test_8.txt'
    routine_for_uat(file)


def test_9_liar_asked_about_themself():
    file = 'user_test_9.txt'
    routine_for_uat(file)


def test_10_culprit_asked_about_themself():
    file = 'user_test_10.txt'
    routine_for_uat(file)


def test_11_honest_answers_about_clue():
    file = 'user_test_11.txt'
    routine_for_uat(file)


def test_12_liar_answers_about_clue():
    file = 'user_test_12.txt'
    routine_for_uat(file)
