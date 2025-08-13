with open ("server_status.txt", "r") as file:
    logs = file.read().splitlines()

status = []
for log in logs:
    status.append(log.rsplit(" ", 1))

# create a dictionary for count
count = {}
for a, b in status:
    if b not in count:
        count[b] = 1
    else:
        count[b] += 1

# create the summary file
with open("server_summary.txt", "w") as file:
    file.write('''----------------------------
    Server Health Summary
---------------------------- 
''')
    for a, b in count.items():
        file.write(f"{a:<10} : {b:>5}\n")
    file.write('----------------------------\n')
    file.write(f"{'Total':<10} : {str(len(status)):>5}")