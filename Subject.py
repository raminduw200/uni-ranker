import pandas as pd

EXCEL_FILE = "gradings.xlsx"
SHEET_1 = "subject_info"
SHEET_2 = "grading_gpv"


class Subject:
    code: str = None
    name: str = None
    grade: str = None
    gpv: float = None
    credit: int = None
    # static
    subject_info: pd.DataFrame = None
    grading_gpv: pd.DataFrame = None

    def __init__(self, code_, grade_):
        self.code = code_
        self.name = get_sub_name(code_)
        self.grade = grade_
        self.credit = self.get_credit_value(code_)
        self.gpv = self.get_gpv(grade_) * self.credit
        if self.subject_info is None or self.grading_gpv is None:
            initialize_readings()

    @staticmethod
    def get_credit_value(code_):
        return int(Subject.subject_info[Subject.subject_info["Code"] == code_]["Credits"].values[0])

    @staticmethod
    def get_gpv(grade_):
        return float(Subject.grading_gpv[Subject.grading_gpv["Grade"] == grade_]["GPV"].values[0]) \
            if (grade_ != 'NC' or '#') else 'AB'

    def get_grade(self):
        return self.grade

    def __str__(self):
        return f"{self.code} : {self.name} : {self.grade}"


def get_sub_name(code_):
    return Subject.subject_info[Subject.subject_info["Code"] == code_]["Name"].values[0]


def initialize_readings():
    excel = pd.ExcelFile(EXCEL_FILE)
    Subject.subject_info = pd.read_excel(excel, SHEET_1)
    Subject.grading_gpv = pd.read_excel(excel, SHEET_2)
