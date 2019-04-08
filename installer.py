import os 

os.system('conda --version > test.txt') 

f = open('test.txt', 'r')
s = f.read()
print(s)
if '4.' in s: 
    conda_install = True 
else: 
    conda_install = False 

print(conda_install)
os.system('rm test.txt') 
if not conda_install: 
    os.system('wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh; bash Anaconda3-2019.03-Linux-x86_64.sh;') 

os.system('conda list | grep pytorch > test.txt') 
if '1.0.1' in open('test.txt', 'r').read(): 
    pytorch_install = True 
else: 
    pytorch_install = False 

if not pytorch_install: 
    os.system('conda install pytorch torchvision cudatoolkit=10.0 -c pytorch') 


