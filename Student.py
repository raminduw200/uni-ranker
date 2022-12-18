from Subject import Subject


class Student:
    id: str = None
    # name: str = None
    total_gpv: int = None
    gpa: float = None
    subjects: [Subject] = None
    total_credit: int = 0

    def __init__(self, id_):
        self.id = id_
        # self.name = name
        self.total_gpv = 0
        self.gpa = 0
        self.subjects = []

    def add_subject(self, code_, grade_):
        if not self.__subject_exists(code_):  # if subject not exits
            subj = Subject(code_, grade_)
            self.subjects.append(subj)
            self.total_credit += subj.credit
            self.total_gpv += subj.gpv
            self.gpa = self.total_gpv / self.total_credit
        else:
            grades = Subject.get_grades_as_list()
            if grades.index(grade_) < grades.index(self.get_subject(code_).get_grade()):
                self.total_gpv -= self.get_subject(code_).gpv
                self.get_subject(code_).update_grade(grade_)
                self.total_gpv += self.get_subject(code_).gpv
                self.gpa = self.total_gpv / self.total_credit

    def __get_subject_index(self, code_):
        for i in range(len(self.subjects)):
            if self.subjects[i].code == code_:
                return i
        return -1

    def get_subject(self, code_):
        return self.subjects[self.__get_subject_index(code_)] if self.__get_subject_index(code_) >= 0 else None

    def __subject_exists(self, code_):
        return self.__get_subject_index(code_) >= 0

    def get_id(self):
        return self.id

    def get_total_gpv(self):
        return self.total_gpv

    def get_gpa(self):
        return self.gpa

    def __str__(self):
        return f"{self.id} : {self.total_gpv} : {self.gpa}"
