import sys

dictOfWords = {}

def readFile(filename):
    f = open(filename, 'r')
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
        print( key + " " + str(dict[key]))

def print_top(filename):
    redFile = sorted(readFile(filename),key=secondInTuple, reverse = True)
    for key in redFile[:20]:
        print(key + " " + str(dict[key]))

def secondInTuple(tuple):
    return dict[tuple]

def main():
   if ( len(sys.argv) != 3):
       print('Please Enter:\n\nWordCounter.py <--count / --topcount> <filename>')
   sys.exit(1)

   countType = sys.argv[1]
   filename = sys.argv[2]
   if option == '--count':
     print_words(filename)
   elif option == '--topcount':
     print_top(filename)
   else:
     print(countType + " not a valid option. Please choose again.")
     sys.exit(1)

if __name__ == '__main__':
  main()
