<div align="start">
  <img src="style/Sec.png" alt="CVE Hunter" width="250" height="300"/>
</div>

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3130/)
[![Python 3.6](https://img.shields.io/badge/python-3.6+-yellow.svg?logo=python)](https://www.python.org/downloads/release/python-360/)
[![GitHub](https://img.shields.io/github/license/i1zco/Secra?color=green&logo=gnu)](https://www.gnu.org/licenses/gpl-3.0.txt)


Secra is a cutting-edge tool designed to identify and report security vulnerabilities. 
By analyzing software versions or scanning operating systems through IP addresses, Secra provides detailed insights 
to help secure your infrastructure against potential threats.

## Features
-  **Version-Based Detection:** Detect vulnerabilities based on the input software version.
-  **IP-Based OS Scan:** Scan operating systems and versions via an IP address.
-  **Detailed Reporting:** Generate comprehensive reports on detected vulnerabilities.
-  **Fast & Efficient:** Optimized for quick scanning without overloading your network.

#  Installation

1. Clone the repository:
```
git clone https://github.com/N3ullex/Vulnex.git                                                                        
cd Vulnex

pip install -r requirements.txt
python secra.py

```

```
Available CPEs found:
[1] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:x64:*
[2] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:*:*
[3] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:arm64:*
[4] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:x86:*
[5] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2166:*:*:*:*:*:arm64:*
[6] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2107:*:*:*:*:*:arm64:*
[7] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2045:*:*:*:*:*:arm64:*
[8] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1992:*:*:*:*:*:arm64:*
[9] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1937:*:*:*:*:*:arm64:*
[10] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1932:*:*:*:*:*:arm64:*
===============================================================
Select a CPE number from the list: 227
===============================================================
cpe:2.3:o:microsoft:windows_10_1709:-:*:*:*:*:*:*:*
===============================================================
Please Wait...

CVE ID: CVE-2018-0824
Descriptions: A remote code execution vulnerability exists in "Microsoft COM for Windows" when it fails to properly handle serialized objects, aka "Microsoft COM for Windows Remote Code Execution Vulnerability." This affects Windows 7, Windows Server 2012 R2, Windows RT 8.1, Windows Server 2008, Windows Server 2012, Windows 8.1, Windows Server 2016, Windows Server 2008 R2, Windows 10, Windows 10 Servers.
Severity: HIGH
CVSS_ScoreV40: None
CVSS_ScoreV31: 8.8
CVSS_ScoreV30: None
===============================================================
```


It will show you the ports, their versions, the system and its version, then choose the CPE you want and it will show you the vulnerabilities in it.'''


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
