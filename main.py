import diversityanalysis

def printTitle(title):
	print('\n     F      M F/M '+title)


def printDistribution(gender, item):
	f = gender.get('F',0)
	m = gender.get('M',0)
	r = f/m if m > 0 else 0.0
	print("%6d %6s %3.1f %s" % (f, m, r, item))


def main():

	diversityanalysis.init('genderdata.csv')

	gender = diversityanalysis.genderDistribution()
	printTitle('Total')
	printDistribution(gender,"Gender")

	college = diversityanalysis.collegeDistribution()
	printTitle('College')
	for k in sorted(college.keys()):
		printDistribution(college[k],k)

	department = diversityanalysis.departmentDistribution()
	printTitle('Department')
	for k in sorted(department.keys()):
		printDistribution(department[k],k)

	major = diversityanalysis.majorDistribution()
	printTitle('Major')
	for k in sorted(major.keys()):
		printDistribution(major[k],k)

	term = diversityanalysis.termDistribution()
	printTitle('Term')
	for k in sorted(term.keys()):
		printDistribution(term[k],k)


main()