# Transposition File Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import sys, time, os, sys, detectEnglish, itertools, math

inputFilename = 'encrypted.txt'
outputFilename = 'decrypted.txt'
blockSize = 0
maximum = 0.0
maxkey = []

def main():
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting.' % (inputFilename))
        sys.exit()

    inputFile = open(inputFilename)
    content = inputFile.read()
    inputFile.close()
    print('Enter block size:')
    blockSize = int(input('> '))
    print(blockSize)

    brokenMessage = hackTransposition(content, blockSize)
    

    if brokenMessage != None:
        print('Writing decrypted text to %s.' % (outputFilename))

        outputFile = open(outputFilename, 'w')
        outputFile.write(brokenMessage)
        outputFile.close()
    else:
        print('Failed to hack encryption.')
        print(maximum)
        print(maxkey)

# based on #http://www.crypto-it.net/eng/simple/columnar-transposition.html
def decrypt(message, keyTuple, row=False):
  matrix = createDecrMatrix(getKeywordSequence(keyTuple), message) if row else createDecrRowMatrix(getKeywordSequence(keyTuple), message)
  plaintext = ""
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext

# based on #http://www.crypto-it.net/eng/simple/columnar-transposition.html
def createDecrMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = int(math.ceil(len(message) / width))
  if height * width < len(message):
    height += 1
  matrix = createEmptyMatrix(width, height)
  pos = 0
  for num in range(len(keywordSequence)):
    column = keywordSequence.index(num+1)
    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1
      print(matrix)
  return matrix

#rewritten for row in row out
def createDecrRowMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = int(len(message) / width)
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height)
  pos = 0
  for row in range(len(matrix)):
    for column in range(len(keywordSequence)):
      matrix[row][keywordSequence[column]-1] = message[pos]
      pos += 1
      if len(message) == pos:
        break
  return matrix


def createEmptyMatrix(width, height):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      matrix[r].append('')
  return matrix


def getKeywordSequence(tup):
  return list(tup) 


# The hackTransposition() function's code was copy/pasted from
# transpositionHacker.py and had some modifications made.
def hackTransposition(message, blockSize):
    print('Hacking...')
    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    keys = list(itertools.permutations(list(range(1,blockSize+1))))
    for key in range(0,  math.factorial(blockSize)):
        print('Trying key #%s... ' % (key), end='')
        print(getKeywordSequence(keys[key]))
        sys.stdout.flush()

        # We want to track the amount of time it takes to test a single key,
        # so we record the time in startTime.
        startTime = time.time()

        decryptedText = decrypt(message,keys[key])
        englishPercentage = round(detectEnglish.getEnglishCount(decryptedText) * 100, 2)

        totalTime = round(time.time() - startTime, 3)
        print('Test time: %s seconds, ' % (totalTime), end='')
        sys.stdout.flush() # flush printed text to the screen
        global maximum 
        global maxkey 
        if englishPercentage > maximum:
            maximum = englishPercentage
            maxkey = keys[key]
        print('Percent English: %s%%' % (englishPercentage))
        if englishPercentage > 20:
            print()
            print('Key #' + str(key) + ': ' + decryptedText[:100])
            print()
            print('Key', keys[key] )
            print()
            print('Enter D for done, or just press Enter to continue:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If transpositionFileHacker.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()


