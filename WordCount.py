#WordCount.py
#Name: Aurora Gunubu
#Date: 
#Assignment:

def main():
  textFile = open("beemovie.txt", 'r')
  lineCount = 0
  wordCount = 0 
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1

    letterCount = letterCount + len(line)

  #print(line)
  print("Lines:" , lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
if __name__ == '__main__':
  main()
