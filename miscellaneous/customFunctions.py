import json


def isIn(text, arrayValues):
    if any(word in text for word in arrayValues):
        return True
    else:
        return False

def LoadJSONForAllFunctions():
    fileCodes = open(filenameErrorCodes,'r')
    ErrorCodes = json.load(fileCodes)
    fileCodes.close()
    return ErrorCodes

def CleanSpaces(text):
    text = ' '.join(text.split())


if __name__ == "__main__":
    print('This file is only a Library')
else:
    errorCodes = LoadJSONForAllFunctions()
