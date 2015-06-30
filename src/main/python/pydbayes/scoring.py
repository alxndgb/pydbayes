import math

import pandas as pan
import numpy as np


##########################################################################

def MSR(dataVec, priorVec):
    prob = 0.0
    prob = math.lgamma(priorVec.sum()) - math.lgamma(priorVec.sum() + dataVec.size)

    x = dataVec.value_counts()
    numLevels = x.size

    for xLevel in xrange(0, numLevels):
        prob = prob + math.lgamma(priorVec[xLevel] + x[x.index == (xLevel)]) - math.lgamma(priorVec[xLevel])
    return prob


##########################################################################

def MCR(dataMatrix, priorMatrix, predictorInx, responseInx):
    x = dataMatrix[dataMatrix.columns[predictorInx]]
    y = dataMatrix[dataMatrix.columns[responseInx]]
    condTable = pan.crosstab(y, x)
    numLevelsY = condTable.shape[0]
    numLevelsX = condTable.shape[1]

    prob = 0.0
    hypers = priorMatrix.sum()
    observed = condTable.sum()

    for xLevel in xrange(0, numLevelsX):
        prob = prob + math.lgamma(hypers[xLevel]) - math.lgamma(hypers[xLevel] + observed[xLevel])
        for yLevel in xrange(0, numLevelsY):
            prob = prob + math.lgamma(
                priorMatrix[priorMatrix.columns[xLevel]][yLevel] + condTable[xLevel][yLevel]) - math.lgamma(
                priorMatrix[priorMatrix.columns[xLevel]][yLevel])

    return prob


def MCRFast(dataMatrix, priorMatrix, predictorInx, responseInx, numLevelsX, numLevelsY):
    condTable = pan.crosstab(dataMatrix[dataMatrix.columns[responseInx]], dataMatrix[dataMatrix.columns[predictorInx]])
    prob = 0.0
    hypers = priorMatrix.sum()
    observed = condTable.sum()

    for xLevel in xrange(0, numLevelsX):
        prob = prob + math.lgamma(hypers[xLevel]) - math.lgamma(hypers[xLevel] + observed[xLevel])
        for yLevel in xrange(0, numLevelsY):
            prob = prob + math.lgamma(
                priorMatrix[priorMatrix.columns[xLevel]][yLevel] + condTable[xLevel][yLevel]) - math.lgamma(
                priorMatrix[priorMatrix.columns[xLevel]][yLevel])

    return prob


##########################################################################

def HardyWeinburg(genotypes):
    genotypeFrequencies = genotypes.value_counts()
    totalPopulation = len(genotypes)
    AA = 0
    Aa = 1
    aa = 2
    freqAA = genotypeFrequencies[genotypeFrequencies.index == AA][AA]
    freqAa = genotypeFrequencies[genotypeFrequencies.index == Aa][Aa]
    freqaa = genotypeFrequencies[genotypeFrequencies.index == aa][aa]
    A = ((2.0 * freqAA) + freqAa) / (2.0 * (freqAA + freqAa + freqaa))
    a = 1.0 - A
    expAA = math.pow(A, 2) * totalPopulation
    expAa = 2.0 * A * a * totalPopulation
    expaa = math.pow(a, 2) * totalPopulation
    exp = [[], [], []]
    exp[0] = expAA
    exp[1] = expAa
    exp[2] = expaa
    return pan.DataFrame(exp)


##########################################################################

def HardyWeinburgNormalized(genotypes):
    genotypeFrequencies = genotypes.value_counts()
    totalPopulation = np.sum(genotypeFrequencies)
    AA = 0
    Aa = 1
    aa = 2
    freqAA = genotypeFrequencies[genotypeFrequencies.index == AA][AA]
    freqAa = genotypeFrequencies[genotypeFrequencies.index == Aa][Aa]
    freqaa = genotypeFrequencies[genotypeFrequencies.index == aa][aa]
    A = ((2.0 * freqAA) + freqAa) / (2.0 * (freqAA + freqAa + freqaa))
    a = 1 - A
    expAA = math.pow(A, 2)
    expAa = 2 * A * a
    expaa = math.pow(a, 2)
    exp = [[], [], []]
    exp[0] = expAA
    exp[1] = expAa
    exp[2] = expaa
    return np.asmatrix(exp)


##########################################################################

def generateConditionalPrior(priorVec1, priorVec2, globalEQSS):
    mat = priorVec2.dot(priorVec1.T)
    m = mat * (globalEQSS / sum(mat.sum()))
    return m


##########################################################################

def generateGeneticPrior(dataVec1, dataVec2, globalEQSS):
    genotypes = dataVec1
    clinical = dataVec2
    expGenotypes = HardyWeinburg(dataVec1)
    normGen = expGenotypes / expGenotypes.min()
    clin = pan.DataFrame(dataVec2.value_counts())
    normClin = (clin * 1.0) / (clin.min() * 1.0)  # Convert counts to floats
    return generateConditionalPrior(normGen, normClin, globalEQSS)
