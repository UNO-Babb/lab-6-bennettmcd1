#WordCount.py
#Name: Bennett McDonald   
#Date: 3/2/25
#Assignment: word counter 

def main():
    textFile = open("gettysberg.txt", 'r')
  
    for line in textFile:
        print(line)
    
    textFile.seek(0)
    line_count = 0
    word_count = 0
    char_count = 0

    for line in textFile:
        line_count += 1
        word_count += len(line.split())

