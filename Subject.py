class Subject:
    code: str = None
    name: str = None
    grade: str = None
    gpv: int = None

    def __init__(self, code_, grade_):
        self.code = code_
        self.name = get_sub_name(code_)
        self.grade = grade_
        self.gpv = self.get_gpv(grade_) * self.get_credit_value(code_)

    @staticmethod
    def get_credit_value(code_):
        if code_ == "SCS 1201":
            return 3
        elif code_ == "SCS 1202":
            return 3
        elif code_ == "SCS 1203":
            return 3
        elif code_ == "SCS 1204":
            return 2
        elif code_ == "SCS 1205":
            return 2
        elif code_ == "SCS 1206":
            return 2
        elif code_ == "SCS 1207":
            return 2
        elif code_ == "SCS 1208":
            return 3
        elif code_ == "SCS 1209":
            return 3
        elif code_ == "SCS 1210":
            return 2
        elif code_ == "SCS 1211":
            return 2
        elif code_ == "SCS 1212":
            return 2
        elif code_ == "SCS 1213":
            return 2
        elif code_ == "SCS 1214":
            return 3

    @staticmethod
    def get_gpv(grade_):
        if grade_ == "A+":
            return 4
        elif grade_ == "A":
            return 4
        elif grade_ == "A-":
            return 3.7
        elif grade_ == "B+":
            return 3.3
        elif grade_ == "B":
            return 3.0
        elif grade_ == "B-":
            return 2.7
        elif grade_ == "C+":
            return 2.3
        elif grade_ == "C":
            return 2.0
        elif grade_ == "C-":
            return 1.7
        elif grade_ == "D+":
            return 1.3
        elif grade_ == "D":
            return 1.0
        elif grade_ == "E":
            return 0.0
        elif grade_ == "F":
            return 0.0

    def get_grade(self):
        return self.grade

    def __str__(self):
        return f"{self.code} : {self.name} : {self.grade}"


def get_sub_name(code_):
    if code_ == "SCS 1201":
        return "Data Structures and Algorithms I"
    elif code_ == "SCS 1202":
        return "Programming Using C"
    elif code_ == "SCS 1203":
        return "Database I"
    elif code_ == "SCS 1204":
        return "Discrete Mathematics I"
    elif code_ == "SCS 1205":
        return "Computer Systems"
    elif code_ == "SCS 1206":
        return "Laboratory I"
    elif code_ == "SCS 1207":
        return "Software Engineering I"
    elif code_ == "SCS 1208":
        return "Data Structures and Algorithms II"
    elif code_ == "SCS 1209":
        return "Object Oriented Programming"
    elif code_ == "SCS 1210":
        return "Software Engineering II"
    elif code_ == "SCS 1211":
        return "Mathematical Methods I"
    elif code_ == "SCS 1212":
        return "Foundation of Computer Science"
    elif code_ == "SCS 1213":
        return "Probability and Statistics"
    elif code_ == "SCS 1214":
        return "Operating Systems I"
