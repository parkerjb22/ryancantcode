import json, sys, getopt
from datetime import datetime, timedelta


now = datetime.now()

def readJson(data, delta):
	for item in data:
		d = datetime.strptime(item['Time'], '%Y-%m-%dT%H:%M:%S.%fZ')
		if (now - d > delta):
			print ("%s is more than %s old (%s)" % (item['Name'], str(delta), item['Time']))


def main(argv):
	inputfile = ''
	numDays = 2
	try:
		opts, args = getopt.getopt(argv,"hf:d:",["file=","days="])
	except getopt.GetoptError:
		print ('rcc.py -f <file> -d <days>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('rcc.py -f <file> -d <days>')
			sys.exit()
		elif opt in ("-f", "--file"):
			inputfile = arg
		elif opt in ("-d", "--days"):
			numDays = arg

	delta = timedelta(days=int(numDays))
	with open('data.json') as data_file:    
		data = json.load(data_file)
		readJson(data, delta)

if __name__ == "__main__":
   main(sys.argv[1:])