from Subject import Subject


class Student:
    id: str = None
    # name: str = None
    subjects: [Subject] = None

    def __init__(self, id_):
        self.id = id_
        # self.name = name
        self.subjects = []

    def add_subject(self, code_, grade_):
        self.subjects.append(Subject(code_, grade_))

    def get_subject(self, code_):
        for subject in self.subjects:
            if subject.code == code_:
                return subject
        return None

    def get_id(self):
        return self.id

