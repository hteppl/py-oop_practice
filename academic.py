from discipline import Discipline


class Academic(Discipline):

    def __init__(self, name: str, semester: int, cathedra: str, lecturer: str, control_form: str, hours: dict):
        super().__init__(name, semester, cathedra)
        self.lecturer = lecturer
        self.control_form = control_form
        self.hours = hours

    def set_lecturer(self, lecturer: str):
        self.lecturer = lecturer

    def set_control_form(self, control_form: str):
        self.control_form = control_form

    def get_hours(self):
        result = ''

        for key, value in self.hours.items():
            result += ('\n - ' + key + ': ' + str(value))

        return result

    def __str__(self):
        return "name: " + self.name \
               + "\nsemester: " + str(self.semester) \
               + "\ncathedra: " + self.cathedra \
               + "\nlecturer: " + self.lecturer \
               + "\ncontrol_form: " + self.control_form
