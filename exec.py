import re
import glob
import os

files = [f for f in glob.glob("*.txt")]
outputFolderName = "output"


if not os.path.isdir(outputFolderName):
    os.makedirs(outputFolderName)

def execute(fileName):
    doc = open(fileName, "r")
    outfile = open(outputFolderName + "/" + fileName, "w")

    for line in doc:
        header = re.search(r'\*{3}((?!CONFIDENTIAL|\*).)+\*{3}', line)
        if header:
            indices = header.span()
            beginningOfLine = line[:indices[0]]
            endOfLine = line[indices[1]:]
            delta = indices[1] - indices[0]
            outHeaderLine = beginningOfLine + (" " * delta) + endOfLine
            outfile.write(outHeaderLine)

        digits = re.search(r'^\s?\d+', line)
        if digits:
            endIndex = digits.end()
            remainingLine = line[endIndex:]
            outDigitLine = (" " * endIndex) + remainingLine
            outfile.write(outDigitLine)


        if not digits and not header:
            outfile.write(line)




for i, fileName in enumerate(files):
    execute(fileName)
    print("Completed document: " + fileName)
