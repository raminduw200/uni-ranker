import pandas as pd
from pathlib import Path

from Student import Student

STUDENTS = []
SHEETS_DIR = "Sheets/"


def stu_exits(id_):
    for i in range(len(STUDENTS)):
        if STUDENTS[i].id == id_:
            return i
    return -1


sheet_list = Path(SHEETS_DIR).rglob('*.csv')
for sheet in sheet_list:
    sheet = str(sheet)

    df = pd.read_csv(sheet)
    df = df[["Index", "Grade"]]

    subject = sheet[sheet.rfind('/') + 1: sheet.rfind('.')]

    for index, grade in df.itertuples(index=False):
        stu_index = stu_exits(index)
        if not stu_index:  # student not exists
            STUDENTS[stu_index].add_subject(subject, grade)
        else:
            stu = Student(index)
            stu.add_subject(subject, grade)
            STUDENTS.append(stu)



# for i in range(len(df)):
#     print(f"{STUDENTS[i].id} : {STUDENTS[i].subjects[0].name} : {STUDENTS[i].subjects[0].grade}")
