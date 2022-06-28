import wmi
import ctypes
pid = 0
wmi = wmi.WMI()
for process in wmi.Win32_Process():
	if process.Name == "steam.exe":
		pid = process.ProcessId