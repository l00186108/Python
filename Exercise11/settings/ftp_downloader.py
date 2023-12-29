""""
FTP file downloader
Tested with Python >=3.6
By: NMC
    v0.1    
"""
import ftplib
import settings.ftp as settings

# Make the connection
ftp = ftplib.FTP(settings.FTP['URL'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(settings.FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()