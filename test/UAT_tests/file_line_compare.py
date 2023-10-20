import difflib
import os
import filecmp

'''
Run the test_user_acceptance.py with pytest and run this to see the differences. 
Although the test_data is ordered at initial data setup, the random choices within 
the game will mix up the outputs.  

So as an examples
user_test_11.txt
-> They give you this clue: "5 DOLLAR GIFT CARD"
+> They give you this clue: "ALBINO ALLIGATOR PIT"

user_test_12.txt
-> They give you this clue: "VIDEO GAME MUSEUM"
+> They give you this clue: "ANIME VHS TAPE"

above two files work correctly, and needs manual intervention to check results.
Sometimes the outputs will match themselves, depending on runtime 1/9 success.
'''


def line_compare():
    path_a = 'test/UAT_tests/actual/'
    path_e = 'test/UAT_tests/expected/'
    list_test_files = list_of_files()

    for file in sorted(list_test_files):

        with open(f'{path_a}{file}') as file_1:
            file_1_text = file_1.readlines()

        with open(f'{path_e}{file}') as file_2:
            file_2_text = file_2.readlines()

        # Find and print the diff:
        print(file)
        for line in difflib.unified_diff(
                file_1_text, file_2_text, fromfile='file1.txt',
                tofile='file2.txt', lineterm=''):
            if line[:2] in ['->', '+>', '?']:
                print(line)


def list_of_files() -> list[str]:
    path = 'test/UAT_tests/actual/'
    full_results_list = os.listdir(path)
    path_a = 'test/UAT_tests/actual/'
    path_e = 'test/UAT_tests/expected/'
    match, mismatch, error = filecmp.cmpfiles(path_a, path_e, full_results_list, shallow=False)
    return mismatch


def main():
    line_compare()


if __name__ == '__main__':
    main()
