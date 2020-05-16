import ftplib

def main():
    file_name = 'allowances_csnox.zip' #downloading from EPA public FTP site
    file_path='DMDnLoad/allowances'
    host='newftp.epa.gov'
    import_ftp(file_name, file_path, host)

def import_ftp(file_name,file_path, host):
    print(host)
    ftp =  ftplib.FTP(host)
    ftp.login()
    ftp.cwd(file_path)
    gFile = open("DOWNLOAD"+file_name, "wb")
    ftp.retrbinary('RETR %s' % file_name, gFile.write)
    gFile.close()
    ftp.quit()

if __name__ == "__main__":
    main()