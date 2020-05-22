import ftplib
import os
def main():
    file_name = 'transaction_csnox.zip' #downloading from EPA public FTP site
    file_path='DMDnLoad/allowances'
    host='newftp.epa.gov'
    ftp_as_zip(file_name, file_path, host)

def ftp_as_zip(file_name,file_path, host, data_location = 'data'):
    print("connecting to: ", host)
    ftp =  ftplib.FTP(host)
    ftp.login()
    ftp.cwd(file_path)
    print("data will be dumped to: " + data_location)
    if not os.path.exists(data_location):
        os.makedirs(data_location)
    print("writing file: "+file_name)
    with open(os.path.join(data_location,file_name), "wb") as gFile:
        ftp.retrbinary('RETR %s' % file_name, gFile.write)
        ftp.quit()

#Most of the AMPD data I am working with I know will be CSV
# def ftp_as_csv(file_name,file_path, host):
#     print("connecting to: ", host)
#     ftp =  ftplib.FTP(host)
#     ftp.login()
#     ftp.cwd(file_path)
#     print("opening file: "+file_name)
#     mem_data = BytesIO()



if __name__ == "__main__":
    main()