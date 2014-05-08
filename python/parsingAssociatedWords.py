
import sys
import csv
import operator

#weWords = ['acceptance', 'accommodation', 'accustomed', 'activity', 'admiration', 'adoption', 'adult', 'advice', 'advise', 'affection', 'affiliation', 'affinity', 'allegiance', 'ancestor', 'anniversary', 'anxiety', 'appreciation', 'approval', 'ardent', 'association', 'attentive', 'banns', 'baptism', 'betroth', 'bloodline', 'bonds', 'bone fide', 'breadwinner', 'bride', 'brotherly', 'care', 'care-giver', 'caring', 'celebration', 'celibate', 'chemistry', 'cherish', 'child', 'children', 'choice', 'civility', 'clan', 'close-knit', 'coach', 'cohort', 'cohort', 'colleague', 'comfortable', 'commitment', 'commonality', 'communicative', 'community', 'companion', 'compassion', 'compatibility', 'competitive', 'confidence', 'congenial', 'conjugal', 'connection', 'consideration', 'constancy', 'conversation', 'convivial', 'couple', 'courteous', 'custody', 'daughter', 'decent', 'defense', 'deferential', 'dependable', 'dependence', 'descent', 'determination', 'development', 'devoted', 'differences', 'divorce','dowry', 'dream', 'dress', 'earnest', 'easy', 'elder', 'eligible', 'emotional', 'empathy', 'encouragement', 'endearing', 'engaged', 'esteem', 'everlasting', 'fair', 'fairness', 'faithful', 'family', 'father', 'father-in-law', 'favorite', 'feelings', 'fidelity', 'first dance', 'flexibility', 'flowers', 'folks', 'forebear', 'forgiveness', 'foster child', 'foundation', 'fraternal', 'fraternal', 'fretful', 'friends', 'friendship', 'gatherings', 'genealogy', 'generation', 'generosity', 'genes', 'gentle', 'genuine', 'geriatric', 'gestation', 'gifts', 'gown', 'grandparent', 'grateful', 'gratitude', 'groom', 'group', 'groups', 'grownup', 'guardian', 'guests', 'guidance', 'habit', 'healthy', 'heir', 'helpful', 'helpmate', 'hereditary', 'heritage', 'history', 'honesty', 'honeymoon', 'hope', 'house guests', 'humor', 'husband', 'ideal', 'illness', 'impressive', 'in-laws', 'independence', 'industrious', 'infancy', 'inheritance', 'inspiration', 'instructive', 'insulting', 'integrity', 'intuitive', 'invitations', 'jocularity', 'joking', 'joy', 'judgment', 'justice of the peace', 'kin', 'kindness', 'kindred', 'kinfolk', 'kinship', 'kisses', 'lace', 'laughter', 'legal', 'lineage', 'listener', 'longevity', 'loving', 'loyalty', 'maiden name', 'majority', 'marriage', 'marry', 'married', 'mate', 'matriarch', 'matrimony', 'mature', 'mentoring', 'milestone', 'minor', 'mom', 'monogamy', 'morale', 'morals', 'mother', 'mother-in-law', 'natal', 'nephew', 'nest', 'newlywed', 'niece', 'nuclear family', 'nuptial', 'nurture', 'obedient', 'offspring', 'open-minded', 'optimism', 'origin', 'parent', 'partiality', 'partner', 'pastor', 'pastor', 'paternity', 'patience', 'patriarch', 'peace', 'people', 'perceptive', 'perseverance', 'philosophical', 'photographer', 'polite', 'positive', 'principles', 'progeny', 'protection', 'provider', 'quality', 'quantity', 'quiet', 'rabbi', 'race', 'reception', 'relation', 'relationship', 'relatives', 'reliability', 'reliance', 'religion', 'resilience', 'resolution of differences', 'respect', 'responsibility', 'retiring', 'reverence', 'reverend', 'ring', 'safety', 'security', 'select', 'senior', 'sensible', 'sensitivity', 'separation', 'service', 'sharing', 'similarities', 'sincerity', 'single', 'sisterhood', 'solidarity', 'son', 'soul mate', 'special', 'special day', 'speeches', 'spouse', 'standards', 'stepmother', 'supportive', 'surname', 'sweet', 'sympathetic', 'tact', 'teamwork', 'tender', 'thoughtfulness', 'ties', 'time together', 'together', 'tolerant', 'top heat', 'tradition', 'trait', 'tribe', 'triplet. troth', 'trust', 'trustworthy', 'truthful', 'tuxedo', 'understanding', 'unforgiving', 'union', 'unique', 'unite', 'unity', 'upbringing', 'valuable', 'values', 'variety', 'veil', 'vigilance', 'volunteer', 'vows', 'warmth', 'watchful', 'we', 'wedlock', 'wedding' 'welcoming', 'white', 'wife', 'willingness', 'wisdom', 'wise', 'with', 'wonderful', 'worry', 'worthwhile', 'worth', 'worthy', 'youngster', 'youth', 'zeal', "weve", "we've", "we'll", "well", "with", "other", "other's", "others", "eachother"]

