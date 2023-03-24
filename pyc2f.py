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
PyC2f.addTarget("192.138.981", "Up", "Attack Host")
# if no sys args are provided, tell the user how to run the help command

if(len(sys.argv)) == 1:
    print("python3 pyc2f.py -h")

# if -h is provided, run the help menu

elif(sys.argv[1]) == "-h":
    PyC2f.logPlatform("-h", "User asked for help")
    help.getHelp()

elif(sys.argv[1]) == "-c":
    if(PyC2f.ping(str(sys.argv[2]))):
        print("[*] target is up")
    else:
        print("[*] target is down")

elif(sys.argv[1]) == "-init":
    if(PyC2f.fileExists("targets.db")):
        print("Database exists")
    else:
        PyC2f.createDB()

elif(sys.argv[1]) == "-l":
    if(PyC2f.fileExists("targets.db")):
        PyC2f.listTargets()
    else:
        print("Database not created. Run python3 pyc2f.py -init")
   


