#Объявление переменных

words_easy = {"family" : "семья",
              "hand" : "рука",
              "people" : "люди",
              "evening" : "вечер",
              "minute" : "минута",
              }

words_medium = {"believe" : "верить",
              "feel" : "чувствовать",
              "make" : "делать",
              "open" : "открывать",
              "think" : "думать",
              }

words_hard = {"rural" : "деревенский",
              "fortune" : "удача",
              "exercise" : "упражнение",
              "suggest" : "предлагать",
              "except" : "кроме",
              }

levels = {0 : "Нулевой",
              1 : "Так себе",
              2 : "Можно лучше",
              3 : "Норм",
              4 : "Хорошо",
              5 : "Отлично",
              }


levels_of_hards = {"легкий" : words_easy,
          "средний" : words_medium,
          "сложный" : words_hard,
}

answers = {}
right_answers = 0

#Выбор сложности
hard = input("Выберите уровень сложности (легкий, средний, сложный):  ")

#Вопросы и ответы
work_dict = levels_of_hards[hard]
for key, value in work_dict.items():
    answer = input(f"{key}, {len(value)} букв, начинается на {value[0]}...Ответ:  ")
    if answer == value:
        print(f"Верно, {key} - это {value}.")
    else:
        print(f"Неверно. {key} - это {value}.")
    answers[key] = answer == value   #запись в словарь


#Выод статистики
print()  #принты для того, чтобы статистика начиналась с новых строк
print("Правильно отвечены слова: ")
for word, bool_value in answers.items():
    if bool_value is True:
        print(word)
        right_answers += 1

print()  #принты для того, чтобы статистика начиналась с новых строк
print("Неправильно отвечены слова: ")
for word, bool_value in answers.items():
    if bool_value is False:
        print(word)

#Подсчет ранга
print(f"Ваш ранг: \n {levels[right_answers]}")
