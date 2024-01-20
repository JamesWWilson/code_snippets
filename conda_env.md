# Create and Manage Unique Conda Environments on Mac OSX

### Install Honeybrew

### Install conda

```
brew install miniconda
```

### Find your directory of pre-built .yaml file and create environment
```
cd ~/..
conda env create -f your_env.yml
```

### NOTE, you may need to init conda. Follow these steps:
```
conda env list
echo $SHELL
conda init <YOUR SHELL>
```
### Turn your environment on and off 
```
conda activate your_env 
conda deactivate
```
### Write a requriements file for your active conda env
```
conda list -e > /path/to/your/folder/requirements.txt
```
### Remove conda environments as they are no longer needed
```
conda env remove --name your_environment_name
```




