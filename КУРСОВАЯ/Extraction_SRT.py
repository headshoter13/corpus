import os, zipfile
import re
import os


def extraction():
    meta_info = open('MetaInfo.csv', 'w')
    for root,dirs,files in os.walk('.//subs'):
        for folder in dirs:
            meta_info.write('\n' + folder.replace('-',' ') + ';')
            if not os.path.exists('.//Extracted_Data//' + folder):
                os.makedirs('.//Extracted_Data//' + folder)
            for root,dirs,files in os.walk('.//subs//' + folder + '//'):
                for file in files:
                    zip_F = zipfile.ZipFile('.//subs//' + folder + '//' + file, 'r')
                    archieve_files = list(zip_F.namelist())
                    if len(archieve_files) <= 2:
                        for sub in archieve_files:
                            if sub[-3:] == 'srt':
                                
                                data = zip_F.read(sub)
                                output = open('.//Extracted_Data//' + folder + '//' + zip_F.filename[-6:-4] + ".srt",'wb') #exporting to given location one by one
                                output.write(data)
                                meta_info.write(zip_F.filename[-6:-4]+ ';')
                                output.close()
    meta_info.close()
                                
                        

extraction()