#weWordsCondensed = ['child', 'children', 'cohort', 'colleague', 'community', 'companion', 'couple', 'daughter', 'family', 'father', 'fraternal','friends', 'friendship', 'gatherings', 'grandparent', 'group', 'groups', 'husband', 'kin', 'marriage', 'marry', 'married', 'mate', 'matrimony', 'mom', 'mother', 'mother-in-law', 'parent', 'partiality', 'partner', 'relationship', 'relatives', 'sharing', 'similarities', 'son', 'soul mate', 'spouse', 'teamwork', 'together', 'tradition', 'we', 'wife', 'with']


#iWords = ['alcohol', 'alone', 'annoying', 'apply', 'art', 'bachelor', 'beer', 'bored', 'boss', 'bullshit', 'campus', 'chill', 'chores', 'classes', 'college', 'crap', 'cute', 'date', 'deprived', 'detached', 'dreading', 'drink', 'drinking', 'drunk', 'duh', 'dumb', 'exhausted', 'fail', 'fml', 'fuck', 'fucked', 'grade', 'grades', 'hard', 'hate', 'hermit', 'homework', 'hunting', 'i', 'idiots', 'idiots', 'individual', 'insomnia', 'interview', 'isolated', 'job', 'jobs', 'lack', 'laundry', 'library', 'lone', 'lonesome', 'manager', 'me', 'meeting', 'mine', 'my', 'myself', 'need', 'needed', 'no', 'nope', 'not', 'nothin', 'nothing', 'office', 'on my own', 'online', 'only', 'paid', 'paper', 'pissed', 'position', 'pride', 'private', 'pub', 'reading', 'restless', 'resume', 'roommate', 'sales', 'school', 'school', 'security', 'single', 'single-handedly', 'sleep', 'sober', 'solitary', 'solo', 'stag', 'studying', 'suck', 'sucks', 'swag', 'tattoo', 'test', 'tired', 'unaided', 'unattached', 'wanna', 'want', 'without help', 'work', 'worked', 'working', 'workout', 'yolo', "i'll", "i'm", "i've", "ill", "im", "ive", "i'd", "id"]

#iWordsCondensed = ['alone', 'i', 'me', 'mine', 'my', 'myself', 'single', 'independence', "i'll", "i'm", "i've", "ill", "im", "ive", "i'd", "id"]

#weWordsCondensed = ['we', "weve", "we've", "we'll", "well", "with", "other", "other's", "others", "eachother"]
mainWeWords = ['acceptance', 'accommodation', 'accustomed', 'activity', 'admiration','advice', 'advise', 'affiliation', 'affinity', 'allegiance','appreciation', 'approval','ardent', 'association', 'attentive', 'banns', 'baptism', 'betroth', 'brotherly', 'care', 'care-giver', 'caring', 'celebration', 'celibate','cherish','comfortable','commonality', 'communicative', 'community','chemistry', 'choice', 'civility','coach', 'cohort', 'cohort', 'colleague',  'companion', 'compassion', 'compatibility', 'competitive', 'confidence', 'congenial', 'conjugal', 'connection', 'consideration', 'constancy', 'conversation', 'convivial','courteous', 'decent', 'defense', 'deferential', 'dependable', 'dependence', 'descent', 'determination', 'development', 'devoted', 'differences','dream','earnest', 'easy','emotional', 'empathy', 'encouragement', 'endearing', 'esteem','fair', 'fairness', 'faithful','favorite', 'feelings', 'fidelity','dress','flexibility', 'flowers', 'forebear', 'forgiveness','foundation','fretful','friends', 'friendship', 'gatherings','generosity','gentle', 'genuine', 'geriatric', 'gestation', 'gifts', 'grateful', 'gratitude', 'group', 'groups','guidance', 'habit', 'healthy', 'heir', 'helpful', 'helpmate', 'hereditary', 'heritage', 'history', 'honesty', 'hope', 'humor','ideal', 'illness', 'impressive', 'independence', 'industrious','inspiration', 'instructive', 'insulting', 'integrity', 'intuitive','jocularity', 'joking','joy', 'judgment','kindness','laughter','kisses','legal','listener', 'longevity', 'loving', 'loyalty','majority','mature', 'mentoring', 'milestone', 'minor', 'morale', 'morals', 'natal', 'nest','nurture', 'obedient','open-minded', 'optimism', 'origin', 'pastor','patience','peace','people','perceptive', 'perseverance', 'philosophical', 'photographer', 'polite', 'positive', 'principles', 'progeny', 'protection', 'provider', 'quality', 'quantity', 'quiet','race','reliability','reliance','resilience','relationship', 'relatives',  'religion', 'respect', 'responsibility', 'people','reverence', 'sharing', 'similarities', 'sincerity', 'single','soul mate', 'special','standards', 'supportive', 'sweet', 'sympathetic', 'tact', 'teamwork', 'tender', 'thoughtfulness', 'time', 'together', 'tolerant', 'top heat','trust', 'trustworthy', 'truthful','understanding', 'unforgiving', 'unique', 'unite','valuable', 'values', 'variety',"weve", "we've", "we'll", "well", "with", "other", "other's", "others", "eachother",'vigilance', 'volunteer','warmth', 'watchful', 'welcoming','willingness', 'wisdom', 'wise', 'with', 'wonderful', 'worry', 'worthwhile', 'worth', 'worthy','zeal', 'love', 'were', "we're", 'we']

