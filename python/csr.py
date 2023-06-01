from netmiko import ConnectHandler
import re

router = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.3.1',
    'username' : 'cisco',
    'password' : 'cisco123!',
    'port' : 22,
    'verbose' : True
}

# Réalise la connexion ssh avec le serveur Linux
net_connect = ConnectHandler(**router)

for a in  [1,2,3,4]:
   interface = net_connect.send_command('sh ip int gigabitethernet'+str(a))
   print(interface)

int_br = net_connect.send_command('sh ip int brief')
print(int_br)

ping = net_connect.send_command('ping 192.168.4.2')
test = net_connect.send_command('ping 192.168.3.2')

print(ping)
print(test)


