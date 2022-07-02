class Subject:
    code: str = None
    name: str = None
    grade: str = None

    def __init__(self, code_, grade_):
        self.code = code_
        self.grade = grade_
        self.__set_name__(code_)

    def __set_name__(self, code_):
        if code_ == "SCS 1201":
            self.name = "Data Structures and Algorithms I"
        elif code_ == "SCS 1202":
            self.name = "Programming Using C"
        elif code_ == "SCS 1203":
            self.name = "Database I"
        elif code_ == "SCS 1204":
            self.name = "Discrete Mathematics I"
        elif code_ == "SCS 1205":
            self.name = "Computer Systems"
        elif code_ == "SCS 1206":
            self.name = "Laboratory I"
        elif code_ == "SCS 1207":
            self.name = "Software Engineering I"
        elif code_ == "SCS 1208":
            self.name = "Data Structures and Algorithms II"
        elif code_ == "SCS 1209":
            self.name = "Object Oriented Programming"
        elif code_ == "SCS 1210":
            self.name = "Software Engineering II"
        elif code_ == "SCS 1211":
            self.name = "Mathematical Methods I"
        elif code_ == "SCS 1212":
            self.name = "Foundation of Computer Science"
        elif code_ == "SCS 1213":
            self.name = "Probability and Statistics"
        elif code_ == "SCS 1214":
            self.name = "Operating Systems I"
