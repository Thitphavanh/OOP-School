# -*- coding:utf-8- -*-
# school
class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.exp = 0  # ຄະແນນປະສົບການ
        self.lesson = 0  # ຈຳນວນຄລາສທີ່ເຄີຍຮຽນ
        self.vehcle = 'ລົດເມ'

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    def Coding(self):
        ''' ນີ້ແມ່ນຄລາສຮຽໜວິຊາຂຽນໂປຣແກຣມ '''
        self.AddEXP()
        print('{} ກຳລັງຮຽນຂຽນໂປຣແກຣມ...'.format(self.fullname))

    def ShowEXP(self):
        print('{} ໄດ້ຄະແນນ {} exp (ຮຽນໄປ {} ຄັ້ງ)'.format(self.name,self.exp,self.lesson))
    
    def AddEXP(self):
        self.exp += 10 # self.exp = self.exp + 10
        self.lesson += 1 # self.lesson = self.lesson + 1

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return self.fullname

    def __add__(self,other):
        return self.exp + other.exp


class Tesla:
    def __init__(self):
        self.model = 'Model S'

    def SelfDrivng(self,st):
        print('ລະບົບຂັບເຄື່ອນອໍໂຕກຳລັງເຮັດວຽກ...ກຳລັງພາ {} ກັບເຮືອນ!'.format(st.name))

    def __str__(self):
        return self.model

class SpecialStudent(Student):
    def __init__(self,name,lastname,father):
        super().__init__(name,lastname)

        self.father = father
        self.vehcle = Tesla()
        print('ຮູ້ບໍຂ້ອຍລູກໃຜ?...! ພໍ່ຂ້ອຍຊື່ {}'.format(self.father))        

    def AddEXP(self):
        self.exp += 30
        self.lesson += 2

class Teacher:
    def __init__(self,fullname):
        self.fullname = fullname
        self.students = []

    def CheckStudent(self):
        print('---- ນັກຮຽນຂອງນາຍຄູ {} ----'.format(self.fullname))
        for i,st in enumerate (self.students):  
            print('{} --> {} [{} exp][ຮຽນໄປ {} ຄັ້ງ]'.format(i+1, st.fullname,st.exp,st.lesson))

    def AddStudent(self,st):
        self.students.append(st)

# print('FILE:',__name__)
if __name__ == '__main__':
    


    # Day 0
    allstudent = []

    teacher1 = Teacher('Steve Jobs')
    teacher2 = Teacher('Elon Musk')
    print(teacher1.students)


    # day 1
    print('----Day 1----')
    st1 = Student('Albert', 'Einstein')
    allstudent.append(st1) # ສະມັກແລ້ວເກັບໄວ້ໃນລິສຕ໌ນັກຮຽນທັນທີ
    teacher2.AddStudent(st1)
    print(st1.fullname)


    # Day 2
    print('----Day 2----')
    st2 = Student('Bill','Gates')
    allstudent.append(st2)
    teacher2.AddStudent(st2)
    print(st2.fullname)

    # Day 3
    print('----Day 3----')
    for i in range(3):
        st1.Coding()

    st2.Coding()
    st1.ShowEXP()
    st2.ShowEXP()

    # Day 4
    print('----Day 4----')
    stp1 = SpecialStudent('Thomas','Edison','Hitler')
    allstudent.append(stp1)
    teacher1.AddStudent(stp1)
    print(stp1.fullname)
    print('ນາຍຄຸ ຂໍຄະແນນຟຣີຈັກ 20 ຄະແນນໄດ້ບໍ...?')
    stp1.exp = 20 # ແກ້ໄຂຄ່າໃນຄລາສໄດ້
    stp1.Coding()
    stp1.ShowEXP()

    # Day 5
    print('----Day 5----')
    print('ນັກຮຽນກັບເຮືອນກັນແນວໃດ?')
    print(allstudent)
    for st in allstudent:
        print('ຂ້ອຍ : {} ກັບບ້ານດ້ວຍ {} ເຈົ້າ'.format(st.name,st.vehcle))
        if isinstance(st,SpecialStudent):
            st.vehcle.SelfDrivng(st)

    # Day 6
    print('----Day 6----')

    teacher1.CheckStudent()
    teacher2.CheckStudent() 
    print('ລວມພະລັງຂອງນັກຮຽນ 2 ຄົນ', st1 + st2)