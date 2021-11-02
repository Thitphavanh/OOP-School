(OOP School) ໄລບຣາຣີ່ສຳຫຼັບໃຊ້ຮຽນ Python OOP by Hery Phenomenal
==============================================
ໂປຣແກຣມໃຊ້ຮຽນ OOP :

ວິທິຕິດຕັ້ງ
~~~~~~~~~~~

ເປີດ CMD / Terminal

.. code:: python

    pip install OOPHerySchool
##### ວິທີໃຊ້ງານແພັກເກດນີ້

ວິທີໃຊ້
~~~~~~~

[STEP 1] - ເປີດ IDLE ຂຶ້ນມາແລ້ວພິມ...

.. code:: python
from OOPHerySchool import Student,Tesla,SpecialStudent,Teacher
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


ພັດທະນາໂດຍ: Hery Phenomenal
