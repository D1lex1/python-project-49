import prompt


def welcome_user():
    name = prompt.string(
        "Welcome to the Brain Games!\nCan I have your name? "
    )
    print(f'Hello, {name}')
