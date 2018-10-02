import configparser
import os
import re
import datetime
import pprint

fileName = 'config.ini'
root = '.'
keep_days = 7
filters = ['\.([0-9]){4}-([0-9]){2}-([0-9]){2}','\.([0-9]){8}-([0-9]){6}\.([0-9]){1,5}']
folders = ['crash', 'profile'] # 소문자로 입력해서 비교
logFile = 'LegendCleaner'
console_out = False

def CheckAndRemoveByDate(fullname):
    current = datetime.datetime.now() - datetime.timedelta(days=keep_days)       
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
    if (filetime < current):        
        try:
            os.remove(fullname)
            Output('Delete ' + fullname)
        except PermissionError:
            Output('PermissionError ' + fullname)

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
                    CleanOutdatedFiles(full_filename, not (filename.lower() in folders))
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

def makeSampleConfig():    
    config = configparser.RawConfigParser()
    config.add_section('Config')
    config.set('Config', 'filters', ";".join(filters))
    config.set('Config', 'folders', ';'.join(folders))
    config.set('Config', 'keep_days', keep_days)
    config.set('Config', 'root', root)
    config.set('Config', 'logfile', logFile)
    config.set('Config', 'console_out', console_out)
    with open(fileName, 'w') as configfile:
        config.write(configfile)

def loadConfig():
    global keep_days
    global filters
    global folders
    global logFile
    global console_out

    config = configparser.RawConfigParser()
    config.read(fileName)

    strLogFile = config.get('Config', 'logfile')
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    logFile = strLogFile + nowDate + '.log'    

    strFilters = config.get('Config', 'filters')
    filters = strFilters.split(';')
    strFolders = config.get('Config', 'folders')
    folders = strFolders.split(';')
    keep_days = config.get('Config', 'keep_days')
    root = config.get('Config', 'root')
    console_out = config.getboolean('Config', 'console_out')

    Output('\nstart : ' + now.strftime('%Y-%m-%d %H:%M:%S'))
    Output('************** Config **************')    
    Output('root=' + str(root))
    Output('console_out='+str(console_out))
    Output('keep_days=' + str(keep_days))    
    Output('filters='+str(strFilters))
    Output('folders='+str(strFolders))
    Output('logFile='+strLogFile)
    Output('************************************')
    
def Output(obj):
    if type(obj) is str or type(obj) is int or type(obj) is float or type(obj) is bool:
        with open(logFile, "a") as log:
            log.write(str(obj)+'\n')
            log.close()
        if console_out == True:
            print(str(obj))
    elif type(obj) is list or type(obj) is dict or type(obj) is tuple:
        out = pprint.pformat(obj)
        Output(out)            

if __name__ == "__main__":
    # 셋팅 파일 저장
    if(os.path.exists(os.path.join(os.getcwd(),fileName))==False):
        makeSampleConfig()        

    loadConfig()

    CleanOutdatedFiles(os.getcwd(), True)
