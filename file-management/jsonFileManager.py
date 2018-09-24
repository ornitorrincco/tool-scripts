import json

#this can not handle multiple +1 index to upload content

filename = 'C:\\log.json'
filenameError = 'C:\\logError.json'


def UpdateJsonFile(index,contentUpload):
    try:
        if not os.path.exists(filename):
            payload = {
              'Key1': {},
              'key2': {},
              'key3': {}
            }
            with open(filename, "w") as jsonFile:
                jsonFile.write(json.dumps(payload,sort_keys=True, indent=4))
                jsonFile.close()
        with open(filename, "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            numberOfTransaction = str(len(data[index]))
            payload = {numberOfTransaction : {}}
            payload[numberOfTransaction].update(transaction)
            data[index].update(payload)
        with open(filename, "w") as jsonFile:
            jsonFile.write(json.dumps(data,sort_keys=True, indent=4))
            jsonFile.close()
    except:
        with open(filenameError, "w") as jsonFileError:
            jsonFileError.write('\n\n')
            jsonFileError.write('Posible Bad Index Error for Payload: '+ index + '\n')
            jsonFileError.write('Posible Bad Transaction Error for Payload: '+ json.dumps(transaction))
            jsonFileError.close()
