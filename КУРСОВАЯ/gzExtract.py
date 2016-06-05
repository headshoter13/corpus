import tarfile
import os
import re
import gzip

def extract_first(info, path, reg_exp):
    export_data = open(info, 'r').read()
    names = set(re.findall('srt	(.*?)	', export_data))
    for name in names:
        try:
            langs_d = {}
            langs = re.findall(reg_exp + name, export_data)
            for elem in langs:
                    if elem[1] not in langs_d:
                        langs_d[elem[1]] = elem[0]
            name = str(name).replace(':*:;!@#%^&','')           
            if not os.path.exists(path + name):
                os.makedirs(path + name)
        except:
            continue
        exract_second(langs_d, './/files//', name)

        
def extract_second(langs_d, path, name):   
    for i in langs_d:
        try:
            q = langs_d[i][-1]
            w = langs_d[i][-2]
            e = langs_d[i][-3]
            r = langs_d[i][-4]
            path = path + str(q) + '//' + str(w) + '/' + str(e)+ '//' + str(r) + '//' + str(langs_d[i]) + '.gz'
            with gzip.open(path) as f, open('.//subs//' + str(name) + '//' + str(i) + '.srt', 'wb') as fout:
                file_content = f.read()
                fout.write(file_content)
                fout.close()
        except:
            continue

extract_first('export.txt', './/subs//', '\d+	(\d+)	(\w*3?)	\d+	\d	\d	srt	')
    
        
