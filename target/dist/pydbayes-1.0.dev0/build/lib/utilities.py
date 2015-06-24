def readDataFromFile(filename, sep = '\t'):
	dataFile = open(filename, 'r')
	columnHeadings = dataFile.readline()
	columnHeadings = columnHeadings.strip('\n')
	columns = columnHeadings.split(sep)
	data = [[] for dummy in xrange(len(columns))]
	for line in dataFile.readlines():
		fields = line.strip('\n').split(sep)
		for i, number in enumerate(fields):
			data[i].append(number)
	results = list()
	results.append(columns)
	results.append(data)
	return results