familyWords = [ 'adoption', 'adult',  'affection', 'ancestor', 'anniversary', 'appreciation', 'approval', 'bloodline', 'bonds', 'bone fide', 'breadwinner', 'bride', 'brotherly', 'care', 'care-giver', 'caring', 'celebration', 'celibate',  'child', 'children',  'clan', 'close-knit',  'commitment',  'companion', 'compassion',  'couple', 'custody', 'daughter',  'divorce', 'dowry',   'elder', 'eligible',  'endearing', 'engaged',  'everlasting',  'family', 'father', 'father-in-law', 'folks',  'foster child',  'fraternal', 'friends', 'friendship', 'gatherings', 'genealogy', 'generation',  'genes', 'gown', 'grandparent',  'groom', 'group', 'groups', 'grownup', 'guardian', 'guests',  'honeymoon',  'house guests',  'husband', 'in-laws',  'infancy', 'inheritance',  'invitations',  'joy', 'judgment', 'kin', 'kindness', 'kindred', 'kinfolk', 'kinship', 'kisses', 'lace',  'lineage', 'loving', 'loyalty', 'maiden name',  'marriage', 'marry', 'married', 'mate', 'matriarch', 'matrimony',  'mom', 'monogamy','mother', 'mother-in-law',  'nephew',  'newlywed', 'niece', 'nuptial',  'offspring',  'parent', 'partiality', 'partner',  'paternity',  'patriarch', 'people',  'rabbi',  'reception', 'relation', 'relationship', 'relatives', 'religion', 'respect', 'responsibility', 'retiring', 'reverend', 'ring', 'safety', 'security', 'select', 'senior', 'sensible', 'sensitivity', 'separation', 'service',  'single', 'sisterhood', 'solidarity', 'son', 'soul', 'special', 'speeches', 'spouse',  'stepmother',  'surname',  'ties',  'together',  'tradition', 'trait', 'tribe', 'triplet', 'trust', 'trustworthy', 'truthful', 'tuxedo', 'union',  'unity', 'upbringing',  'veil',  'vows', 'we', 'wedlock', 'wedding'  'white', 'wife',  'youngster', 'youth',  "weve", "we've", "we'll", "well", "with", "other", "other's", "others", "eachother", 'house', 'home', 'kid', 'baby', 'honey', 'sweetie', 'love']

workWords = ['alcohol', 'apartment', 'house', 'home', 'apply', 'beer', 'boss', 'bullshit', 'date', 'deprived', 'dreading', 'drink', 'drinking', 'drunk', 'exhausted', 'fuck', 'fucked', 'hunting', 'i', 'interview', 'job', 'jobs', 'laundry', 'manager', 'me', 'meeting', 'mine', 'my', 'myself', 'need', 'needed', 'nothing', 'office', 'on my own', 'only', 'paid', 'position', 'pride', 'private', 'pub', 'resume', 'sales', 'single', 'single-handedly', 'sleep', 'sober', 'solo', 'tired', 'unaided', 'unattached', 'without help', 'work', 'worked', 'working', 'workout', 'bar', 'drink', 'shots', 'tequila', 'vodka', 'gin', 'party', 'partying', 'downtown', 'dance']

