from academic import Academic
from plan import Plan, AcademicList
from practice import Practice

academics = AcademicList()
academics.append(Academic('Дисциплина 1', 1, 'Кафедра 1', 'Чернов Мирон Викторович', 'экзамен',
                          dict({'лекция': 4, 'практическая': 3, 'лабораторная': 2})))
academics.append(Academic('Дисциплина 2', 2, 'Кафедра 2', 'Жданов Филипп Филиппович', 'зачет',
                          dict({'лекция': 3, 'практическая': 2, 'лабораторная': 1})))
academics.append(Academic('Дисциплина 3', 3, 'Кафедра 3', 'Уваров Валентин Олегович', 'зачет',
                          dict({'лекция': 5, 'практическая': 2})))

# вывод данных
for x in academics:
    print(x.__str__() + '\n')

# проверка метода для изменения лектора
academics.__getitem__(1).set_lecturer('ИЗМЕНЕННЫЙ ЛЕКТОР')

# проверка метода для изменения формы контроля
academics.__getitem__(2).set_control_form('ИЗМЕНЕННАЯ ФОРМА')

# вывод данных
print('\n------\n')
for x in academics:
    print(x.__str__() + '\n')

practices = list()
practices.append(
    Practice('Тестовая практика 1', 1, 'Кафедра 1', 'учебная', 'важный чел 1', ['тема 1', 'тема 2']))
practices.append(
    Practice('Тестовая практика 2', 1, 'Кафедра 2', 'производственная', 'важный чел 2', ['тема 3', 'тема 4']))
practices.append(
    Practice('Тестовая практика 3', 1, 'Кафедра 3', 'преддипломнаяная', 'важный чел 3', ['тема 5', 'тема 6']))

# вывод данных
print('\n----------\n----------\n')
for x in practices:
    print(x.__str__() + '\n')

# проверка метода для изменения руководитель
practices.__getitem__(0).set_leader('ИЗМЕНЕННЫЙ РУКОВОДИТЕЛЬ')

# добавление новой темы (видно в output.txt)
practices.__getitem__(1).add_theme('НОВАЯ ТЕМА')

# удаление существующей темы (видно в output.txt)
practices.__getitem__(1).del_theme('тема 3')

# изменение существующей темы (видно в output.txt)
practices.__getitem__(2).edit_theme('тема 5', 'ИЗМЕНЕННАЯ ТЕМА')

# вывод данных
print('\n------\n')
for x in practices:
    print(x.__str__() + '\n')

plan = Plan('#001', 'Тестовое', 'Тестовая кафедра', academics, practices)
plan.to_file()

# вызов исключения #1 (ValueError)
practices.__getitem__(1).del_theme('тема 123')

# вызов исключения #2 (ValueError)
practices.__getitem__(2).edit_theme('тема 5231', 'ИЗМЕНЕННАЯ ТЕМА')
