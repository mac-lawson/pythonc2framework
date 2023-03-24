def getHelp():
    help = '''
    connect shh
    -c <username> <ip> <ssh port>

    list all active connections
    -l 

    ping
    -p <ip/uri>

    destroy program memory
    -d 

    initialize database (not required for non-persistent users)
    -init
    '''
    print(help)