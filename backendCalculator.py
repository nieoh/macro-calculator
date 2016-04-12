
#input number of exercises per week
def stressFactor(epw):
	#Sedentary. No exercise
	if epw < 1:
		return 1.2
	#Mild activity. 1-3 days / week light exercise
	elif epw < 4:
		return 1.375
	#Moderate. 3-5 / week moderate exercise
	elif epw < 6:
		return 1.55
	#Heavy 6-7 / week heavy exercise
	elif epw < 8:
		return 1.7
	#Extreme. Twice per day, extra heavy workouts. 
	elif epw > 7:
		return 1.9
	#fail
	else:
		return None

#Simplified Mifflin-St.Jeor Equation
def MifflinStJeorSimplified(sex, age, weight, height, stressFactor):
	#make sure that stressFactor is valid. If not, set it to sedentary. 
	if stressFactor == None:
		stressFactor = 1.2
	if sex.lower() == 'f':
		REE = (10*weight + 6.25*height - 5*age - 161)*stressFactor #kg, cm, yrs
	elif sex.lower() == 'm':
		REE = (10*weight + 6.25*height - 5*age - 5)*stressFactor #kg, cm, yrs
	else:
		print "Please enter valid gender"
		REE = None
	return REE

print MifflinStJeorSimplified('f', 26, 69.4, 165, stressFactor(5))