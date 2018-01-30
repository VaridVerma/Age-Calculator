cd=input("current date")
cm=input("current month")
cy=input("current year")
dd=input("birth date")
dm=input("birth month")
dy=input("birth year")

#for date calculation
if cd>dd:
	d=cd-dd
else:
	#for month with 31 days
	if cm in [1,3,5,7,8,10,12]:
		cd=cd+31
	#for month with 30 days
	if cm in [4,6,9,11]
		cd=cd+30
	#for february
	if cm == 2:
		#for leap year
		if cy%4==0:
			cd=cd+29
		#for non leap year
		else:
			cd=cd+28
	d=cd-dd
	cm=cm-1

#for month calculation
if cm>dm:
	m=cm-dm
else:
	cm+=12
	m=cm-dm
	cd-=1
	
#for year calculation
y=cy-dy


print y," Years ",m," Months ",d," Days "
