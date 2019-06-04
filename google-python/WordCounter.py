import sys

dictOfWords = {}

def readFile(filename):
    f = open(filename, 'rU')
    for line in f:
        words = line.split()
        for word in words:
            word = word.lower()
            if(word in dictOfWords.keys()):
                dictOfWords[word] += 1
            else:
                dictOfWords[word] = 1
    f.close()
    return dictOfWords

def print_words(filename):
    redFile = sorted(readFile(filename))
    for key in redFile:
        print( key + " " + str(dictOfWords[key]))

def print_top(filename):
    redFile = sorted(readFile(filename),key=secondInTuple, reverse = True)
    for key in redFile[:20]:
        print(key + " " + str(dictOfWords[key]))

def secondInTuple(tuple):
    return dictOfWords[tuple]


def main():
    if ( len(sys.argv) != 3):
       print('\n\nPlease Enter:\nWordCounter.py <--count / --topcount> <filename>')
       sys.exit(1)

    countType = sys.argv[1]
    filename = sys.argv[2]
    print(countType, filename)
    if countType == '--count':
         print_words(filename)
    elif countType == '--topcount':
         print_top(filename)
    else:
         print(countType + " not a valid option. Please choose again.")
         sys.exit(1)



if __name__ == '__main__':
    main()
