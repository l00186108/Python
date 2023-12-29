'''
Script: people.py
By: NMC
Purpose: In any complex application, create a base class which will never be instantiated.
Date: 27OCT23
'''
class People():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for People")
        self.dob = None  # Date of birth
        self.title = None  # Title (e.g., Mr., Mrs., Dr.)
        self.first_name = None  # First name
        self.middle_initial = None  # Middle initial
        self.surname = None  # Last name

    def find_age(self):
        pass

class Staff(People):
    def __init__(self) -> None:
        # Call back to the parent class
        print("Running constructor for Staff")
        People.__init__(self)
        self.staff_id = None  # Staff ID
        self.start_date = None  # Date of employment
        self.debug = True  # Debug flag for staff

    def length_of_service(self):
        if self.debug:
            print("Staff->Length_of_service")
        pass

class Student(People):
    def __init__(self) -> None:
        # Call back to the parent class
        print("Running constructor for Student")
        People.__init__(self)
        self.student_id = None  # Student ID
        self.start_date = None  # Start date of enrollment

    def length_of_attendance(self):
        print("Yoo hoo!")
        pass

class AcademicStaff(Staff):
    def __init__(self) -> None:
        # Call back to the parent class
        print("Running constructor for AcademicStaff")
        Staff.__init__(self)
        self.primary_qualification = None  # Primary qualification
        self.academic_grade = None  # Academic grade

    def academic_cbt(self):
        pass

class AdminStaff(Staff):
    def __init__(self) -> None:
        # Call back to the parent class
        print("Running constructor for AdminStaff")
        Staff.__init__(self)
        self.primary_qualification = None  # Primary qualification
        self.job_description = None  # Job description
        self.department = None  # Department

    def academic_cbt(self):
        pass