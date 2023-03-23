import sys
from c2f import PyC2f, help

logo = '''

██████  ██    ██  ██████ ██████  ███████ 
██   ██  ██  ██  ██           ██ ██      
██████    ████   ██       █████  █████   
██         ██    ██      ██      ██      
██         ██     ██████ ███████ ██      
                                         
Developer: Mac Lawson
https://github.com/mac-lawson
https://maclawson.vercel.app
mlawson07@protonmail.com
'''

print(logo)
if(len(sys.argv)) == 1:
    print("python3 pyc2f.py -h")

elif(sys.argv[1]) == "-h":
    help.getHelp()

elif(sys.argv[1]) == "-c":
    if(PyC2f.ping(str(sys.argv[2]))):
        print("[*] target is up")
    else:
        print("[*] target is down")

# elif(sys.argv[1]) == "-l":
#     if(PyC2f.ping(str(sys.argv[2]))):
#         print("[*] target is up")
#     else:
#         print("[*] target is down")



