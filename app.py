#modules
import requests

print("LNG - Language Converter. Made By Ct tricks ~AKA~ Tanish Raj.")
print("[ON] Cnnecting with server...")

print("[--]\n[--] Enter Source Language Code. For example 'en' for English,")
sl = input("[IN] SL : ")

print("[--]\n[--] Enter target Language Code. For example 'hi' for Hindi,")
tl = input("[IN] TL : ")

print("[--]\n[--] Enter the message/text you want to convert,")
text = input("[IN] Text : ")

print("[--]\n[--]")
#start conversion
url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl="+ sl +"&tl="+ tl +"&dt=t&q=" + text

response = requests.get(url)
if response.status_code == 200 :
    data = response.text
    data = data.split('"')[1]
    print("[OP] Output : " + data)
    print("[--]\n[SC] Converted Successfully....")
else : 
    print("[UT] Unable to translate at the moment. Try again later")
