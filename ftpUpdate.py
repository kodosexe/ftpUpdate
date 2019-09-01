import os
from ftplib import FTP

print("Reading config.txt")

f = open("config.txt", "r")
f1 = f.readlines()

domain = f1[1]
domain = domain[:len(domain)-1]

user = f1[3]
user = user[:len(user)-1]

password = f1[5]
password = password[:len(password)-1]

folder = f1[7]
folder = folder[:len(folder)-1]

print("Connecting to " + domain + " with user " + user)
print("Read file successfully, logging in")

ftp = FTP(domain, user, password)
ftp.login

print("Login successful, changing directory to " + folder)
ftp.cwd(folder)

print("Directory found, updating files")

for x in range(9, len(f1)-1, 2):
	local_filename=f1[x]
	local_filename=local_filename[:len(local_filename)-1]
	
	filename=f1[x+1]
	filename=filename[:len(filename)-1]
	
	print("Updating file " + filename + " at " + local_filename)
	
	lf = open(local_filename, "wb")
	ftp.retrbinary("RETR " + filename, lf.write, 8*1024)

	lf.close
	
print("Done. Stay Classy, San Diego.")
