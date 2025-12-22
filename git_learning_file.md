Git is a powerful version control 
system widely used in software development to track changes, collaborate
 on projects, and manage code efficiently. Understanding the basic 
concepts and commands in Git is important for any developer. This 
article will cover the fundamental concepts and some of the most Useful 
Git Commands and Basic Concepts to help you get started.

Basic Concepts
1. Repository (Repo)
A repository
 is a storage space where your project's files and their revision 
history are kept. It can be local (on your computer) or remote (on a 
server).

2. Commit
A commit
 represents a snapshot of your repository at a specific point in time. 
Each commit has a unique SHA-1 hash identifier and includes a message 
describing the changes.

3. Branch
A branch
 is a parallel version of your repository. It allows you to work on 
different features or fixes without affecting the main codebase. The 
default branch in a new repository is usually called master or main.

4. Merge
Merging is the process of combining changes from one branch into another. It helps integrate the work done in different branches.
5. Clone
Cloning is the process of creating a copy of a remote repository on your local machine.

6. Remote
A remote is a common repository that all team members use to exchange their changes.

7. Staging Area / Index
The staging area (or index) is where you prepare changes to be committed. It allows you to review and organize changes before making a commit.

8. Working Directory
The working directory is where you modify your files. Changes in the working directory are not tracked by Git until you stage them.

Setting up our Git Repository
Let’s make a Git Repository first of all and learn about all these Git commands.
Let’s start by creating a folder where we can have 
different files like a text file, an Excel Database file, a Markdown 
File, a Folder consisting of Source Code files (An actual Project may 
have many different files).
But right now for simplicity's sake let’s keep these files empty.
We can use Git Bash to write Git commands or we can also use VS Code which has built-in support for Git. You can install Git here or you can check out How to integrate Git Bash with Visual Studio Code?. If you are using Git for the first time to know how to set up Git Bash.
Now let’s open Git Bash by Right-clicking and selecting “Git Bash Here”.
Initializing our Git Repository
Here we are initializing our Git Repository or you can say we are making our directory a Git Repository.
Note: If you already have made a Git Repository then don’t use this command again else all the changes that you have made to this Repository will get re-initialized.
Staging Files Initially
We are staging these files initially so that now we can track them using Git.
Creating Initial Commit
Let’s make our Initial Commit to our Repository.
Now let’s take a look at some of the useful Git commands for merging branches, forking a Repository, Renaming, and Deleting files using the command line, and much more.

Useful Git Commands
1. git init
Initializes a new Git repository in the current directory.

git init
2. git clone
Creates a copy of an existing remote repository.

git clone <repository-url>
3. git status
Displays
 the state of the working directory and the staging area. It shows which
 changes have been staged, which haven't, and which files are not being 
tracked by Git.

git status
4. git add
Adds changes from the working directory to the staging area.

git add <file>
To add all changes:

git add .
5. git commit
Records the changes in the staging area in the repository with a descriptive message.

git commit -m "Your commit message"
6. git log
Shows the commit history for the current branch.

git log
7. git branch
Lists all branches in the repository. The * indicates the current branch.

git branch
Creates a new branch:

git branch <branch-name>
8. git checkout
Switches to a different branch or restores files in the working directory.

git checkout <branch-name>
9. git merge
Merges changes from one branch into the current branch.

git merge <branch-name>
10. git pull
Fetches changes from a remote repository and merges them into the current branch.

git pull origin <branch-name>
11. git push
Uploads local commits to a remote repository.

git push origin <branch-name>
12. git remote
Manages the set of tracked repositories.
To add a new remote:

git remote add <name> <url>
13. git fetch
Downloads objects and refs from another repository.

git fetch
14. git reset
Resets the current HEAD to a specified state. It can be used to unstage changes or move the branch pointer.
To unstage changes:

git reset <file>
15. git diff
Shows changes between commits, commit and working tree, etc.
To see changes in the working directory:

git diff
To see changes between the working directory and the index:

git diff --cached
16. git stash
Temporarily shelves changes in the working directory that are not ready to be committed.

git stash
To apply stashed changes:

git stash apply
17. git tag
Creates a tag to mark a specific point in the repository's history, typically used for releases.

git tag <tag-name>
18. git blame
Shows who made changes to each line in a file.

git blame <file>
19. git reflog
Records updates to the tip of branches. It’s useful for recovering lost commits.

git reflog
20. git rm
Removes files from the working directory and the index.

git rm <file>
                