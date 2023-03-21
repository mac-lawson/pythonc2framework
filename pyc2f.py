import sys
from c2f import help

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


