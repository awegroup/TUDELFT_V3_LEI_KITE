# Introduction

Hi! Welcome to this Python Template, this `README_dev.md` contains instructions on the intended usage of this python template.

## Getting-Started
1. Copy the template into a new repository, and edit the name to your project name
2. On your pc (locally) create a folder for your code project
3. Open this folder with your favorite editor (e.g. VSCode) and within it create a new python venv
4. Clone the just created repository into this folder, i.e. run `git clone ???`
5. Make some changes, and create your first commit see: ...

## Setting-Up the Project
- [ ] Update 

## Proposed-Workflow

### Generic
- Work with a main, develop and feature branches
- Write user settings in a `.yaml` file
- Don't use any hardcode inside your source folder
- Write scripts that should be run inside notebooks
- The other folders should only contain functions or data


### Steps for implementing a new feature
1. Create an issue on GitHub
2. Create a branch from this issue and change the branch source to `develop`
3. Use provided cmds to checkout this branch locally
4. --- Implement your new feature---
5. Verify nothing broke using pytest
```
  pytest
```
7. git add, git commit (with # to current Issue number), git push
```
  git add .
  git commit -m "#<number> <message>"
  git push
```
7. Create a pull-request, with `base:develop`, to merge this feature branch and close this issue
9. Update branch information locally using `git fetch --prune`, pull in new info `git pull origin develop` and delete branch locally using `git branch -d <enter branch name>`
```
  git fetch --prune
  git pull --all
  git checkout develop
  git pull
```
9. Once merged on the remote and locally, delete this feature branch on the remote (see pull-request) and locally using 
```
  git branch -d <branch name>
```
10. Close issue


## Explanation of folders/files
- `.gitkeep` is placed such that the empty folder show on GitHub, without this file would be automatically ignored and the project structure would not be clear. Once other files are present inside this folder, this file can be deleted.
- The folders `data/`, `processed_data/`, and `results/` have been added to the `.gitignore` file, as they are expected to contain 
  - large files that should not be uploaded to GitHub
  - confidential data that should not be uploaded to GitHub
  - generated data that can be recreated
  - generated results that can be recreated
