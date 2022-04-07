from ftplib import FTP
from shutil import unpack_archive

CIMIS_WIND_FTP = 'ftp.cimis.water.ca.gov'
CIMIS_FILE_PREFIX = 'dailyStns{year}'

# connects to ftp server
ftp = FTP(CIMIS_WIND_FTP)
ftp.login()
ftp.cwd('pub2/annual')


# writes file from ftp to local
with open('data/cimis_2020.zip', 'wb') as fp:
    ftp.retrbinary('RETR dailyStns2020.zip', fp.write)

unpack_archive('data/cimis_2020.zip', 'data/cimis_2020')
