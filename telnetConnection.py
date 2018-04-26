import sys
import telnetlib


def Enter(tn):
    tn.write(b'\r')

def EnterInCmd(tn):
    tn.write(b'\n')

def Down(tn):
    tn.write(b'\x1b[B')

def F1(tn):
    tn.write(b'\x1bOP')




HOST = b'localHost'
user = b'usuario'
password = b'password'
tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(1000)
tn.read_until(b'Enter your user id:')
tn.write(user)
tn.write(b'\n')
tn.read_until(b'user password:')
tn.write(password)
tn.write(b'\n')
tn.read_until(b'.Q             \x1b[0m\x1b[3;2H')