schoolWords = ['alcohol', 'apply', 'art', 'bachelor', 'beer', 'bored', 'campus', 'chill', 'chores', 'classes', 'college', 'cute', 'date', 'deprived', 'dreading', 'drink', 'drinking', 'drunk', 'fail', 'fucked', 'grade', 'grades', 'hard', 'hate', 'homework', 'i', 'idiot', 'idiots', 'individual', 'insomnia', 'interview', 'isolated',  'lack', 'laundry', 'library', 'lone', 'lonesome', 'me', 'mine', 'my', 'myself', 'need', 'needed', 'no', 'nope', 'not', 'nothin', 'nothing', 'online', 'only', 'paper', 'pissed', 'position', 'reading', 'school', 'school', 'single', 'single-handedly', 'sleep', 'solo', 'stag', 'studying', 'suck', 'sucks', 'swag', 'tattoo', 'test', 'tired', 'without help', 'work', 'worked', 'working', 'workout', 'yolo', "i'll", "i'm", "i've", "ill", "im", "ive", "i'd", "university"]

mainIWords = ['alone','bored', 'crap', 'deprived', 'detached', 'dreading', 'dumb', 'fail', 'fml', 'fuck', 'fucked', 'hard', 'hate', 'hermit', 'i',  'individual', 'insomnia', 'isolated', 'lack', 'lone', 'lonesome', 'me', 'mine', 'my', 'myself', 'need', 'needed', 'no', 'nope', 'not', 'nothin', 'nothing', 'on my own', 'only', 'paid', 'pissed', 'private', 'restless', 'single', 'single-handedly', 'sleep', 'solitary', 'solo', 'stag', 'suck', 'sucks', 'tired', 'unaided', 'unattached', 'wanna', 'want', 'without help', "i'll", "i'm", "i've", "ill", "im", "ive", "i'd", "id"]

mainWeArray = {}
familyArray = {}
workArray = {}
schoolArray = {}
mainIArray = {}
totals= {'mainWe' : 0, 'family' : 0, 'work' : 0, 'school' : 0, 'mainI' : 0}

def lookForWords(filename):
	with open(filename, 'rU') as topics:
		topicReader = csv.reader(topics)
		for line in topicReader:
			for word in line[1:]:
				if word in mainWeWords:
					totals["mainWe"] += 1
					if line[0] in mainWeArray:
						mainWeArray[line[0]] += 1
					else:
						mainWeArray[line[0]] = 1
				if word in familyWords:
					totals["family"] += 1
					if line[0] in familyArray:
						familyArray[line[0]] += 1
					else:
						familyArray[line[0]] = 1
				if word in workWords:
					totals["work"] += 1
					if line[0] in workArray:
						workArray[line[0]] += 1
					else:
						workArray[line[0]] = 1
				if word in schoolWords:
					totals["school"] += 1
					if line[0] in schoolArray:
						schoolArray[line[0]] += 1
					else:
						schoolArray[line[0]] = 1
				if word in mainIWords:
					totals["mainI"] += 1
					if line[0] in mainIArray:
						mainIArray[line[0]] += 1
					else:
						mainIArray[line[0]] = 1
	return (mainWeArray, familyArray, workArray, schoolArray, mainIArray, totals)


def filterArray(full, part):
	newArray = {}
	for key in full:
		if key in part:
			newArray[key] = full[key]
	return newArray


if __name__ == '__main__':
	csvFile = sys.argv[-1]
	lookForWords(csvFile)
	 # print "----------- I ARRAY -------------"
		#sorted_i = sorted(iArray.iteritems(), key=operator.itemgetter(1))
		#print sorted_i
		#print "----------- WE ARRAY -------------"
		#sorted_we = sorted(weArray.iteritems(), key=operator.itemgetter(1))
	 # print sorted_we
		# print filterArray(iArray, work)
		# print "work"
		# print filterArray(iArray, partying) 
		# print "partying"
		# print filterArray(iArray, otherI)
		# print "otherI"
		# print filterArray(iArray, mainI)
		# print "mainI"
		# print filterArray(weArray, otherWe)
		# print "otherWe"
		# print filterArray(weArray, friends)
		# print "friends"
		# print filterArray(weArray, mainWe)
		# print "mainWe"

#def yeah():
#	newList = [x.strip().lower() for x in iWords.split(',')]
#	print sorted(newList)

#yeah()