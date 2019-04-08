# Pytorch-tutorial
Uecker Fast tutorial on Pytorch usage for Neural Network
# Installation of Anaconda/Miniconda on Linux (Mikneto)
- First, download the Anaconda installer for Python 3.7 on Linux:

  `wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh`
- Install Anaconda by `bash Anaconda3-2019.03-Linux-x86_64.sh`. Follow the instuction on the website is a good option. Hopefully, Anaconda is successfully installed. You can try `jupyter notebook` to test wheter it works and follow the instruction on (https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server) to run notbook remotely.

# Installation of Pytorch
- First check the cuda version of the system by typing: `nvcc --version`, you will find the cuda version (which should be 10.0 on Mikn]eto)
- Then you can install pytorch through conda, check the command on (https://pytorch.org/), for Mikneto, it is:

  `conda install pytorch torchvision cudatoolkit=10.0 -c pytorch`
- Congrats! So far, Pytorch is successfully installed, it's very easy, right?
