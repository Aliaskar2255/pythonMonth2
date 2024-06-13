# logic.py

import random
import configparser

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config['Game']

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_game():
    config = load_config('settings.ini')
    min_value = int(config['MinValue'])
    max_value = int(config['MaxValue'])
    attempts = int(config['Attempts'])
    starting_balance = int(config['StartingBalance'])
    current_balance = starting_balance

    secret_number = generate_random_number(min_value, max_value)

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас на счету: {current_balance}")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка {attempt}/{attempts}. Введите вашу ставку и число от {min_value} до {max_value}: "))
        if min_value <= guess <= max_value:
            if guess == secret_number:
                current_balance *= 2
                print(f"Поздравляем! Вы угадали число! Ваш баланс удвоен. Теперь у вас {current_balance}.")
                break
            else:
                current_balance -= guess
                print(f"К сожалению, вы не угадали. Ваш баланс: {current_balance}.")
        else:
            print("Неверный ввод. Пожалуйста, введите число в заданном диапазоне.")

    else:
        print(f"К сожалению, вы не угадали число. Загаданное число было: {secret_number}.")
