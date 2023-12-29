"""
main.py
By: NMC
Date: 20OCT23
"""

from Source.directory_utilities import detect_os, detect_working_directory

from mypath import UDP_SETTINGS as udp_settings
print(udp_settings)

print(detect_os())
print(detect_working_directory())  