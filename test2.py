import openai




# openai.api_key= ""
# 
# dialogue= []
# while True:
#     text= input()
#     if not text:
#         break
#     dialogue.append({"role": "user", "content": f"{text}"})
#     response= openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages= dialogue
#     )
#     
#     try:
#         print(response['choices'][0]['message']['content'])
#     except Exception as e:
#         print(e)
#         print(response)
#     print('\n\n\n')


import requests
from bardapi import Bard
token= ""

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", token)
bard= Bard(token=token,session=session)

while True:
    text= input()
    if not text:
        break
    print(bard.get_answer(text)['content'])








