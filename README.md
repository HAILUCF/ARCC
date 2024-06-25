# ARCC
Instructions on getting started on UCF's Advanced Research Computing Center's high-performance computing clusters.

* [ARCC Home Page](https://arcc.ist.ucf.edu/)
* [ARCC Tutorials](https://arcc.ist.ucf.edu/index.php/help/tutorials)
* [ARCC Video Tutorials](https://youtube.com/playlist?list=PLla7wVlbY2ISTBJJO588nkLQPntoTr0ex&si=12tYVBbwU5igOYjS)

# ARCC Hostnames/Addresses
* Stokes (general computing cluster): stokes.ist.ucf.edu
* Newton (GPU cluster): newton.ist.ucf.edu
  
# Requirements
To access a cluster, you must have the following:
* UCF NID
* Registered ARCC Account
* Be on the UCF Network (WiFi, LAN, or VPN)
  * [UCF VPN Instructions](https://ucfvpn-1.vpn.ucf.edu/+CSCOE+/logon.html?a0=15&a1=&a2=&a3=1#form_title_text)
 
# Software
To interact with a cluster, you should use a terminal software.
## Terminal:
* Windows: [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)
* Mac: Built in Terminal application

## FTP Client (transfer files) FileZilla:
* [Windows](https://filezilla-project.org/download.php?platform=win64) : Not necessary if using MobaXterm.
* [MacOS](https://filezilla-project.org/download.php?platform=osx)

# Connecting through a Terminal:
[Tutorial](https://arcc.ist.ucf.edu/index.php/help/tutorials/logging-into-arcc-clusters)

If you are using a terminal/command-line interface to connect, use the following commands:
1) Navigate to the folder where you keys are: `cd [PATH_TO_YOUR_KEY]`
2) Mac/Linux Only: Set the permissions on your key (only need to do once): `chmod 600 ida_rsa`
3) Connect with SSH: `ssh -Y -i PPK_KEY_FILE_NAME YOUR_USERNAME@stokes.ist.ucf.edu`
    * `ssh -Y -i ida_rsa userid@stokes.ist.ucf.edu`
  
# Modules
Modules are software packages that are available on the cluster, so you do not need to download them. There are over 150 packages available, including compilers and interpreters (python, anaconda, GCC, R, mathlab, etc.)
* List all available modules: `module avail`
* List python versions available: `module avail python`
* List anaconda versions available: `module avail anaconda`
* Load python 3.8: `module load python/python-3.8.0-gcc-9.1.0`
* List loaded modules: `module list`
* Unload python: `module unload python`
* Load multiple modules: `module load python gcc`
* Unload all loaded modules: `module purge`
