"""
Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user(answers_dict):
    n = 0
#    question = input('Пользователь: ')
    while True:
        question = input('Пользователь: ')
        for key, value in answers_dict.items():
            if key == question:
                print(f'Программа: {value}')
                n += 1
                break
#            else:
#                print(f'Программа: Не понимаю вашего вашего вопроса')

        if n == len(answers_dict):
            break
        else:
            continue

if __name__ == "__main__":
    ask_user(questions_and_answers)