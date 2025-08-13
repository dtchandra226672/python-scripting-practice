with open ("port_scan_results.txt", "r") as file:
    ports = file.read().splitlines()

# create array from the txt file
port_list = []
for a in ports:
    split_ip = a.split(":")
    split_port = split_ip[1].split(" ")
    port_list.append([split_ip[0], split_port[0], split_port[1]])

count_ports = {}
for a, b, c in port_list:
    if a not in count_ports:
        if c == "CLOSED":
            count_ports[a] = [1, 0, 1] # total, open, close
        else:
            count_ports[a] = [1, 1, 0] # total, open, close
    else:
        if c == 'CLOSED':
            count_ports[a][0] += 1 # increment total
            count_ports[a][2] += 1 # increment close
        else:
            count_ports[a][0] += 1 # increment total
            count_ports[a][1] += 1 # increment open

total_ip, total_ports = 0, 0

for a in (count_ports):
    total_ip += 1
    total_ports += count_ports[a][0]


with open ("port_summary.txt", "w") as file:
    file.write('''----------------------------
Port Scan Summary
---------------------------- 
''')
    for a in count_ports:
        port = a
        total, open, close = count_ports[a]
        file.write(f"{port:<15} : {total} scanned, {open} open, {close} closed\n")
    file.write("----------------------------\n")
    file.write(f"{'Total IPs':<15} : {total_ip}\n")
    file.write(f"{'Total Ports':<15} : {total_ports}\n")