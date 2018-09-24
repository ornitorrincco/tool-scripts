import os


# get all the Filenames of the extension of the CWD
def getNames(extension):
    names = []
    for filename in os.listdir('.'):
        if filename.endswith('.' + extension):
            names.append(filename)

    return names
