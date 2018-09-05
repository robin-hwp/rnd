import pprint

# pprint.pformat을 이용한 파일 핸들링
'''
    myCats.py를 쓰게되면 module 위치가 검색되지 않는 디렉토리에 파일이 생성될 수 있다.
    그렇게되면 나중에 import를 못하게 되므로 myCats.py 파일을 모듈 참조가 가능한 위치로 
    복사해 주면 된다.
'''

# 1. 쓰기
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

