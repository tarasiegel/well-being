
import sys
import csv
from decimal import *
from parsingAssociatedWords import *


mainWeDict= {}
friendsDict= {}
workDict = {}
schoolDict = {}
mainIDict = {}

firstLine = []

def filterOutWords(topicFile, csvFile):
	mainWe, friends, work, school, mainI, totals = lookForWords(csvFile)
	with open(topicFile, 'rU') as topics:
		topicReader = csv.reader(topics)
		for line in topicReader:
			if line[0] != "state_id":
				topicIndex = 0
				for word in line[1:]:
					if str(topicIndex) in friends:
						if line[0] in friendsDict:
							friendsDict[line[0]] += float(float(word)*float(friends[str(topicIndex)]))				
						else:
							friendsDict[line[0]] = float(float(word)*friends[str(topicIndex)])
					if str(topicIndex) in mainWe:
						if line[0] in mainWeDict:
							mainWeDict[line[0]] += float(float(word)*mainWe[str(topicIndex)])
						else:
							mainWeDict[line[0]] = float(float(word)*mainWe[str(topicIndex)])
					if str(topicIndex) in work:
						if line[0] in workDict:
							workDict[line[0]] += float(float(word)*float(work[str(topicIndex)]))				
						else:
							workDict[line[0]] = float(float(word)*work[str(topicIndex)])
					if str(topicIndex) in school:
						if line[0] in schoolDict:
							schoolDict[line[0]] += float(float(word)*float(school[str(topicIndex)]))				
						else:
							schoolDict[line[0]] = float(float(word)*school[str(topicIndex)])
					if str(topicIndex) in mainI:
						if line[0] in mainIDict:
							mainIDict[line[0]] += float(float(word)*float(mainI[str(topicIndex)]))				
						else:
							mainIDict[line[0]] = float(float(word)*mainI[str(topicIndex)])
					topicIndex += 1
			else:
				firstLine = line[1:]
	for friend in friendsDict:
			friendsDict[friend] = float(friendsDict[friend])/float(totals['family'])
	for mainWe in mainWeDict:
			mainWeDict[mainWe] = float(mainWeDict[mainWe])/float(totals['mainWe'])
	for school in schoolDict:
			schoolDict[school] = float(schoolDict[school])/float(totals['school'])
	for work in workDict:
			workDict[work] = float(workDict[work])/float(totals['work'])
	for mainI in mainWeDict:
			mainIDict[mainI] = float(mainIDict[mainI])/float(totals['mainI'])

def writeFile():
	with open('stateTopicWords1.csv', 'wb') as output:
		outputWriter = csv.writer(output)
		firstRow = []
		firstRow.append("stateID")
		for word in firstLine:
			firstRow.append(word)
		outputWriter.writerow(firstRow)	
		for state in sorted(friendsDict):
			row = []
			row.append(state)
			row.append(mainIDict[state])
			row.append(schoolDict[state])
			row.append(workDict[state])
			row.append(friendsDict[state])
			row.append(mainWeDict[state])
			outputWriter.writerow(row)


if __name__ == '__main__':
    topicFile = sys.argv[1]
    csvFile = sys.argv[2]
    filterOutWords(topicFile, csvFile)
    writeFile()