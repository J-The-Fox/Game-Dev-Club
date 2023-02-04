# Built-In Modules
import os
# Downloaded Modules
import psutil

# Psutil Can Grab Info About Your System, Helpful In Games When You Need To Know How Much Memory Is Being Used
# Note: psutil Measures Capacity In Bytes. 

# Here Are The Most Relevant System Info Gathered Whenever You Run This Program
# These Are Not Process Specific
systemInfoList = [
    "# -----=====[PID]=====----- #",
    f"Current Pid: {os.getpid()}", # Using os For This But It Is Helpful To Get The PID, Can Use It To Monitor Your Program
    "# -----=====[RAM]=====----- #",
    f"Total: {psutil.virtual_memory()[0]} Bytes",
    f"Available: {psutil.virtual_memory()[1]} Bytes",
    f"Used: {psutil.virtual_memory()[3]} Bytes",
    f"Free: {psutil.virtual_memory()[4]} Bytes",
    "# -----=====[Swap]=====----- #",
    f"Total: {psutil.swap_memory()[0]} Bytes",
    f"Used: {psutil.swap_memory()[1]} Bytes",
    f"Free: {psutil.swap_memory()[2]} Bytes",
    "# -----=====[CPU]=====----- #",
    f"Core Count: {psutil.cpu_count()}",
    #f"Frequency: {psutil.cpu_freq()[0]}", # Works On Windows, Either MacOS Has An Issue Or psutil Has An Issue With It - -J-The-Fox
    "# -----=====[Disk]=====----- #",
    "Size: " + str(psutil.disk_usage("/")[0]) + " Bytes",
    "Space Used: " + str(psutil.disk_usage("/")[1]) + " Bytes",
    "Space Free: " + str(psutil.disk_usage("/")[2]) + " Bytes",
    "Percent Used: " + str(psutil.disk_usage("/")[3]) + "%",
    "# -----=====[Boot]=====----- #",
    f"Boot Time: {psutil.boot_time()} Seconds",
]

# Loops Over Each Item In The List And Prints It Out
for item in systemInfoList:
    print(item)

print("---------------------------------")

# You Can Make It Process Specific By Adding A psutil.Process(PID).your_command()
# Like This
print("CPU Percent For This Process: " + str(psutil.Process(os.getpid()).cpu_percent()) + "%")