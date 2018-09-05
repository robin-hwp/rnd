# Automate the Boring stuff
# Chapter 8 – Reading and Writing Files

import os

# 디렉토리와 파일 합산 경로
os.path.join('C:\\Windows\\System32', 'calc.exe') 
# return : 'C:\\Windows\\System32\\calc.exe'


# 현재 작업 디렉토리 확인 및 현재 작업 디렉토리 변경 (Current Working Directory)
os.getcwd()
os.chdir('C:\\Windows\\System32')
os.getcwd()

# relative path or absolute path
# ..\ or c:\

# Creating New Folders with os.makedirs()
os.makedirs('C:\\delicious\\walnut\\waffles')

# os.path
os.path.abspath('.')
os.path.isabs('.')                  # return : False
os.path.isabs(os.path.abspath('.')) # return : True
os.path.relpath('C:\\Windows', 'C:\\') # return : 'Windows'

# os.path.dirname(path), os.path.basename(path)
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path) # return : calc.exe
os.path.dirname(path) # return : C:\\Windows\\System32
os.path.split(path) # return : tuple ('C:\\Windows\\System32', 'calc.exe')

# os.path.split() 함수는 폴더명과 파일명 구조의 Tuple로 분리를 해주지만.
# path.split(os.path.sep)는 각 항목들을 리스트로 분리해준다.

# os.listdir 인자로는 폴더까지만 처리한다.
os.path.getsize('C:\\Windows\\System32\\calc.exe') # return : file size
os.listdir(os.path.dirname(path)) # return : 해당 폴더에 있는 폴더와 파일 리스트, 
# os.listdir() 함수를 이용한 항목 for loop
# for filename in os.listdir('C:\\Windows\\System32'): 

os.path.exists(path) # 해당 경로의 파일 또는 폴더가 존재 여부 체크 : True / False
os.path.isdir('C:\\Windows\\System32') # 폴더인지 체크 : True / False
os.path.isfile('C:\\Windows\\System32\\calc.exe') # 파일인지 체크 : True / False

# 만약 드라이브에 미디어가 삽입되었는지 체크할땐 드라이브 폴더를 체크한다.
os.path.exists('D:\\')

# 파일 사용 순서
# 1. File = open(path[, r/w/a])
# 2. File.read(stirng) or File.write(string)
# 3. File.close()