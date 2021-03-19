#####################
# import modules
#####################
import os.path

#####################
# Define functions
#####################


def add_score(difficulty):
    my_file = "/home/guy/Desktop/WorldOfGames/Scores.txt"

    if not os.path.exists(my_file):  # if file exists
        os.system("touch /home/guy/Desktop/WorldOfGames/Scores.txt")

    if os.path.getsize("/home/guy/Desktop/WorldOfGames/Scores.txt") == 0:  # if file is empty
        os.system("echo 0 >> /home/guy/Desktop/WorldOfGames/Scores.txt")

    points_of_winning = int((difficulty * 3) + 5)
    file = open('Scores.txt', 'r')
    last_score = file.read()
    new_score = int(last_score) + int(points_of_winning)
    file = open('Scores.txt', 'w')
    file.write(str(new_score))
    print("current score: ")
    file = open('Scores.txt', 'r')
    print(file.read())
