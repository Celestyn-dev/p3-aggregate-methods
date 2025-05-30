from datetime import datetime

class Course:
    all = []

    def __init__(self, name):
        self._name = name
        self._enrollments = []
        Course.all.append(self)

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

    def get_enrollments(self):
        return self._enrollments.copy()

    def get_name(self):
        return self._name


class Enrollment:
    all = []

    def __init__(self, student, course):
        self._student = student
        self._course = course
        self._enrollment_date = datetime.now()
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class Student:
    all = []

    def __init__(self, name):
        self._name = name
        self._enrollments = []
        self._grades = {}
        Student.all.append(self)

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
            return enrollment
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def add_grade(self, enrollment, grade):
        self._grades[enrollment] = grade

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total = sum(self._grades.values())
        return total / len(self._grades)

    def get_name(self):
        return self._name