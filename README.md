# Voyce
How to
* [Run the app](#how-to-run-the-app)
## How to run the app
* Fork this repo
* cd to the directory you want to save your file and run 
```
git clone https://github.com/Averyzhang761/Voyce_Project.git
```
* Create the new branch on your local machine (To make sure we don't change the master file before reviewing the change)
```
git branch <name_of_your_new_branch>
```
* See the exising branch:
```
git branch
```
* Switch in your branch :
```
 git checkout [name_of_your_new_branch]
```
* cd to voyce repo
```
cd Voyce_Project
```
* Create the virtual env
``` 
python3 -m venv venv
source venv/bin/activate
```
* Install dependencies (packages for the app)
```
pip install -r requirements.txt
```
* Run
```
python manage.py runserver
```
You should be able to see the website

## How to commit
Add the files to commit (use . to commit all files)
```
git add .
```
Commit the fields
```
git commit -m "Some message"
```
Push the branch on github :
```
git push origin [name_of_your_new_branch]
```
As we review on the change, we can merge the other branch:
```
git merge [name_of_your_new_branch]
```
Delete a branch on your local filesystem
```
git branch -d [name_of_your_new_branch]
```
## How to update your repo
Once the master repo has been updated, use
```
git pull origin master
```
to get up to date.

To get your branch up to date with the current master use
``` 
git checkout <your branch>
```
Up to date with the origin
```
git fetch
git rebase origin/master
```
