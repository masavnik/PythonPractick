import re
import fileinput

s = 'По всем вопросам пишите на vasiliy-pupkin@gmail.com, или на secondemail@yandex.ru, отвечу сразу. Или пишите моему ассистенту secretary@gmail.com!'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', s)
for email in emails:
    print(email)


pattern = re.compile(r'(\+7|8).*?(\d{2,3}).*?(\d{2,3}).*?(\d{2}).*?(\d{2})')
def isValid(number):
    if re.match(pattern, number):
        print("ДА")
    else:
        print("НЕТ")
isValid(input())