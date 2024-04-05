import os
import subprocess

def read_conf_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("bst.instance.Pie64.status.adb_port"):
            port_str = line.split("=")[1].strip()
            port_str = port_str.replace('"', '')
            return int(port_str)

def run_adb_command(port):
    command = f"adb connect 127.0.0.1:{port}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    file_path = r"C:\ProgramData\BlueStacks_nxt\bluestacks.conf"
    if os.path.exists(file_path):
        port = read_conf_file(file_path)
        if port:
            run_adb_command(port)
        else:
            print("Could not find adb_port in the configuration file.")
    else:
        print(f"The specified file {file_path} does not exist.")
