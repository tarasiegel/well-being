
import sys
import csv
from decimal import *



populationDict = {}
statePopulationDict = {}
stateDict = {}
firstLine = []

def createPopulationDict(populationFile, topicFile):
	with open(populationFile, 'rU') as population:
		populationReader = csv.reader(population)
		for line in populationReader:
			populationDict[line[0]] = line[5]

	with open(topicFile, 'rU') as topics:
		topicReader = csv.reader(topics)
		for line in topicReader:
			if line[0] != "cty_id":
				if int(line[0][:-3]) in statePopulationDict.keys():
					statePopulationDict[int(line[0][:-3])] += int(populationDict[line[0]])
				else:
					statePopulationDict[int(line[0][:-3])] = int(populationDict[line[0]])
	print statePopulationDict


def lookForWords(topicFile):
	with open(topicFile, 'rU') as topics:
		topicReader = csv.reader(topics)
		for line in topicReader:
			if line[0] != "cty_id":
				row = []
				for word in line[1:]:
					population = populationDict[line[0]]
					#print "line: " + line[0] + " pop: " + population + " word: " + word
					row.append(float(Decimal(population)*Decimal(word)))
				if int(line[0][:-3]) in stateDict.keys():
					current = stateDict[int(line[0][:-3])]
					for i in range(len(row)):
						current[i] += row[i]
					stateDict[int(line[0][:-3])] = current
				else:
					stateDict[int(line[0][:-3])] = row
			else:
				firstLine = line[1:]
	for state in stateDict.keys():
		stateArray = stateDict[state]
		newArray = []
		for i in range(len(stateArray)):
			newValue = stateArray[i]/(float(statePopulationDict[state]))
			newArray.append(newValue)
		stateDict[state] = newArray
	#print stateDict


def writeFile():
	with open('stateTopicIds.csv', 'wb') as output:
			outputWriter = csv.writer(output)
			firstRow = []
			firstRow.append("stateID")
			for word in firstLine:
				firstRow.append(word)
			outputWriter.writerow(firstRow)	
			for state in stateDict.keys():
				row = []
				row.append(state)
				stateArray = stateDict[state]
				for i in range(len(stateArray)):
					row.append(stateArray[i])
				outputWriter.writerow(row)


if __name__ == '__main__':
    topicFile = sys.argv[1]
    populationFile = sys.argv[2]
    createPopulationDict(populationFile, topicFile)
    lookForWords(topicFile)
    writeFile()