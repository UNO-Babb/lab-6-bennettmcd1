#WordCount.py
#Name: Bennett McDonald   
#Date: 3/2/25
#Assignment: word counter 

def main():
    file_name = input("Enter a File Name: ")
    try:
        textFile = open(file_name, 'r')
      
        line_count = 0
        word_count = 0
        char_count = 0

        for line in textFile:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

        textFile.close()
        
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
    
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except IOError:
        print(f"An error occurred while trying to read the file.")

if __name__ == '__main__':
    main()

