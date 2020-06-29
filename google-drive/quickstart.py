from __future__ import print_function
import pickle
import os.path
import os 
from datetime import datetime
import glob
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import gdown
from videos.utils import *

__version__ = "0.0.2"
__status__ = "Under development"


# If modifying these scopes, delete the file token.pickle.

# Reference:
# https://medium.com/@annissouames99/how-to-upload-files-automatically-to-drive-with-python-ee19bb13dda
# https://www.youtube.com/watch?v=9OYYgJUAw-w
# https://github.com/gsuitedevs/PyDrive


class initGD:
    MIMETYPES = {
            # Drive Document files as MS dox
            'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            # Drive Sheets files as MS Excel files.
            'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            # Drive presentation as MS pptx
            'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
            # see https://developers.google.com/drive/v3/web/mime-types
        }
    EXTENSTIONS = {
            'application/vnd.google-apps.document': '.docx',
            'application/vnd.google-apps.spreadsheet': '.xlsx',
            'application/vnd.google-apps.presentation': '.pptx'
    }
    def __init__(self):
        g_login = GoogleAuth()
        # Try to load saved client credentials
        g_login.LoadCredentialsFile("mycreds.txt")
        print (f" GLOGIN: {g_login.credentials}")
        if g_login.credentials is None:
            # Authenticate if they're not there
            g_login.LocalWebserverAuth()
        elif g_login.access_token_expired:
            # Refresh them if expired
            g_login.Refresh()
        else:
            # Initialize the saved creds
            g_login.Authorize()
        # Save the current credentials to a file
        g_login.SaveCredentialsFile("mycreds.txt")
        self.drive = GoogleDrive(g_login)
        print ("[*] Set up account sucessfully !!!")
    

    def upload_one_file(self,file_path):
        '''
            Upload one file 
        '''

        # file_path = "./test1.jpg"
        # with open(file_path,"r") as file:
        #     # do something here with file
        #     print (os.path.basename(file.name))
        #     file_drive = self.drive.CreateFile({'title':os.path.basename(file.name) }) 
        #     file_drive.SetContentString(os.path.basename(file.name)) 
        #     file_drive.Upload()
        # print ("[*] Uploaded file sucessfully!")

        file_path = file_path
        file1 = self.drive.CreateFile()
        file1.SetContentFile(file_path)
        file1.Upload()
        print('Created file %s with mimeType %s' % (file1['title'],file1['mimeType']))

    def create_folderGD(self,folder_name,id = None):
        '''
            Create a folder on Google drive
            If ID = None -> create in the root folder
            Otherwise, it'll create the folder inside your target folder

            Return:
                Folder Name, Folder ID 
        '''
        self.folder_name  = folder_name
        self.id = id

        if self.id == None:
            file1 = self.drive.CreateFile({'title': self.folder_name, 
                "mimeType": "application/vnd.google-apps.folder"})
            file1.Upload()

        else:
            file1 = self.drive.CreateFile({'title': self.folder_name, 
                "parents":  [{"id": self.id}], 
                "mimeType": "application/vnd.google-apps.folder"})
            file1.Upload()

        return file1['title'],file1['id']

    def upload_many_files(self,folder,id = None):
        '''
            Upload many files in a folder
            Input:
                folder: Your local folder path
            Return:
    
        '''
        self.folder_path = folder
        self.id = id

        folder_name = self.folder_path.split("/")[-1]
        folder_name, folder_id = self.create_folderGD(folder_name)

        if self.id == None:
            target_id = folder_id
        else:
            target_id = self.id

        # Upload only files 
        if os.listdir(self.folder_path):
            for file in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path,file)):
                    # file_path = file
                    # fix erroe
                    file_path = os.path.join(self.folder_path,file)
                    file1 = self.drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": target_id}]})
                    file1.SetContentFile(file_path)
                    file1.Upload()
                    
        print ("Uploaded file succesfully...")

    def upload_folder(self):
        '''
            Upload a folder to GGDrive
            1/ Create a folder
            2/ Upload all the files in that folder to GGDrive
        '''
        # 1/ Create folder.
        folder_metadata = {
            'title' : 'docs',
            # The mimetype defines this new file as a folder, so don't change this.
            'mimeType' : 'application/vnd.google-apps.folder'
        }
        folder = self.drive.CreateFile(folder_metadata)
        folder.Upload()

        # Get folder info and print to screen.
        folder_title = folder['title']
        folder_id = folder['id']
        print('title: %s, id: %s' % (folder_title, folder_id))


        # 2/ Upload all the files in that folder to GGDrive

        # Upload file to folder.
        f = self.drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}]})

        # Make sure to add the path to the file to upload below.
        f.SetContentFile('docs/eng.txt')
        f['title'] = 'eng.txt'
        f.Upload()

    def search_folder_name(self,folder_name,root):
        '''
            Get a list of files, search from name of files
            Input:
                name: Name of folder
            Return: 
                 files_in_folder: (list) file
        '''

        self.folder_name = folder_name

        # 1. Get list files
        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        file_name = [file['title'] for file in file_list]
        file_id   = [file['id'] for file in file_list]

        # 2. Get the folder id -> list all files in that folder
        folder_id    =  file_id[file_name.index(self.folder_name)] # return the idd of folder
        list_files = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()

        return list_files

    def search_folder_id(self,id):
        '''
           Get a list of files, search from folder ID
        '''
        list_file = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(self.id)}).GetList()
        list_name = [file['title'] for file in list_file]
        list_id   = [file['id'] for file in list_file]
        return list_file,list_name,list_id

    def create_folder(self,name):
        '''
            Create folder based on its name
            Input: 
                (str) name: Name of folder
            Return:
                None
        '''
        self.name = name
        try:
            # Create target Directory
            os.mkdir(self.name)
            print("Directory " , self.name ,  " Created ") 
        except FileExistsError:
            print("Directory " , self.name ,  " already exists")

    def escape_fname(self,name):
        self.name = name
        return self.name.replace('/','_')

    def download_folder_id(self,id,dst_path):
        '''
            Download folder based on its ID 
            Input: 
                id: (str) ID of folder
            Return: 
                list_files: (list) Object List 
        '''

        self.id = id
        self.dst_path = dst_path

        list_files,list_names,list_ids = self.search_folder_id(self.id)
        self.create_folder(self.dst_path)

        print ("[*] Folder ID:",self.id)
        print ('[*] Found: {} files.'.format(len(list_names)))
        print ("----------------------------------------------------------------------------")
        for f in list_files:
            print('-> Title: {}, Id: {}'.format(f['title'], f['id']))
        print ("----------------------------------------------------------------------------") 

        root = self.dst_path

        # Download all the files
        for i, file1 in enumerate(sorted(list_files, key = lambda x: x['title'])):
            # Download folder
            if file1['mimeType'].split('.')[-1] == 'folder':
                print ('tile {}, id: {}'.format(file1['title'],file1['id']))
                print (os.path.join(root,file1['title']))
                self.download_folder_id(file1['id'],os.path.join(root,file1['title']))
            # Download files
            else:
                download_mimetype = None
                file_name = self.escape_fname(file1['title'])
                file_name = '{}/{}'.format(self.dst_path,file_name)
                print ('[*] Filename:',file_name)
                try:
                    # print('Downloading {} from GDrive ({}/{})'.format(file1['title'], i, len(files)))
                    print ('--> Downloading:',file_name)
                    if file1['mimeType'] in self.MIMETYPES:
                        download_mimetype = self.MIMETYPES[file1['mimeType']]
                        file1.GetContentFile(file_name+self.EXTENSTIONS[file1['mimeType']], mimetype=download_mimetype)
                    else:
                        file1.GetContentFile(file_name)
                except:
                    print ('Failed')
        print ("Finished downloading !")
    def list_pagination(self):

        '''
            PyDrive handles file listing pagination for you.
        '''
        # Auto-iterate through all files that matches this query
        file_list = self.drive.ListFile({'q': "'root' in parents"}).GetList()
        print (type(file_list))
        print (len(file_list))
        for file1 in file_list:
            print('title: {}, id: {}'.format(file1['title'], file1['id']))

        # # Paginate file lists by specifying number of max results
        # for file_list in self.drive.ListFile({'maxResults': 10}):
        #     print('Received {} files from Files.list()'.format(len(file_list))) # <= 10
        #     for file1 in file_list:
        #         print('title: {}, id: {}'.format(file1['title'], file1['id']))
    def search_files(self):
        pass
    def return_fields(sel):
        pass
    def manage_metadata(self):
        pass
    def handle_error(self):
        pass



