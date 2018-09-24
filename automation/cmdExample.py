import subprocess

cmd = 'python script.py value1'

try:
    p = subprocess.call(cmd,shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    for line in result:
        if not line.startswith('#'):
            print(line)
except Exception as error:
    print(error)
