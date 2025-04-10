import pandas as pd
from pathlib import Path
import Subject
from Student import Student
from natsort import natsorted

STUDENTS = []
SHEETS_DIR = "Sheets/CS/"
START_INDEX = '2000'  # to filter only current year students(Ignore repeat students)
EXPORT_PATH = "Rankings/CS/"
EXPORT_NAME = "Rankings_CS_Second_Year_First_Sem.csv"

Subject.initialize_readings()


def stu_exits(id_):
    for i in range(len(STUDENTS)):
        if STUDENTS[i].get_id() == id_:
            return i
    return -1


sheet_list = sorted(Path(SHEETS_DIR).rglob('*.csv'))
subjects_indices = []
subjects_names = []
for sheet in sheet_list:
    sheet = str(sheet)

    sheet_df = pd.read_csv(sheet)
    sheet_df = sheet_df[["Index No", "Result"]]

    subject_code = sheet[sheet.rfind('/') + 1: sheet.rfind('.')]
    if 'R' not in subject_code:
        subjects_indices.append(subject_code)
        subjects_names.append(Subject.get_sub_name(subject_code))
    else:
        subject_code = subject_code[:subject_code.find('R') - 1]  # SCS 2201-R -> SCS 2201

    for index, grade in sheet_df.itertuples(index=False):
        if str(index)[:4] != START_INDEX:
            continue
        stu_index = stu_exits(index)
        if stu_index < 0:  # student not exists
            stu = Student(index)
            stu.add_subject(subject_code, grade)
            STUDENTS.append(stu)
        else:
            STUDENTS[stu_index].add_subject(subject_code, grade)
result_df = pd.DataFrame(columns=["Index", "Total GPV", "GPA"] + subjects_names)
for i in range(len(STUDENTS)):
    row = [STUDENTS[i].id, STUDENTS[i].get_total_gpv(), STUDENTS[i].get_gpa()]
    for j in range(len(subjects_indices)):
        row.append(
            STUDENTS[i].get_subject(subjects_indices[j]).get_grade() if STUDENTS[i].get_subject(subjects_indices[j])
            else ""
        )
    result_df.loc[i] = row

# Add rank columns and sort
result_df.insert(0, "Rank", result_df["GPA"].rank(method="min", ascending=False))
result_df = result_df.sort_values(by='Rank', na_position='first')

result_df.to_csv(EXPORT_PATH + EXPORT_NAME, index=False)
