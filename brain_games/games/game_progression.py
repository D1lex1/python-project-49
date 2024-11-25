import random


START_QUESTION = 'What number is missing in the progression?'


def progression():
    progression_step = random.randint(1, 5)
    progression_lenght = random.randint(5, 10)
    progression_list = []
    progression_start = random.randint(0, 25)
    while progression_lenght != 0:
        progression_list.append(progression_start)
        progression_start += progression_step
        progression_lenght -= 1
    progression_str = ' '.join([str(num) for num in progression_list])
    return progression_list, progression_str


def game_output():
    progression_list, progression_str = progression()
    correct_answer = progression_list[
        random.randint(0, len(progression_list) - 1)
    ]
    question = progression_str.replace(str(correct_answer), '..', 1)
    return str(correct_answer), question
