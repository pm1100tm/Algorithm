"""
A씨는 개발된 소스코드를 특정업체에 납품하려고 한다.
개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다.
A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.
A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.
"""
# 1. 패일 패스만 리스트로 가져오는 메서드 구현
# 2. 파일 읽기/수정하기/저장하기 메서드 구현
# 3. 파일 읽은 후, 탭이 있나 검사하는 메서드 구현

import os

def get_file_path():
  """
  지정한 패스의 모든 .py 파일 가져와서 리스트 형태로 반환합니다.
  : param: -
  : return: list,
  """
  pathlist = []
  path = os.getcwd() + "/quiz/codingDojang/Python-Algorithm/002_source_code_file"
  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith(".py"):
        pathlist.append(root + "/" + file)
      else: pass
  return pathlist

# 파일 읽기, 수정하기, 저장하기
def file_read_write():
  """
  파일 패스를 취득한 후, 각 파일을 읽고, 수정하고, 저장합니다.
  : param: -
  : return: -
  """
  pathlist = get_file_path()
  for path in pathlist:
    new_lines = []
    with open(path, "r") as f:
      lines = f.readlines()
      for line in lines:
        new_lines.append(line.replace("\t", " "*4))

    with open(path, "w") as f:
      f.writelines(new_lines)

file_read_write()

def check_work():
  """
  파일을 읽어들여, 문자열 안에 탭이 있는지 검사합니다.
  탭이 있다면 예외를 발생시킵니다. 없다면 검사완료 메시지를 출력합니다.
  : param: -
  : return: -
  """
  pathlist = get_file_path()
  for path in pathlist:
    _file = open(path)
    if _file.read().find("\t") != -1:
      raise Exception("코드에 탭을 찾았습니다.")
    else:
      print("파일이 정상입니다. 검사 완료.")


""" 백업 할 필요가 있는 경우 cp 는 osx 명령어 """
def file_backup():
  pathlist = get_file_path()
  os.system ("cp %s %s" % (path, path+".bak")) #백업파일 생성


""" with 안쓰고 """
def test():
  path = os.getcwd() + "/quiz/codingDojang/Python-Algorithm/002_source_code_file/code1.py"
  f = open(path, "r")
  lines = f.read()

  for "\t" in lines:
    pass

  new_lines = lines.replace("\t", " "*4)

  newf = open(path, "w")
  newf.write(new_lines)
  newf.close()
  f.close()


""" 하면서 얻은 것 """
# import os 모듈
# a = os.path.dirname(__file__) # 현재 파일의 절대 경로
# b = os.path.basename(__file__) # 현재 파일 이름
# c = os.getcwd() # 현재 작업 폴더 경로
# d = os.listdir(path) # path 안의 모든 파일 이름을 리스트로 반환
# file객체.writelines(iter) - 문자열, 문자열 리스트

# w 모드로 파일을 열었을 때, 읽지 못함.
# 파일 모드 정리
"""
r 읽기 전용
w 쓰기 전용
  w 파일 내용 버려
  a 파일 끝에 추가
  x 파일이 있으면 에러

읽기/쓰기
w+ 파일 내용 버려
r+ 파일 내용 유지 - 파일 처음부터 쓰기
a+ 파일 내용 유지 - 파일 끝부터 쓰기
x+ 파일 있으면 에러

t 텍스트 모드
  rt, wt 파일을 텍스트 모드로 여는데, t는 생략 가능
b 바이너리 모드
  rb, wb 등은 피클링을 사용하거나 바이너리 데이터를 직접 저장할 때 사용
"""







