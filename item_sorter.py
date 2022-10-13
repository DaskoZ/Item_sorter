import re, pickle, os
from shutil import move

def is_empty(l):
    if not l:
        return 1
    return 0

def create_folders(path):
    doc_path = os.path.join(path, 'Documents')
    sub_folders = ['Documents', 'Images', 'Compressed', 'Excutables', 'Developer', 
    'Web', 'Audio', 'Video', 'DataBase', 'Other', 'Folders']

    for folder in sub_folders:
        os.mkdir(os.path.join(path, folder))

    for folder in ['Docx', 'Sheets', 'PDF']:
        os.mkdir(os.path.join(doc_path, folder))

def item_sorter(moveFrom_path, moveTo_path, folder_name):
    
    if is_empty(os.listdir(moveFrom_path)):
        print('Folder is Empty!\nquiting...')
        quit()

    #   Spliting files and folders
    files = []
    folders = []
    for i in os.listdir(moveFrom_path):
        if os.path.isfile(os.path.join(moveFrom_path, i)):
            files.append(i)
            continue
        folders.append(i)
    
    moveTo_path = os.path.join(moveTo_path, folder_name)
    #   Create folders!
    if not os.path.exists(moveTo_path):
        os.mkdir(moveTo_path)
        create_folders(moveTo_path)
    
    #   Load dictionary of file extensions
    with open('./extensions.pkl', 'rb') as f:
        extensions = pickle.load(f)
    
    #   Moving folders
    for folder in folders:
        move(os.path.join(moveFrom_path, folder), 
            os.path.join(moveTo_path, 'Folders'))

    #   Moving files
    for file in files:
        #   regx return match of file extension in uppercase!
        regx = re.search(r'\.[^.]+$', file).group().upper()
        for extension in extensions.keys():
            if regx in extensions[extension]:
                if extension == 'Documents':
                    moveTo_doc_path = os.path.join(moveTo_path, extension)
                    if regx == '.PDF':
                        move(os.path.join(moveFrom_path, file),
                             os.path.join(moveTo_doc_path, 'PDF'))
                        break
                    elif regx in ['.DOC', '.DOCX', '.EPUB', '.PPT', '.PPTX']:
                        move(os.path.join(moveFrom_path, file),
                             os.path.join(moveTo_doc_path, 'Docx'))
                        break
                    elif regx in ['.CSV', '.XLSX', '.XLS', '.XLSM', '.ODS']:
                        move(os.path.join(moveFrom_path, file),
                             os.path.join(moveTo_doc_path, 'Sheets'))
                        break
                
                move(os.path.join(moveFrom_path, file),
                     os.path.join(moveTo_path, extension))
                break

if __name__ == '__main__':
    item_sorter(moveFrom_path='C:\\Users\\User\Desktop\\folder_to_sort', 
    moveTo_path='D:\\', 
    folder_name='sorted_folder')# D:\sorted_folder