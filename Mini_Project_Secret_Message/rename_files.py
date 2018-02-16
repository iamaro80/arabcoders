 # Mini-Project: Secret Message
import os

def rename_files():
    file_list = os.listdir(r'C:\udacity\prank')
    print file_list
    saved_path = os.getcwd()
    working_path = 'C:\udacity\prank'
    os.chdir(working_path)

    for file_name in file_list:
        print 'old name', file_name
        print 'new name', file_name.translate(None,'0123456789')
        os.rename(file_name, file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
    print os.getcwd()

rename_files()
