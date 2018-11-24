print "Welcome to programme that coverts kilometres into miles. All you have to do is enter the desired distance in kilometres and programme will convertit to miles itself."
"""
def kmToMiles():                              # ako zelim definirati funkciju da se ne ponavlja ista vrijednost varijable u while petlji
	km = float(input("Enter the value in kilometres: "))
	print "Your value counts " + str(km * 1.609344) + " miles."
"""
#kmToMiles()
km = float(input("Enter the value in kilometres: "))
print "Your value counts " + str(km * 0.6213) + " miles."
POTVRDA = "Y"

while True:
	answer = raw_input("Do you want to enter new value? Press Y if yes and N if no: ")
	if answer.upper() == POTVRDA:
		#kmToMiles()
		km = float(input("Enter the value in kilometres: "))
		print "Your value counts " + str(km * 1.609344) + " miles."
	else:
		print "Goodbye"
		break


