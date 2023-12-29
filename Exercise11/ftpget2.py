'''
Script: ftpget2.py
By: NMC
Purpose: File Transfer Protocol
Date: 26OCT23
'''
import ftplib

FTP = {
    "PATH": '/mirrors/ubuntu-cdimage/releases/22.04/release',
    "FILENAME": 'SHA256SUMS',
    "URL": 'ftp.heanet.ie'
}

# Make the connection
ftp = ftplib.FTP(FTP['URL'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()