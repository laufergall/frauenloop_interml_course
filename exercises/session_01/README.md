# Session 1: Introduction to the course. Git basics

## Proposed tasks:

1. Make sure you have a GitHub account and [a SSH key set](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). Download and install [git](https://git-scm.com/downloads) if you have not yet.

2. Clone this repository

```bash
git clone <this repository URL>
```

3. Make a branch for you to work on, choose your branch name

```bash
git checkout -b branch_name
```

4. Add your participant's data to the [data/raw/course_participants.md](data/raw/course_participants.md) file.

5. Make a commit, choose your message

```bash
git add data/raw/course_participants.md
git commit -m "Add Laura participant data"
```

6. Push your branch

```bash
git push -u origin branch_name
```

7. Create a pull request

8. Review, approve, and merge another participant's pull request into the master branch

9. Pull to update your local master branch

```bash
git pull
```

## Next steps

1. Create a folder structure (can be inspired by this one) for your team data science project.

2. Start a new git repository.

```bash
git init
```

3. Make your first commit.

```bash
git add .
git commit -m "Initial commit"
```

4. Create an empty repo in GitHub.

5. Push the project to your create repo in GitHub.

```bash
git remote add origin <remote repository URL>
git push -u origin master
```

6. Protect the `master` branch, so that nobody is allowed to push directly to it.

From now on, collaborate with your team members on this project.

## Suggestions
* Always create branches, do not commit directly to master
* It is good practice to review each another's work before merging
* Add the data folder to the .gitignore file
* Add needed packages to requirements.txt as you go
