import configparser
import os
import re
import time
import datetime

fileName = 'config.ini'
root = 'd:\\'
keep_days = 7
filters = ['\.([0-9]){4}-([0-9]){2}-([0-9]){2}','\.([0-9]){8}-([0-9]){6}\.([0-9]){1,5}']
cleanDir = ['Crash', 'profile']

def checkRemove(fullname, filter):
    basename = os.path.basename(fullname)
    regex = re.compile( filter)    
    match = regex.search(basename)
    if( match == None ):
        return False
    else :
        # 파일이 수정된 날짜가 keep_days 보다 이전인 데이터는 삭제한다.
        current = datetime.datetime.now() - datetime.timedelta(days=keep_days)       
        filetime = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))

        #print ((time.ctime(os.path.getmtime(fullname)))
        #print (filetime +'<'+ current)
        print (filetime < current)
        return (filetime < current)


def makeSampleConfig(pathdir, polders):    
    config = configparser.ConfigParser()
    config.read(fileName)    
    config.set(config.default_section, 'ROOT', root)
    for ext in filters:
        config.set(config.default_section, 'EXTEND', ext)

    configfile = open(filename, 'w')
    config.write(configfile)

def CleanSubPath(basePath):
    # for entry in os.listdir(os.path.dirname(basePath)):
    #     if( entry.is_dir() ):
    #         print(entry)
    try:
        filenames = os.listdir(basePath)
        for filename in filenames:
            full_filename = os.path.join(basePath, filename)
            if os.path.isdir(full_filename):                
                if filename in cleanDir:
                    print('remove dir : ' + full_filename)
                else:                
                    CleanSubPath(full_filename)
            else:
                for ff in filters:
                    if( checkRemove(full_filename, ff) == True ):
                        print(full_filename)
    except PermissionError:
        pass
        # if( entry.is_dir() ):   
        #     print (entry.name)                 
        #     CleanSubPath(os.path.join(basePath,entry.name), fileExts)                
        # else:
        #     CleanFile(os.path.join(basePath,entry.name), fileExts)


if __name__ == "__main__":
    # 셋팅 파일 저장
    # if(os.path.exists(os.path.join(os.getcwd(),fileName))==False):
    #     makeSampleConfig()        

    CleanSubPath(os.getcwd())
    # input('press any key ...')
    #config = configparser.ConfigParser()
    #config.read("config.ini")

