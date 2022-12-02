# Create an SSH Key (primarily in BitBucket) 

### Create and Move Directory to .ssh

```
ls -lah 
mkdir .ssh
cd .ssh
```
### Create SSH Key
```
ssh-keygen -t rsa -C "firstname.lastname@company_email.com"
```

### Confirm your address
```
eval $(ssh-agent)
```
### Add your SSH Key
```
ssh-add id_rsa
```
### Print SSH Key to console
```
cat id_rsa.pub
```
### Copy and add SSH Key to Bitbucket

For this step, go to Bitbucket.com and click on your user profile in the top right. 
A pop-up will open and you will click on Personal Settings. From here, navigate to Security on the left and click on SSH Keys. 
Here you can add your SSH key. Please title is as the same name as the environment it ties to.
Done!

You can now clone repos from BitBucket to your repo. 




