import ascii_magic
import yaml
import random
import time

with open("./questions.yml", "r") as stream:
    questions = yaml.safe_load(stream)

random.shuffle(questions)
score = 0

for question in questions:
    # Show question
    if "Image" in question:
        output = ascii_magic.from_image_file(question["Image"], columns=40)
        print(output)
    print(question["Question"])
    answers = question["Answers"]
    correct_answer = question["Correct"]
    random.shuffle(answers)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    
    player_answer = int(input())


    if answers[player_answer-1] == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. Correct answer is: {correct_answer}")
        questions.append(question)
    time.sleep(1)
    print()