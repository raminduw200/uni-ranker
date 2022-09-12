from Subject import Subject


class Student:
    id: str = None
    # name: str = None
    total_gpv: int = None
    gpa: float = None
    subjects: [Subject] = None
    TOTAL_CREDIT: int = 34

    def __init__(self, id_):
        self.id = id_
        # self.name = name
        self.total_gpv = 0
        self.gpa = 0
        self.subjects = []

    def add_subject(self, code_, grade_):
        subj = Subject(code_, grade_)
        self.subjects.append(subj)
        self.total_gpv += subj.gpv
        self.gpa = self.total_gpv / self.TOTAL_CREDIT

    def get_subject(self, code_):
        for subject in self.subjects:
            if subject.code == code_:
                return subject
        return None

    def get_id(self):
        return self.id

    def get_total_gpv(self):
        return self.total_gpv

    def get_gpa(self):
        return self.gpa