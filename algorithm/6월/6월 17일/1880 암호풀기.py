import sys
sys.stdin = open('input (43).txt', 'r')


secureCode = input()
encode = input()

# ord(z) => 122
# ord(a) => 97
# ord(A) => 65
decode = [0] * 123

# 변경된 알파벳 순서를 아스키코드에 맞춰서 변경
# index가 아스키코드
for i in range(26):
    decode[97 + i] = secureCode[i]
    decode[65 + i] = chr(ord(secureCode[i]) - 32)

result = ''

for i in range(len(encode)):
    try:
        result += decode[ord(encode[i])]
    except: # 공백이면 공백으로 추가
        result += ' '

print(result)





