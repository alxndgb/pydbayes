#############################################################################
# There is an R-like data frame package
import pandas as pan
import numpy as np
import math

dataframe = pan.read_table('smallDF_pheno.txt', sep = '\t')
#data = dataframe.drop(dataframe.columns[0], axis = 1)
data = dataframe
data = data * 1.0 # Convert to floats - will be easier later on
dimensions = data.shape
print(dimensions)

globalEQSS = 550
genotypes = data[data.columns[1]]
clinical = data[data.columns[2]]
conditionalPrior = generateGeneticPrior(genotypes, clinical, globalEQSS)
score = MCR(data, conditionalPrior, 1, 2)
print(score)


# Work out some timings
with Timer() as t:
	for test in xrange(0,1000):
		score = MCR(data, conditionalPrior, 1, 2)
print(t.secs)


with Timer() as t:
	for test in xrange(0,1000):
		score = MCRFast(data, conditionalPrior, 1, 2, 3, 4)
print(t.secs)