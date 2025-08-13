import shutil

directory = "C:\\Users"
disk_info = shutil.disk_usage(directory)
disk_free  = disk_info.free / 1024**3
disk_used  = disk_info.used / 1024**3
disk_total = disk_info.total / 1024**3
disk_usage = disk_used / disk_total * 100

with open ("disk_status.txt", "w") as file:
    file.write('''----------------------------
Disk Usage Report
----------------------------\n''')
    file.write(f"{'Path':<15} : {directory:>5}\n")
    file.write(f"{'Total Space':<15} : {disk_total:>5.2f} GB\n")
    file.write(f"{'Used Space':<15} : {disk_used:>5.2f} GB\n")
    file.write(f"{'Free Space':<15} : {disk_free:>5.2f} GB\n")
    file.write(f"{'Usage':<15} : {disk_usage:>5.2f}%\n")