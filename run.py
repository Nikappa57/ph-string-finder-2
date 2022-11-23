import os
import time

from script.stringfinder import StringFinder

def main():
    start_time = time.time()
    legit_file = [os.path.join('legit') + file for file in os.listdir('legit') if '.txt' in file]
    unlegit_file = [os.path.join('unlegit') + file for file in os.listdir('unlegit') if '.txt' in file]

    print(legit_file)
    print(unlegit_file)
    sf = StringFinder(legit=legit_file, unlegit=unlegit_file, length=1)

    sf.readFile()
    
    with open("result.txt", "w") as f:
        f.write("\n".join(sf.compare()))
    
    end_time = time.time()

    print("FINISHED IN {} seconds".format(end_time-start_time))
    input()

if __name__ == "__main__":
    main()
