import re

p = re.compile("ca.e") # p : pattern

"""
정규식
. : 하나의 문자 ex) ca.e = caae cabe cace...
^ : 문자열의 시작 ex) ^de = destiny, destination ...
$ : 문자열의 끝 ex) $on = competition, won ...
"""

m = p.match("careless") # match : 주어진 문자열의 시작부터 확인 > care (o), careless (o), caffe (x), good care(x)
# m = p.search("good care") # search : 주어진 문자열에 포함되는지 확인 > care (o), careless (o), good care (o), caffe (x)

def match_print(m):
    if m: 
        print("m.group() :", m.group()) # .group() : 일치하는 문자열 반환
        print("m.string :", m.string) # .string : 전체 문자열 반환
        print("m.start() :", m.start()) # .start() : 일치하는 문자열의 시작 인덱스 반환
        print("m.end() :", m.end()) # .end() : 일치하는 문자열의 끝 인덱스 반환
        print("m.span() :", m.span()) # .span() : 일치하는 문자열의 시작, 끝 인덱스 반환
    else :
        print("Not matched")

match_print(m)