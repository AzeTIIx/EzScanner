[![Downloads](https://static.pepy.tech/badge/ezscanner)](https://pepy.tech/project/ezscanner)

# EzScanner the quick and easy nmap scanner

<div align="center">
  <img src="https://github.com/CharlesAIMIN/EzScanner/blob/main/EzScanner1.png">
</div>

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
git clone https://github.com/AzeTIIx/EzScanner.git
cd EzScanner/
sudo python3 setup.py install
```

# Quick Start
EzScanner can be run from the CLI.

# 📚 CLI Example

You can perform nmap scan

```
EzScanner nmap -b 20 -e 80 -ip 127.0.0.1
```

Or scan a range of IP 

```
EzScanner isup -b 20 -e 80 -ip 127.0.0.1
```
