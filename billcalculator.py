# # excercise 1
def tip(bill, percentage):
	tip = bill * (percentage * .01)
	return tip

def total(bill, percentage):
	total = bill + tip(bill, percentage)
	return total

def split(bill, percentage, people):
	split = (bill + tip(bill, percentage)) / people
	return split


def main():
	# bill = 100.00
	percentage = 18
	people = 2

	user_bill = float(raw_input("how much was your bill? "))
	
	print tip(user_bill, percentage)
	print total(user_bill,percentage)
	print split(user_bill,percentage,people)

main()
# print total_bill(subtotal)



# excercise 2



