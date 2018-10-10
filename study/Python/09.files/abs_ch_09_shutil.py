import os, shutil

os.chdir('./study/python/09.files/test')
print(os.getcwd())

# 파일 복사
shutil.copy('../abs_ch_09_shutil.py', '.')
shutil.copy('../abs_ch_09_shutil.py', './abs_ch_09_shutil.copy_rename.py')
print('copy result :')
print(os.listdir())
print('')


# 이미 폴더가 있으면 폴더 삭제
if os.path.isdir('../test2'):
    shutil.rmtree('../test2')

# 디렉토리 복사
print('shutil.copytree() test :')
print(os.listdir('..'))
shutil.copytree('../test', '../test2')
print("shutil.copytree('../test', '../test2')")
print(os.listdir('..'))
print('')

shutil.copy('../abs_ch_09_shutil.py', '../abs_ch_09_shutil.temp0.py')
shutil.copy('../abs_ch_09_shutil.py', '../abs_ch_09_shutil.temp1.py')
shutil.move('../abs_ch_09_shutil.temp0.py', './abs_ch_09_shutil.move0.py')
shutil.move('../abs_ch_09_shutil.temp1.py', './abs_ch_09_shutil.move1.py')
print('move result :')
print(os.listdir())
print('')

shutil.copy('../abs_ch_09_shutil.py', './abs_ch_09_shutil.temp0.py')
print('copyto ./abs_ch_09_shutil.temp0.py')
print(os.listdir())
os.unlink('./abs_ch_09_shutil.temp0.py')
print('os.unlink(./abs_ch_09_shutil.temp0.py) result :')
print(os.listdir())

# 파일 생성 후 휴지통으로 보낸다.
# how to install send2trash.> python -m pip install send2trash
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('bacon.txt')


# 대상 디렉토리의 하위 디렉토리까지 모두 돌면서 확인.
# for문 하나에서... 대단 os.walk.
for folderName, subfolders, filenames in os.walk('..'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')


import zipfile
print(os.getcwd())

# zip 파일로 압축하기
name = os.path.basename(os.getcwd()))

newZip = zipfile.ZipFile('../new.zip'.format(), 'w')


# for folderName, subfolders, filenames in os.walk('.'):
#     print('The current folder is ' + folderName)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)
#     print('')
# newZip.write()



# 1. 파일 목록 얻기
# (1) glob.glob(wildcard) - 유닉스 경로명 패턴 스타일로 파일 목록을 얻을 수 있다.
# (2) os.listdir(path) - 지정된 디렉토리의 전체 파일 목록을 얻을 수 있다.
# (3) dircache.listdir(path) - os.listdir(path)와 동일한 파일 목록을 전달한다.
# path가 변경되지 않았을 때, dircache.listdir()은 다시 디렉토리 구조를 읽지 않고 이미 읽은 정보를 활용
# dircache.annotate(head, list) - 일반 파일명과 디렉토리명을 구분해주는 함수

# 2. 디렉토리 다루기
# os.chdir(path) - 작업하고 있는 디렉토리 변경
# os.getcwd() - 현재 프로세스의 작업 디렉토리 얻기
# 기타 여러 함수가 있다.

# 3. 파일 이름 다루기
# os.path.abspath(filename) - 파일의 상대 경로를 절대 경로로 바꾸는 함수
# os.path.exists(filename) - 주어진 경로의 파일이 있는지 확인하는 함수
# os.curdir() - 현재 디렉토리 얻기
# os.pardir() - 부모 디렉토리 얻기
# os.sep() - 디렉토리 분리 문자 얻기

# 4. 경로명 분리하기
# os.path.basename(filename) - 파일명만 추출
# os.path.dirname(filename) - 디렉토리 경로 추출
# os.path.split(filename) - 경로와 파일명을 분리
# os.path.splitdrive(filename) - 드라이브명과 나머지 분리 (MS Windows의 경우)
# os.path.splitext(filename) - 확장자와 나머지 분리