if __name__ == '__main__':
    # Init the Drive
    drive = initGD()

    ''' Download file '''
    dst_path = './temp_videos'

    ids = ['1EzNM4msxeGWjwHhbQVxlGJjD9GrtNRN2',
            '1Q7RqlrG7iLpcWeJKUho04quuxzoPBkF3',
            '1W20D2ufNqD4DvzUS-pwnAAIfR8G-NZsj',
            '1I0b3iH1HHfGRMOpIKb7vDyMr8ZU9V-KK',
            '1qgWoGOOrgtmAy5Fd2nzFsFgSr6EOktv0',
            '19wzTAL_XrSDTNJz4mg0Qj6KFQT5No97y',
            '1k8pBCm0cibJXtYQX3U6pqesIS2X5y1ac']

    for index,folder_id in enumerate(ids):
        mkdir(index)
        if index == 3:
           output_folder = os.path.join(dst_path,str(index))
           drive.download_folder_id(folder_id,output_folder)



    ''' Upload File '''
    # drive.upload_many_files(folder='/mnt/49418012-cfa6-4af1-86d8-c0fb55ae6501/[Tools]Addons/download_google_drive')

    # Upload one file 
    # drive.upload_one_file('/mnt/49418012-cfa6-4af1-86d8-c0fb55ae6501/[Tools]Addons/download_google_drive/client_secrets_m10607812.json')
    # drive.create_folderGD('hungdeptrai','1pnEQYWIILLornKVrMHON38ygrsgx7RYn')
    # drive.upload_many_files('drive_download','1pnEQYWIILLornKVrMHON38ygrsgx7RYn')