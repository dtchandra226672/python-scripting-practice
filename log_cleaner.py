import os
from datetime import datetime

dir_list = os.listdir()
log_files = []
for name in dir_list:
    if name.startswith("log ") and name.endswith(".txt"):
        log_files.append(name)

dated_logs = []
for f in log_files:
    try:
        date_str = f.split()[1].split(".")[0]
        log_date = datetime.strptime(date_str, "%Y-%m-%d")
        dated_logs.append((log_date, f))
    except ValueError:
        continue  # skip malformed files
dated_logs.sort()
logs_to_delete = dated_logs[:-3]

if logs_to_delete:
    for a, filename in logs_to_delete:
        print(filename)
    switch = True;
else:
    print("No logs to delete.")
    switch = False;
    

while (switch):
    print("These files are bound to be removed, confirm deletion? (y/n)")
    user_input = input()
    
    if user_input.lower() == 'y':
        for _, filename in logs_to_delete:
            os.remove(filename)
            print(f"Deleted: {filename}")
        break;
    elif user_input.lower() == 'n':
        break;
    else:  
        print("Input invalid, please key in again!")
    
# now = (datetime.now()).date()
# two_ago = now - timedelta(days=2)
# delta = two_ago - dates[0]
# max_delta = timedelta(days=0)

# if delta > max_delta:
#     delta_int = delta.days
    
#     for a in range(delta_int):
#         filename = "log " + str(dates[0] + timedelta(days=a)) + ".txt"
#         if os.path.exists(filename):
#             os.remove(filename)
#         else:
#             print("The file " + filename + " does not exist")
# else: 
#     print("The log files are already at the latest 3 days")