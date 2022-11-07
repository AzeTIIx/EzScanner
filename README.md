# Summary

EzScanner allows you to perform a fast NMAP scan in TCP, as well as banner grab and scan a range of IP addresses to check if they are online.

Please do not use this tool on networks whose owner has not given you permission.

# 🛠️ Installation

With pip

```
pip install EzScanner
```
or

```
python3 -m install EzScanner
```


With Github

```
git clone https://github.com/CharlesAIMIN/EzScanner.git
cd EzScanner/
sudo python3 setup.py install
```

# Quick Start
PyPentest can be run from the CLI.

# 📚 CLI Example

You can perform nmap scan

```
EzScanner nmap -b 20 -e 80 -ip 127.0.0.1
```

Or scan a range of IP 

```
PyPentest isup -b 20 -e 80 -ip 127.0.0.1
```
