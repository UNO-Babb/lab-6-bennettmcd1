#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
    textFile = open("fish.txt", 'r')
  
    words = {}

    print("fish" in words)
    words["fish"] = [2]
    print("fish" in words)
    words["fish"].append(5)
    print(words)
    
    for line_number, line in enumerate(textFile, start=1):
        for word in line.split():
            word = word.lower().strip()
            if word in words:
                words[word].append(line_number)
            else:
                words[word] = [line_number]
    
    textFile.close()
    
    print("\nWord Index:")
    for word, line_numbers in sorted(words.items()):
        print(f"{word}: {line_numbers}")


if __name__ == '__main__':
    main()

