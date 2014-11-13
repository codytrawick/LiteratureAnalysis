from string import letters

letterFrequency = {}
wordLengthFreq = {}
wordsPerLineFreq = {}
wordFreq = {}

def wordsPerLine(line):
  wordList=line.split()
  wordNumber = len(wordList)
  wordsPerLineFreq[wordNumber]=wordsPerLineFreq.get(wordNumber,0) + 1
  return wordList

def removePunctuation(word):
  newWord = ""
  for letter in word:
    if letter in letters:
      newWord += letter.lower()
  return newWord

def wordCount(wordList):
  for word in wordList:
    word = removePunctuation(word)
    wordFreq[word] = wordFreq.get(word,0) + 1

def wordLengthFreqFunc(wordList):
  for word in wordList:
    wordLength = len(word)
    wordLengthFreq[wordLength] = wordLengthFreq.get(wordLength,0) + 1

def letterCount(line):
  for letter in line:
    letter = letter.lower()
    letterFrequency[letter] = letterFrequency.get(letter,0)+1

def analyzeLine(line):
  wordList=wordsPerLine(line)
  wordLengthFreqFunc(wordList)
  wordCount(wordList)
  letterCount(line)

def readDocument(name):
  f = open(name+".txt")
  line = f.readline()
  while line != "":
    analyzeLine(line)
    line = f.readline()
  f.close()

def dictSort(aDict):
  values = aDict.items()
  values.sort(key=lambda x: x[1], reverse = True)
  return values

def writeAnalysis(text):
  fSource=open(text+".txt")
  title = fSource.readline()
  title = title[:len(title)-1]
  fSource.close()

  f=open(text+"Analysis.txt","w")
  f.write(title.upper() + " ANALYSIS\n")
  letterAnalysis = letterFrequency.items()
  wordCountAnalysis = dictSort(wordFreq)

  f.write("Letter Frequency\n")
  for letterTuple in letterAnalysis:
    if letterTuple[0] == "\n":
      letterTuple = ("\\n",letterTuple[1])
    myStr = "The letter {} was used {} times.\n"
    f.write(myStr.format(*letterTuple))

  f.write("\nWord Length Frequency.\n")
  for lengthTuple in wordLengthFreq.items():
    myStr = "{1} words were {0} characters long.\n"
    f.write(myStr.format(*lengthTuple))

  f.write("\nLine Length Analysis\n")
  for lineTuple in wordsPerLineFreq.items():
    myStr = "{1} lines had {0} characters in it.\n"
    f.write(myStr.format(*lineTuple))

  f.write("\nMost Frequently Used Words:\n")
  index = 0
  while wordCountAnalysis[index][1] > 100:
    f.write(wordCountAnalysis[index][0]+"\n")
    index += 1

  f.write("\nWords Used Only Once:\n")
  index = len(wordCountAnalysis)-1
  while wordCountAnalysis[index][1] == 1:
    f.write(wordCountAnalysis[index][0] + ", ")
    index = index - 1


  f.close()
readDocument("romeoAndJuliet")
writeAnalysis("romeoAndJuliet")

