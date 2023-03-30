# import paramiko

# # Source and destination ports
# source_port = 3001
# destination_port = 9000

# # Create SSH connection
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('localhost', username='Praful Patekar', password='lghive2023')

# # Set up port forwarding
# transport = ssh.get_transport()
# channel = transport.open_channel('direct-tcpip', ('localhost', source_port), ('localhost', destination_port))

# # Keep the script running to maintain the port forwarding tunnel
# while True:
#     print("Running")


import paramiko

# SSH server details
ssh_host = '172.23.16.1'
ssh_port = 22
ssh_username = 'Praful Patekar'
ssh_password = 'lghive2023'


# Source and destination ports
source_port = 3001
destination_port = 9000

# Create SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

# Set up port forwarding
transport = ssh.get_transport()
channel = transport.open_channel('direct-tcpip', ('localhost', source_port), ('localhost', destination_port))

# Keep the script running to maintain the port forwarding tunnel
while True:
    pass
