import subprocess

def run_shell(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=10)
        return output.decode()
    except Exception as e:
        return str(e)