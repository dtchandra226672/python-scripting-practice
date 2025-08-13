with open("uptime_log.txt", "r") as file:
    uptime = file.read().splitlines()

split_uptime = []
for a in uptime:
    parts = a.split(' ')
    split_uptime.append([parts[0], parts[1]])

uptime_count = []
for a, b in split_uptime:
    b = int(b)
    day = 0
    hrs = 0
    mnt = 0
    sec = 0

    if (b >= 86400):
        day = b // 86400
        b %= 86400
    if (b >= 3600):
        hrs = b // 3600
        b %= 3600
    if (b >= 60):
        mnt = b // 60
        b %= 60
    sec = int(b)

    uptime_count.append([day, hrs, mnt, sec])

with open("uptime_report.txt", "w") as file:
    file.write('''----------------------------
Server Health Summary
---------------------------- 
''')
    for a in range (len(uptime_count)):
        # file.write(split_uptime[a][0] + " : " + str(uptime_count[a][0]) + "d " + 
        #            str(uptime_count[a][1]) + "h " + str(uptime_count[a][2]) + "m " + 
        #            str(uptime_count[a][3]) + "s\n")
        
        server = split_uptime[a][0]
        days, hrs, mins, secs = uptime_count[a]
        label = "!! LOW UPTIME !!" if days <= 0 else ""
        file.write(f"{server:<15} : {days:02d}d {hrs:02d}h {mins:02d}m {secs:02d}s {label}\n")
    file.write('''----------------------------''')