#!/usr/bin/env python3
"""
RedTeam Framework Demo Script
This script demonstrates the C2 server capabilities
"""

import requests
import json
import time

SERVER = "http://127.0.0.1:8080"

def check_registered_agents():
    """Check what agents are registered"""
    print("\n🔍 Checking for registered agents...")
    # This is a simple way to test - we'll try to get tasks for a known agent
    # In a real scenario, you'd have an admin endpoint to list agents
    
def send_shell_command(agent_id, command):
    """Send a shell command to an agent"""
    print(f"\n📤 Sending shell command to agent {agent_id[:8]}...")
    print(f"Command: {command}")
    
    task = {
        "type": "shell",
        "command": command
    }
    
    try:
        response = requests.post(f"{SERVER}/task/{agent_id}", 
                               json={"task": task}, 
                               timeout=5)
        if response.status_code == 200:
            print("✅ Task sent successfully!")
            return True
        else:
            print(f"❌ Failed to send task: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending task: {e}")
        return False

def demo_workflow():
    """Demonstrate the complete workflow"""
    print("🚀 RedTeam Framework Demo")
    print("=" * 50)
    
    # Simulate an agent ID (in real scenario, this would come from registration)
    import uuid
    demo_agent_id = str(uuid.uuid4())
    
    print(f"\n📝 Demo Agent ID: {demo_agent_id[:8]}...")
    
    # Register the demo agent
    print("\n🔗 Registering demo agent...")
    try:
        response = requests.post(f"{SERVER}/register", 
                               json={"agent_id": demo_agent_id},
                               timeout=5)
        if response.status_code == 200:
            print("✅ Agent registered successfully!")
        else:
            print(f"❌ Registration failed: {response.status_code}")
            return
    except requests.exceptions.RequestException as e:
        print(f"❌ Registration error: {e}")
        return
    
    # Send some demo commands
    commands = [
        "whoami",
        "pwd", 
        "ls -la",
        "uname -a"
    ]
    
    for cmd in commands:
        if send_shell_command(demo_agent_id, cmd):
            time.sleep(1)  # Brief pause between commands
    
    print("\n✨ Demo completed!")
    print("\n📋 Framework Features Demonstrated:")
    print("  • Agent registration")
    print("  • Task assignment") 
    print("  • Shell command execution")
    print("  • C2 communication")

if __name__ == "__main__":
    demo_workflow()
