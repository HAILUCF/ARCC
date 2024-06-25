# ARCC Orientation
Instructions on getting started on UCF's Advanced Research Computing Center's high-performance computing clusters.

* [ARCC Home Page](https://arcc.ist.ucf.edu/)
* [ARCC Tutorials](https://arcc.ist.ucf.edu/index.php/help/tutorials)
* [ARCC Video Tutorials](https://youtube.com/playlist?list=PLla7wVlbY2ISTBJJO588nkLQPntoTr0ex&si=12tYVBbwU5igOYjS)

# ARCC Hostnames/Addresses
* Stokes (general computing cluster): _stokes.ist.ucf.edu_
* Newton (GPU cluster): _newton.ist.ucf.edu_
  
# Requirements
To access a cluster, you must have the following:
* UCF NID
* Registered ARCC Account. [Sign-up Here](https://arcc.ist.ucf.edu/index.php/accounts/user-registration-form?view=form)
* Be on the UCF Network (WiFi, LAN, or VPN)
  * [UCF VPN Instructions](https://ucfvpn-1.vpn.ucf.edu/+CSCOE+/logon.html?a0=15&a1=&a2=&a3=1#form_title_text)
* Your private key (_ida\_rsa_) and passphrase.
 
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
[Modules Tutorial](https://arcc.ist.ucf.edu/index.php/help/tutorials/module-system)

Modules are software packages that are available on the cluster, so you do not need to download them. There are over 150 packages available, including compilers and interpreters (python, anaconda, GCC, R, mathlab, etc.) To use a module, you must first load it. Below are commands to list, load, and unload modules.
* List all available modules: `module avail`
* List python versions available: `module avail python`
* List anaconda versions available: `module avail anaconda`
* Load python 3.8: `module load python/python-3.8.0-gcc-9.1.0`
* List loaded modules: `module list`
* Unload python: `module unload python`
* Load multiple modules: `module load python gcc`
* Unload all loaded modules: `module purge`

# SLURM
[SLURM Tutorial](https://arcc.ist.ucf.edu/index.php/help/tutorials/job-submission-within-the-arcc)

SLURM is the job scheduler used to submit jobs to the cluster. You should not run jobs directly on the cluster without scheduling it. Here are some SLURM commands
* Show node availability: `sinfo`
* View running jobs: `squeue`
* View your running jobs: `squeue -u USERID`
* Submit a job: `sbatch helloworld.slurm`
* Cancel a job: `scancel JOB_ID`
