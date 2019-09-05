class Student:

    homepers = 0.3
    quizpers = 0.2
    particpers = 0.1
    projectpers = 0.4

    def __init__(self, ID, firstName, LastName, phone, gender, birthDate):
        self.ID = ID
        self.fullName = firstName + " " + LastName
        self.email = firstName + "." + LastName + "@aua.am"
        self.phone = phone
        self.gender = gender
        self.birthDate = birthDate

    def getPersonalInfo(self):
        print(self.ID)
        print(self.fullName)
        print(self.email)
        print(self.phone)
        print(self.gender)
        print(self.birthDate)

    def getCurrentGrade(self, homework, quizes, participation, project):
        currentgrade = homework*Student.homepers+quizes*Student.quizpers+participation*Student.particpers+project*Student.projectpers
        print(currentgrade)


def main():
    st1 = Student("AUA123", "Gor", "Isoyan", 12345, "M", "01/01/2019")
    st2 = Student("AUA133", "Ani", "Zadikyan", 825980, "F", "01/04/2019")

    # st1.getPersonalInfo()
    # st2.getPersonalInfo()
    st1.getCurrentGrade(95,90,95,93)
main()