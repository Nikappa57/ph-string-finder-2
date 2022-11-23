import re
import concurrent.futures

class StringFinder:
    def __init__(self, unlegit:list, legit:list, length:int):
        self.unlegit_files = unlegit
        self.legit_files = legit
        self.length = length

    def readFile(self):
        self.legit = set()
        self.unlegit = set()

        with concurrent.futures.ThreadPoolExecutor(8) as executor:
            for file in self.legit_files:
                executor.submit(self.readFileLegit, file)
        
        for file in self.unlegit_files:
                self.readFileUnlegit(file)

    def readFileUnlegit(self, file):
        print("start reading ", file)
        with open(file) as f:
            self.unlegit = self.unlegit.intersection(
                set(map(self.line_adapter, f.read().splitlines()))) if self.unlegit \
                    else set(map(self.line_adapter, f.read().splitlines()))
        print("end of the reading ", file)
    
    def readFileLegit(self, file):
        print("start reading ", file)
        with open(file) as f:
            self.legit.update(
                set(map(self.line_adapter, set(f.read().splitlines()))))
        print("end of the reading ", file)

    def compare(self) -> set:
        return set(self.unlegit) - set(self.legit)

    @staticmethod
    def line_adapter(line:str) -> str:
        pattern = "(0x.+) (\([0-9]*\)): (.*)"
        check = re.search(pattern, line)
        line = check.group(3) if check else line
        return line

