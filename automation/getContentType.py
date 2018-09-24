def getExtention(filename,Host):
    try:
        response = requests.get(host)
        type = str(response.headers['Content-Type'])
        extention = ''
        if type == 'audio/aac':
            extention = '.aac'
        elif type ==  'video/x-msvideo':
            extention = '.avi'
        elif type == 'application/octet-stream':
            extention = '.bin'
        elif type == 'application/x-bzip':
            extention = '.bz'
        elif type == 'application/x-bzip2':
            extention = '.bz2'
        elif type == 'application/x-csh':
            extention = '.csh'
        elif type == 'text/css':
            extention = '.css'
        elif type == 'text/csv':
            extention = '.csv'
        elif type == 'application/msword':
            extention = '.doc'
        elif type == 'application/epub+zip':
            extention = '.epub'
        elif type == 'image/gif':
            extention = '.gif'
        elif type == 'text/html':
            extention = '.html'
        elif type == 'image/x-icon':
            extention = '.ico'
        elif type == 'application/java-archive':
            extention = '.jar'
        elif type == 'image/jpeg':
            extention = '.jpeg'
        elif type == 'application/javascript':
            extention = '.js'
        elif type == 'video/mpeg':
            extention = '.mpeg'
        elif type == 'application/pdf':
            extention = '.pdf'
        elif type == 'application/vnd.ms-powerpoint':
            extention = '.ppt'
        elif type == 'application/x-rar-compressed':
            extention = '.rar'
        elif type == 'application/rtf':
            extention = '.rtf'
        elif type == 'application/x-sh':
            extention = '.sh'
        elif type == 'image/svg+xml':
            extention = '.svg'
        elif type == 'application/x-shockwave-flash':
            extention = '.swf'
        elif type == 'application/x-tar':
            extention = '.tar'
        elif type == 'image/tiff':
            extention = '.tiff'
        elif type == 'application/vnd.visio':
            extention = '.vsd'
        elif type == 'audio/x-wav':
            extention = '.wav'
        elif type == 'audio/webm':
            extention = '.weba'
        elif type == 'video/webm':
            extention = '.webm'
        elif type == 'image/webp':
            extention = '.webp'
        elif type == ' 	application/xhtml+xml':
            extention = '.xhtml'
        elif type == 'application/vnd.ms-excel':
            extention = '.xls'
        elif type == 'application/xml':
            extention = '.xml'
        elif type == 'application/zip':
            extention = '.zip'
            
        if extention != '':
            return 'Bad Content type'
        else:
            return extention
    except:
        print('Problem with: ' + fileName)
