import paramiko
import subprocess
import sqlite3
import os
import requests



'''
ssh_connect

This function creates an SSHClient object from the Paramiko library, 
sets the missing host key policy to automatically add new hosts to the known_hosts file, 
and then uses the connect() method to establish an SSH connection to the specified hostname with the given username and password.
 The function returns the SSHClient object, which can be used to run commands on the remote server.

Example usage:
client = ssh_connect('example.com', 'myusername', 'mypassword')
stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read().decode())
client.close()

'''
def ssh_connect(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password)
    return client

'''
list_clients

A backup function for if a standard text file is needed to be used instead of database
'''
def list_clients(file):
    print((open(str(file)).read))


'''
ping

This function defines a ping function that takes a host 
argument (either a URL or IP address) and uses the subprocess.run 
function to execute the ping command with the -c 1 
option (which sends a single packet) and the given host. 
The function checks the return code of the command to 
determine whether the host is reachable (return code 0) or not (return code non-zero).

Example usage:
if ping('google.com'):
    print('google.com is reachable')
else:
    print('google.com is not reachable')
'''

def ping(host):
    # Use the ping command to check if the host is reachable
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False
    
'''
createDB

This function creates a table named "targets" with three columns: 
"target_ip", "exploit_status", and "privileges" 
All of which are of data type TEXT. 
You can customize the database name and column data types as per your needs.


'''
def createDB():
    conn = sqlite3.connect('targets.db')  # connect to database (or create if not exists)
    c = conn.cursor()  # create a cursor object

    # create table with columns
    c.execute('''CREATE TABLE targets
                 (target_ip TEXT, exploit_status TEXT, privileges TEXT)''')

    conn.commit()  # commit changes
    conn.close()  # close connection

    print("PyC2f Framework Database Inited")


'''
Check whether a file exists at the given file_path.

Parameters:
    file_path (str): The path of the file to check.

Returns:
     bool: True if the file exists, False otherwise.

     
Usage:
if file_exists('/path/to/myfile.txt'):
    print('The file exists!')
else:
    print('The file does not exist.')

'''

def file_exists(file_path):

    return os.path.exists(file_path) and os.path.isfile(file_path)

'''
addTarget

Modifies database to add a new target

'''
def addTarget(ip, status, privilege):
    conn = sqlite3.connect('targets.db')  # connect to database (or create if not exists)
    c = conn.cursor()  # create a cursor object
    # create table with columns
    c.execute('''INSERT INTO targets (target_ip, exploit_status, privileges) VALUES ({ip}, {status}, {privilege});
    ''')

    conn.commit()  # commit changes
    conn.close()  # close connection

'''
This function tries every combination of username and password from the wordlists 
until it finds one that works or exhausts all possibilities. 
If successful credentials are found, the function prints a message indicating which credentials worked and returns True. 
Otherwise, it prints a message indicating that none of the provided credentials worked and returns False.

Usage:
try_credentials("https://example.com/login", "usernames.txt", "passwords.txt")


'''

def try_credentials(url, username_wordlist, password_wordlist):
    # Load the username and password wordlists into memory
    with open(username_wordlist) as f:
        usernames = f.read().splitlines()
    with open(password_wordlist) as f:
        passwords = f.read().splitlines()

    # Try each combination of username and password
    for username in usernames:
        for password in passwords:
            # Make the request with the current credentials
            response = requests.get(url, auth=(username, password))

            # Check if the response indicates successful authentication
            if response.status_code == 200:
                print(f"Successfully authenticated with username '{username}' and password '{password}'")
                return True

    # If we get here, none of the credentials worked
    print("Unable to authenticate with any of the provided credentials")
    return False
