class AcademicList(list):

    def __init__(self):
        super().__init__()

    def __sizeof__(self):
        return len(self)


class Plan:

    def __init__(self, dir_code, dir_name, cathedra, academics: AcademicList, practices):
        self.dir_code = dir_code
        self.dir_name = dir_name
        self.cathedra = cathedra
        self.academics = academics
        self.practices = practices

    def to_file(self):
        output = list()
        output.append('Код направления: ' + self.dir_code)
        output.append('\nНазвание направления: ' + self.dir_name)
        output.append('\nКафедра: ' + self.cathedra)
        output.append(f'\n\n\n— Список занятий ({len(self.academics)} шт.): ')

        for x in self.academics:
            output.append('\n\n− Занятие `' + x.name + '`')
            output.append('\n Лектор: ' + x.lecturer)
            output.append('\n Семестр: ' + str(x.semester))
            output.append('\n Кафедра: ' + x.cathedra)
            output.append('\n Форма контроля: ' + x.control_form)
            output.append('\n Часы: ' + x.get_hours())

        output.append('\n\n\n---------------------------------')
        output.append(f'\n\n— Список практик ({len(self.practices)} шт.): ')

        for x in self.practices:
            output.append('\n\n− Практика `' + x.name + '`')
            output.append('\n Руководитель: ' + x.leader)
            output.append('\n Вид: ' + x.practice_type)
            output.append('\n Семестр: ' + str(x.semester))
            output.append('\n Кафедра: ' + x.cathedra)

            themes = ''
            for y in x.themes:
                themes += '\n - ' + y

            output.append('\n Темы: ' + themes)

        file = open('output.txt', 'w', encoding='utf-8')
        file.writelines(output)
        file.close()
