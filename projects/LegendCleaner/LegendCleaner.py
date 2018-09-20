import configparser
import os
import re
import datetime

fileName = 'config.ini'
root = 'd:\\'
keep_days = 7
filters = ['\.([0-9]){4}-([0-9]){2}-([0-9]){2}','\.([0-9]){8}-([0-9]){6}\.([0-9]){1,5}']
cleanDir = ['crash', 'profile'] # 소문자로 입력해서 비교

def CheckAndRemoveByDate(fullname):
    current = datetime.datetime.now() - datetime.timedelta(days=keep_days)       
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
    if (filetime < current):        
        try:
            os.remove(fullname)
            print('Delete ' + fullname)
        except PermissionError:
            print('PermissionError ' + fullname)

def CheckRegexFile(fullname):
    for filter in filters:
        basename = os.path.basename(fullname)
        regex = re.compile( filter)    
        match = regex.search(basename)
        if match != None:
            return True    
    return False

# 해당 디렉토리의 오래된 파일들을 삭제한다.
def CleanOutdatedFiles(targetDir, useFilter):
    try:
        filenames = os.listdir(targetDir)
        for filename in filenames:
            full_filename = os.path.join(targetDir, filename)
            if useFilter == True:
                # 정규 표현식 필터 확인 대상
                if os.path.isdir(full_filename):
                    CleanOutdatedFiles(full_filename, not (filename.lower() in cleanDir))
                else:
                    if CheckRegexFile( full_filename ):
                        CheckAndRemoveByDate(full_filename)
            else:
                # 모든 파일 대상 
                if os.path.isdir(full_filename):
                    CleanOutdatedFiles(full_filename, False)                    
                else:
                    CheckAndRemoveByDate(full_filename)
    except PermissionError:
        pass

def makeSampleConfig(pathdir, folders):    
    config = configparser.ConfigParser()
    config.read(fileName)    
    config.set(config.default_section, 'ROOT', root)
    for ext in filters:
        config.set(config.default_section, 'EXTEND', ext)

    configfile = open(filename, 'w')
    config.write(configfile)

if __name__ == "__main__":
    # 셋팅 파일 저장
    # if(os.path.exists(os.path.join(os.getcwd(),fileName))==False):
    #     makeSampleConfig()        

    CleanOutdatedFiles(os.getcwd(), True)
    # input('press any key ...')
    #config = configparser.ConfigParser()
    #config.read("config.ini")

