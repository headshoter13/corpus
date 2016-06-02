import os
import re


def sub_open(path_rar, path_corp):
    if not os.path.exists(path_corp):
        os.makedirs(path_corp)
    for root,dirs,files in os.walk(path_rar):
        for folder in dirs:
            print(folder)######### 
            file = file_corp(path_corp, folder)
            alligns = allign_times('.//Extracted_Data//', folder)
            writing_the_corpus(file, alligns)

         
def allign_times(path_rar, folder):
    alligns = []
    for root,dirs,files in os.walk(path_rar + folder + '//'):
        try:
            for file in files:
                print(file) ######
                sub_file = open(path_rar + folder + '//' + file,  'r').read()
                times = re.findall('\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', sub_file)
                data_times, data_reverse = transform(times)
                vals = [i for i in sorted(list(data_times.values()))]
                vals1 = [i for i in sorted(list(data_times.keys()))]
                allphrases = piece_to_file(data_times, sub_file, times, vals, data_reverse, vals1, file)
                alligns.append(allphrases)
        except:
            continue
    
    return alligns
                    
                    
def file_corp(way, name):
    file = open(way + name + '.xml', 'w', encoding = 'utf-8')
    return file

                        
def transform(times):
    data_times = {}
    data_reverse = {}
    for i in times:
        data_times[i] = i[:2] + '.' + i[3:5] + i[6:13].replace(',','') + i[17:19] + '.' + i[20:22] + i[23:].replace(',', '')
        data_reverse[i[:2] + '.' + i[3:5] + i[6:13].replace(',','') + i[17:19] + '.' + i[20:22] + i[23:].replace(',', '')] = [i]
    return data_times, data_reverse


def piece_to_file(data_times, sub_file, times, vals, data_reverse, vals1, file): 
    limit = 0.0195   #0.02 normally but not everywhere
    allphrases = [file[:-4]]
    length = float(data_times[vals1[-1]].split()[1]) / limit  
    num = 1
    num_zero = 0
    while len(allphrases) < int(length) and num_zero <len(vals) and num < len(vals):
        num, phrases = each_str(allphrases, vals, sub_file, data_times, num, num_zero, vals1, limit, data_reverse)
        allphrases.append(phrases)
        num_zero = num
        num += 1
    
    return allphrases
        

def each_str(allphrases, vals, sub_file, data_times, num, num_zero, vals1, limit, data_reverse):
    phrases = ''
    limit_each = 0
    while limit_each < limit and num_zero <len(vals) and num < len(vals):    
            numb1 = vals[num_zero].split()[1]
            numb2 = vals[num].split()[1]
            x = str(data_reverse[vals[num_zero]][0]) #time-element to find
            x1 = str(data_reverse[vals[num]][0])
            txt = re.findall(x +  '\n(.*?)\n\n', sub_file, flags = re.DOTALL)
            txt1 = re.findall(x1 + '\n(.*?)\n\n', sub_file, flags = re.DOTALL)
            txt[0] = txt[0].replace('\n', '')
            txt1[0] = txt1[0].replace('\n', '')
            
            if txt[0] not in phrases:
                phrases += txt[0]
            limit_each = float(numb2) - float(numb1)
            if limit_each < limit:
                phrases += txt1[0]
                num += 1
            else:
                num += 1
       
    return num, phrases
        
        
def writing_the_corpus(file, alligns):
    alls = [len(i) for i in alligns] 
    file.write('<?xml version="1.0" encoding="utf-8"?>\n<html>\n<head>\n</head>\n<body>\n')
    par_id = 1  # total phrases
    while len(alls) > 0 and par_id != min(alls):
            var_id = 0   #languages
            file.write('  <para id="' + str(par_id - 1) + '">\n')
            for massive in alligns:
                line = re.sub('<.*?>.*<.*?>', '', str(alligns[var_id][par_id]))
                file.write('    <se lang="' + str(alligns[var_id][0]) + '" variant_id="' + str(var_id) + '">' + line + '</se>\n')
                var_id += 1
            file.write('  </para>\n' )
            par_id += 1
    file.write('</body>\n</html>')
    file.close()
    
        
sub_open('.//Extracted_Data//', './/Corpora//')



