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
	return math.floor(calories - (endWeight - startWeight)*500)

###################################################################
#Calculate calories allotment for a day given TDEE and weight change goals
#inputs:  TDEE(kJ): calories for TDEE calculated
#weightChange(lbs): desired positive or negative avg change in weight / week
###################################################################
def CaloriesAllotment(TDEE, weightChange):
	return math.floor(TDEE + 500 * weightChange)

###################################################################
#Calculate macronutrient split based upon a percentage split
#inputs: calories(kJ): 
#           protein(): % of calories allotted to protein in decimal
#              carb(): % of calories allotted to carbs in decimal
#               fat(): % of calories allotted to fat in decimal
#output: list of protein, carb, fat in grams
###################################################################
def macroPercentage(calories, protein, carb, fat):
	p = math.ceil((calories * protein)/4)
	f = math.floor((calories * fat)/9)
	c = math.ceil((calories * carb)/4)
	return [p, c, f]

###################################################################
#Calculate protein based upon body weight and a percentage, fat by body weight and a percentage, and carbs as remainder
#This is the method 3SFitness uses
#Need more research on this formula
#inputs: calories(kJ):
#         weight(lbs):
#           protein(): % of weight for protein given as decimal (usually between 0.6 - 1.2)
#               fat(): % of weight for fat given as decimal (usually .3)
###################################################################
def macroBodyWeight(calories, weight, protein, fat):
	p = math.ceil(weight * protein)
	f = math.floor(weight * fat)
	c = math.ceil((calories - p * 4 - f * 9)/4)
	return [p, c, f]




###################################################################
#General macronutrient calculator using specified method.
#Methods include: Percentage split; body-weight specific protein & percentage fat
#input: calories(kJ): calories to be split
#         weight(lb): current weight in lbs
###################################################################
def macroCalculator(calories, weight, protein, carb, fat, method):
	if method == "percentage":
		[p, c, f] = macroPercentage(calories, protein, carb, fat)
	elif method == "bodyweight":
		[p, c, f] = macroBodyWeight(calories, weight, protein, fat)
	return "protein: %d g, carbs: %d g, fat: %d g" % (p, c, f)

#nieoh current stats using % method
print "Using percentage method: %s" % macroCalculator(MifflinStJeorSimplified('f', 26, 69.4, 165, StressFactor(5)), None,.3, .4, .3, "percentage")
#nieoh current stats using bodyweight method
print "Using bodyweight method: %s" % macroCalculator(MifflinStJeorSimplified('f', 26, 69.4, 165, StressFactor(5)), 153, 1.1, None, .3, "bodyweight")

#nieoh current stats using bodyweight method with -1 lb / week goal
TDEE = MifflinStJeorSimplified('f', 26, 69.4, 165, StressFactor(5))
calories = CaloriesAllotment(TDEE, -1)
print "Using bodyweight method with -1lb / week goal: %s" % macroCalculator(calories, 153, 1.1, None, .3, "bodyweight")










