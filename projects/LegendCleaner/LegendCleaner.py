

import configparser
import os
import re
import datetime
import pprint

configFile = 'LegendCleaner.ini'
root = '.'
keep_days = 7
filters = ['\.([0-9]){4}-([0-9]){2}-([0-9]){2}','\.([0-9]){8}-([0-9]){6}\.([0-9]){1,5}']
folders = ['x64\\crash', 'x64\\profile'] # 소문자로 입력해서 비교
logFile = 'LegendCleaner'
logFileRe=''
console_out = False


def CheckAndRemoveByDate(fullname):
    current = datetime.datetime.now() - datetime.timedelta(days=int(keep_days))
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

def CheckCleanFolder(target):
    for folder in folders:
        if folder in target :
            return True

    return False

# 해당 디렉토리의 오래된 파일들을 삭제한다.
def CleanOutdatedFiles(targetDir):
    try:
        for dirpath, dirnames, filenames in os.walk(targetDir):
            force = CheckCleanFolder(dirpath)
            for filename in filenames:
                if force or CheckRegexFile(filename):
                    CheckAndRemoveByDate(dirpath + '\\' + filename)

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
    with open(configFile, 'w') as configfile:
        config.write(configfile)

def loadConfig():
    global keep_days
    global filters
    global folders
    global logFile
    global console_out
    global logFileRe

    config = configparser.RawConfigParser()
    config.read(configFile)

    strLogFile = config.get('Config', 'logfile')
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    logFile = strLogFile.strip() + nowDate + '.log'
    logFileRe = strLogFile.strip() + '([ 0-9-:])+\.log'

    strFilters = config.get('Config', 'filters')
    filters = strFilters.strip().lower().split(';')
    strFolders = config.get('Config', 'folders')
    folders = strFolders.strip().lower().split(';')
    keep_days = config.get('Config', 'keep_days')
    root = config.get('Config', 'root')
    console_out = config.getboolean('Config', 'console_out')

    Output('\nstart : ' + now.strftime('%Y-%m-%d %H:%M:%S'))
    Output('************** Config **************')    
    Output('root=' + str(root))
    Output('console_out='+str(console_out))
    Output('keep_days=' + str(keep_days))    
    Output('filters='+str(strFilters.strip().lower()))
    Output('folders='+str(strFolders.strip().lower()))
    Output('logFile='+strLogFile.strip())
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
    if(os.path.exists(os.path.join(os.getcwd(),configFile))==False):
        makeSampleConfig()        

    loadConfig()

    filters.append(logFileRe.lower())

    CleanOutdatedFiles(root)
