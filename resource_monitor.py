import pandas as pd

df = pd.read_csv('resource_log_usage.csv')

cpu_thresh = 90
mem_thresh = 85
disk_thresh = 90

alerts = df[
    (df["cpu_usage"] > cpu_thresh) |
    (df["memory_usage"] > mem_thresh) |
    (df["disk_usage"] > disk_thresh)
]

print(alerts)

with open ("resource_alerts.txt", "w") as file:
    for index, row in alerts.iterrows():
        cpu_alert = (" CPU: " + str(row['cpu_usage']) + '%') if row['cpu_usage'] > cpu_thresh else ""
        mem_alert = (" MEMORY: " + str(row['memory_usage'])+ '%') if row['memory_usage'] > mem_thresh else ""
        dsk_alert = (" DISK: " + str(row['disk_usage'])+ '%') if row['disk_usage'] > disk_thresh else ""
        
        file.write(f"[ALERT] {row['timestamp']} - {row['hostname']} -{cpu_alert:>10}{mem_alert:>15}{dsk_alert:>15} (CRITICAL) \n")

