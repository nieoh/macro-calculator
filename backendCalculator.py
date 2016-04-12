import math

###################################################################
#Stress factor calculator for Mifflin-St.Jeor Equation based upon activity level
#inputs: epw = number of exercises per week
###################################################################
def StressFactor(epw):
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

###################################################################
#Simplified Mifflin-St.Jeor Equation for calculating TDEE
#inputs:  sex: subset of ['f', 'F', 'm', 'M']
#  age(years): 
#  weight(kg):
#  height(cm):
#stressFactor: given by helper function StressFactor
###################################################################
def MifflinStJeorSimplified(sex, age, weight, height, stressFactor):
	#make sure that stressFactor is valid. If not, set it to sedentary. 
	if stressFactor == None:
		stressFactor = 1.2
	if sex.lower() == 'f':
		TDEE = (10*weight + 6.25*height - 5*age - 161)*stressFactor #kg, cm, yrs
	elif sex.lower() == 'm':
		TDEE = (10*weight + 6.25*height - 5*age - 5)*stressFactor #kg, cm, yrs
	else:
		print "Please enter valid gender"
		TDEE = None
	return TDEE


#nieoh 04/11/16 stats
print "TDEE given by simplified Mifflin-St.Jeor formula: %d kJ" %(MifflinStJeorSimplified('f', 26, 69.4, 165, StressFactor(5)))

###################################################################
#TDEE adjustment calculator. 
#Given average calories and average initial and average end weight for a week, outputs actual TDEE/day for the past week. 
#inputs: calories(kJ): avg / day for the week
#    startWeight(lbs): average weight from previous week (preferably at least 3 measurements)
#	   endWeight(lbs): average weight from this week
###################################################################
def TDEEAdjustment(calories, startWeight, endWeight):
	return calories - (endWeight - startWeight)*500

###################################################################
#Calculate macronutrient split based upon a percentage split
#inputs: calories(kJ): 
#           protein(): % of calories allotted to protein in decimal
#              carb(): % of calories allotted to carbs in decimal
#               fat(): % of calories allotted to fat in decimal
#output: list of protein, carb, fat in grams
###################################################################
def macroPercentageCalculator(calories, protein, carb, fat):
	p = math.ceil((calories * protein)/4)
	f = math.floor((calories * fat)/9)
	c = math.ceil((calories * carb)/4)
	return [p, c, f]


###################################################################
#General macronutrient calculator using specified method.
#Methods include: Percentage split; body-weight specific protein & percentage fat
#input: calories(kJ): calories to be split
###################################################################
def macroCalculator(calories, protein, carb, fat):
	[p,c,f] = macroPercentageCalculator(calories, protein, carb, fat)
	return "protein: %d g, carbs: %d g, fat: %d g" % (p, c, f)

#nieoh current stats
print macroCalculator(MifflinStJeorSimplified('f', 26, 69.4, 165, StressFactor(5)), .3, .4, .3)









