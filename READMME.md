# 🔍 Network Security Scanner

A lightweight Python-based network security scanner using **Nmap** to perform quick port scanning and service detection. Ideal for cybersecurity audits and penetration testing. 🚀

## ⚡ Features
- ✅ **Basic scan** (`-sT -F`): Fast TCP scan on common ports.
- ✅ **Version detection** (`-sV -F`): Identifies running services and versions.
- ✅ **Logging**: Saves scan results in timestamped log files.
- ✅ **Docker support**: Run the scanner inside a container with pre-installed security tools.

## 🛠️ Installation
### **1. Install Dependencies**
Make sure you have **Python 3**, **Nmap**, and `python-nmap` installed.

#### **For Kali Linux & Ubuntu**
```bash
sudo apt update && sudo apt install nmap python3-pip -y
pip install python-nmap
```

#### **For macOS (using Homebrew)**
```bash
brew install nmap
pip install python-nmap
```

## 🚀 Usage
Run the script with a target IP or domain:
```bash
python3 scanner.py <TARGET_IP_OR_DOMAIN>
```

### **Example Commands**
#### 🔹 Basic scan
```bash
python3 scanner.py 192.168.1.1
```

#### 🔹 Version detection scan
```bash
python3 scanner.py scanme.nmap.org --type version
```

## 🐳 Running with Docker
To use the scanner inside a Docker container:

### **1. Build the Docker Image**
```bash
docker build -t security-scanner .
```

### **2. Run the Scanner**
```bash
docker run --rm security-scanner <TARGET_IP_OR_DOMAIN>
```

## 📜 License
This project is open-source and available under the **MIT License**.

---
Made with ❤️ for ethical hacking & cybersecurity! 🔒

