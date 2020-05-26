# import getpass
# import telnetlib

# HOST = "http://localhost:8000/"
# user = raw_input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until("login: ")
# tn.write(user + "\n")
# if password:
#     tn.read_until("Password: ")
#     tn.write(password + "\n")

# tn.write("ls\n")
# tn.write("exit\n")

# print tn.read_all()




"""
Retrieve messages from an email inbox
"""
# import poplib

# mailbox = poplib.POP3_SSL('pop.googlemail.com', '995')
# mailbox.user('inglish.contact@gmail.com')
# mailbox.pass_('KendallJenner97170-Jagaciak')
# num_of_messages = len(mailbox.list()[1])
# with open('retrieved_messages.txt', 'w', encoding='utf-8') as f:
#     for i in range(num_of_messages):
#         for msg in mailbox.retr(i + 1):
#             f.write(str(msg))
#             f.write('\n')
#             f.write('\n')
# mailbox.quit()


"""
FTP
"""
# import ftplib

# def get_file(ftp, filename):
#     try:
#         ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write())
#     except:
#         print('Error')

# def store_file(ftp, filename):
#     data = open(filename, 'rb')
#     ftp.storbinary('STOR ' + data, open(filename, 'rb'))

# ftp = ftplib.FTP('ftp.a.b')
# ftp.login('user', 'password')
# # ftp.dir()
# # ftp.cwd('//')
# get_file(ftp, '')
# ftp.quit()

# PROXY SERVER

# import requests

# proxies = {
#     'http': '265.24.11.6:8080'
# }

# response = requests.get('https://www.twitter.com', proxies=proxies)
# print(response.headers)


import redis

client = redis.Redis(host='169.254.55.21', port=6379)
client.set('language', 'Python')
print(client.get('language'))