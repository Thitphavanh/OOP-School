# -*- coding: utf-8- -*-
# newschool

import school
from school import Student,SpecialStudent
from school import * # * is import all

def Test():
	'''
	ນີ້ແມ່ນໂຕຢ່າງການຂຽນໂປຣແກຣມໂດຍໃຊ້ເພັກເກດນີ້
	st1 = school.Student('Albert','Einstein')
	print(st1)

	st2 = Student('Bill','Gates')
	print([st2])


	stp2 = SpecialStudent('T','E','P')

	teacher1 = Teacher('Elon')

	'''
	st1 = school.Student('Albert','Einstein')
	print(st1)

	st2 = Student('Bill','Gates')
	print([st2])


	stp2 = SpecialStudent('T','E','P')

	teacher1 = Teacher('Elon')
	print(teacher1.fullname)

print(help(Test))