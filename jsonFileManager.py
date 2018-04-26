import json

#this can not handle multiple +1 index to upload content

filenameError = 'C:\\log.json'
filenameError = 'C:\\logError.json'


def UpdateJsonFile(index,contentUpload):
    try:
        if not os.path.exists(filename):
            payload = {
              'Key1': {},
              'key2': {},
              'key3': {}
            }
            jsonFile = open(filename, "w")
            jsonFile.write(json.dumps(payload,sort_keys=True, indent=4))
            jsonFile.close()
        jsonFile = open(filename, "r")
        data = json.load(jsonFile)
        jsonFile.close()
        data[index].update(contentUpload)
        jsonFile = open(filename, "w")
        jsonFile.write(json.dumps(data,sort_keys=True, indent=4))
        jsonFile.close()
    except:
        jsonFile = open(filenameError, "w")
        jsonFile.write('Posible Bad Index Error for Payload: '+ index + '\n')
        jsonFile.write('Posible Bad Try Error for Payload: '+ json.dumps(contentUpload))
        jsonFile.close()
