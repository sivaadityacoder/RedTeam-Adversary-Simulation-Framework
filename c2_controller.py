#!/usr/bin/env python3
"""
Interactive C2 Controller
Send commands to real agents and see results
"""

import requests
import json
import time
import sys

SERVER = "http://127.0.0.1:8080"

def list_agents():
    """In a real framework, you'd have an endpoint to list agents"""
    print("📋 Note: This framework stores agents in memory")
    print("   Agents register when they connect and appear in server logs")

def send_command_to_agent(agent_id, command):
    """Send a command and wait for result"""
    print(f"\n📤 Sending command to agent {agent_id[:8]}...")
    print(f"Command: '{command}'")
    
    task = {
        "type": "shell",
        "command": command
    }
    
    # Send the task
    try:
        response = requests.post(f"{SERVER}/task/{agent_id}", 
                               json={"task": task})
        if response.status_code == 200:
            print("✅ Task queued successfully!")
            print("⏳ Waiting for agent to execute...")
            return True
        else:
            print(f"❌ Failed to queue task: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def interactive_mode():
    """Interactive command mode"""
    print("\n🎮 Interactive C2 Mode")
    print("=" * 40)
    print("Enter commands to send to agents:")
    print("Type 'quit' to exit")
    
    # For demo, we'll use a test agent ID
    agent_id = input("\n🆔 Enter agent ID (or press Enter for demo): ").strip()
    if not agent_id:
        import uuid
        agent_id = str(uuid.uuid4())
        # Register the agent
        requests.post(f"{SERVER}/register", json={"agent_id": agent_id})
        print(f"📝 Using demo agent: {agent_id[:8]}...")
    
    while True:
        try:
            command = input("\n💻 Command> ").strip()
            if command.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            elif command:
                send_command_to_agent(agent_id, command)
            else:
                print("Please enter a command")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

def main():
    print("🔴 RedTeam C2 Controller")
    print("=" * 50)
    
    # Check server status
    try:
        response = requests.get(f"{SERVER}/", timeout=2)
        print("✅ C2 Server is online")
    except:
        print("❌ C2 Server is not responding")
        sys.exit(1)
    
    print("\nChoose an option:")
    print("1. Interactive command mode")
    print("2. Quick demo")
    
    choice = input("\nChoice (1-2): ").strip()
    
    if choice == "1":
        interactive_mode()
    elif choice == "2":
        # Quick demo
        import uuid
        agent_id = str(uuid.uuid4())
        requests.post(f"{SERVER}/register", json={"agent_id": agent_id})
        
        demo_commands = ["whoami", "pwd", "date", "ps aux | head -5"]
        for cmd in demo_commands:
            send_command_to_agent(agent_id, cmd)
            time.sleep(1)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
