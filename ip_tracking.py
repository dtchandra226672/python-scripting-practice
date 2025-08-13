import subprocess
from datetime import datetime
  
with open('ip_addr_list.txt', 'r') as file:
    ip_addr = file.read().splitlines()

for ip in ip_addr:
    print(ip)
    # subprocess.run(['ping', ip])
    result = subprocess.run(['ping', '-n', '1', ip])

    now = datetime.now() 
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("result.txt", "a") as log:
        if result.returncode == 0:
            log.write(f"[{timestamp}] {ip} is reachable\n")
        else:
            log.write(f"[{timestamp}] {ip} is unreachable\n")