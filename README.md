ftpUpdate
=========
A simple program to update multiple files from an FTP server.

Installation
------------
	sudo git clone https://github.com/kodosexe/ftpUpdate

If you want the program to update the files every time at boot, create a custom service:

	sudo nano /lib/systemd/system/ftpUpdate.service

There, enter the following lines

	[Unit]
	Description=ftpUpdate
	After=multi-user.target
	
	[Service]
	Type=idle
	ExecStart=/use/bin/python /home/USERNAME/ftpUpdate/ftpUpdate.py
	
	[Install]
	WantedBy=multi-user.target

Set the permission of the file to 644

	sudo chmod 644 /lib/systemd/system/ftpUpdate.service

Tell systemd to include the new service in its boot routine

	sudo systemctl daemon-reload
	sudo systemctl enable ftpUpdate.service

Next time your Pi boots, the updater should run.
(Tested on a Raspberry Pi Zero W)

Usage
-----
Enter your FTP server domain and credentials into the config.txt file, and add the entire path to each individual file at the end of the document</br>
Example:

	/home/pi/somescript.py
	somescript.py
	/home/pi/yourfolder/anotherscript.py
	anotherscript.py

<b>Note:</b>
Do not edit any lines beginning with '//'

Also
----
This program comes with no guarantee whatsoever, including functionality and security.
Do not transfer any confidential files via this service.
