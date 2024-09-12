from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if groups:
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            # data.append(groups)

        specialty_names = set()
        for group in groups:
            specialty_names.add(group.specialty.name)
        return list(specialty_names)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
