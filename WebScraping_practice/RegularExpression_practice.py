import re #정규식 라이브러리

pattern = re.compile("12.4") #. : 하나의 문자를 의미(12.4) >>> 1234, 12a4
                             # ^ : 문자열의 시작(^124)     >>> 1245, 1243
                             # $ : 문자열의 끝(124&)       >>> 124, 0124

def if_matching(matching):
    if matching :
        print("m.group() :",matching.group()) # 일치하는 문자열 반환
        print("m.string :",matching.string)   # 입력한 문자열 반환
        print("m.start() :",matching.start()) # 일치하는 문자열의 시작 index
        print("m.end() :",matching.end())     # 일치하는 문자열의 끝 index
        print("m.span :",matching.span())     # 일치하는 문자열의 시작과 끝 index
 
    else :
        print("error")

matching = pattern.match("00001234") # .match() : 앞부터 확인 > 뒤에 다른 것이 있어도 가능
if_matching(matching)

matching = pattern.search("00001234") # .search() : 일치하는것이 있는지 확인
if_matching(matching)

list = pattern.findall("123400001224") # .findall() : 일치하는 모든 것을 리스트로 반환
print(list)


"""
<정규식 정리>
1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열") : 문자열에 처음부터 일치여부 확인 > 뒤에는 상관x
3. m = p.search("비교할 문자열") : 문자열에 일치하는 것이 있는지 확인
4. list = p.findall("비교할 문자열") : 일치하는 모든것을 리스트로 반환

원하는 형태 : 정규식
. : 하나의 문자를 의미(12.4) >>> 1234, 12a4
^ : 문자열의 시작(^124)      >>> 1245, 1243
$ : 문자열의 끝(124&)        >>> 124, 0124
"""