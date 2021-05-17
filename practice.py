from discipline import Discipline


class Practice(Discipline):

    def __init__(self, name: str, semester: int, cathedra: str, practice_type: str, leader: str, themes: list):
        super().__init__(name, semester, cathedra)
        self.practice_type = practice_type
        self.leader = leader
        self.themes = themes

    def set_leader(self, leader: str):
        self.leader = leader

    def add_theme(self, theme: str):
        self.themes.append(theme)

    def del_theme(self, theme: str):
        try:
            self.themes.remove(theme)
        except ValueError:
            print('ValueError in `del_theme` for theme `' + theme + '`')

    def edit_theme(self, theme_old: str, theme_new: str):
        try:
            index = self.themes.index(theme_old)
            new_themes = list()

            for x in self.themes:
                if self.themes.index(x) == index:
                    new_themes.append(theme_new)
                else:
                    new_themes.append(x)

            self.themes = new_themes
        except ValueError:
            print('ValueError in `edit_theme` for theme `' + theme_old + '`')

    def __str__(self):
        return "name: " + self.name \
               + "\npractice_type: " + self.practice_type \
               + "\nsemester: " + str(self.semester) \
               + "\ncathedra: " + self.cathedra \
               + "\nleader: " + self.leader
