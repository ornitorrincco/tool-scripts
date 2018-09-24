import imaplib
import base64
email_user = ''
email_pass = ''

M = imaplib.IMAP4_SSL('url', 4040)
# M.login(email_user, email_pass)
# M.select()
#
# typ, data = M.search(None, 'ALL')
