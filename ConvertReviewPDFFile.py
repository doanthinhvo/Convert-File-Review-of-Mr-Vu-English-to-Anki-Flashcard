!pip install PyPDF2
####### 
from PyPDF2 import PdfFileReader

# pdfReader = PdfFileReader(open(pdf_path, "rb"))
# text=''

def removeNewLineCharacter(string):
    if "\n" in string:
        string = string.replace("\n", "")
    return string
def replaceComma(string):
    if "," in string:
        string = string.replace(",", "commax")
    return string

for i in range(22, 23):    
    readFileName = f'NGONG - Session {i} - Review.pdf'
    # NGONG - Session 12 - Review
    writeFileName = f'NGONG S{i}.txt'

    pdfReader = PdfFileReader(open(readFileName, "rb"))
    text=''

    # read each page to remove REVIEW word at the begining of each page.
    for i in range(1, pdfReader.numPages): # start from page 1 because page 0 is cover that don't contains learned structure.
        page = pdfReader.getPage(i)
        context = page.extractText().strip()
        context = context[:-1]
	# remove the REVIEW word.
        context = context.replace("REVIEW", "")
        text = text+context.strip()
        

    # print(writeFileName)
    # print(text)
    # after this for loop, text will contain all the content needed.

    word1=''
    meaning=''
    # create a new dictionary
    wordDict = {}

    # create a new list of possition of "•"
    position1 = []


    # search the positions of all "•"
    for i in range(0, len(text)):
        if text[i] == '•':
            position1.append(i)



    currentMeaningandWord = ''
    # get current meaning and word 
    for i in range(0, len(position1)):
        if i == len(position1)-1:
            currentMeaningandWord = text[position1[i]+1:len(text)]
        else:
            currentMeaningandWord = text[position1[i]+1:position1[i+1]]

        # get the position of the first "-" occurrence
        position2 = currentMeaningandWord.find("–")
        # get the meaning 
        meaning = currentMeaningandWord[0:position2]
        # get the word
        word1 = currentMeaningandWord[position2+1:len(currentMeaningandWord)]
        # add the word and meaning to the dictionary
        # print(meaning)
        wordDict[removeNewLineCharacter(word1)] = removeNewLineCharacter(meaning.strip())

    # print(writeFileName)
    # print(wordDict)
    # print(wordDict)
    # print("\n=====================================")

    # with open(write_file, 'w') as f:
    #     f.write(text)

    with open(writeFileName, 'w') as f:
        for key in wordDict.keys():
            f.write("%s: %s\n"%(key,wordDict[key]))
