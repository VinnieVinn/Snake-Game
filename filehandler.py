import os
directory = os.path.dirname(os.path.realpath(__file__))
highscore_directory = directory + "\\highscore.txt"
highscore_file = open(highscore_directory, "a")
highscore_list = open(highscore_directory).read().lower().splitlines()

def add_score(score):
    highscore_file.write(f"\n{score}")
    highscore_list.append(str(score))

def get_best():
    highscore_list.sort(key=lambda score : int(score))
    return highscore_list[-1]

def close_file():
    highscore_file.close()