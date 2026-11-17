# Online Banking System

## Aim of the Experiment
To demonstrate creating a Git merge conflict in the Account Management module of an Online Banking System and manually resolving it.

## Account Management Module Description
The `account.py` module manages bank accounts with the following key functions:
- `account_status()`: Displays current operational status of the account.
- `account_details()`: Displays account number, holder name, and balance.
- `activate_account()`: Activates the user account.
- `suspend_account()`: Suspends the user account.
- `verify_account()`: Marks the account as verified.

## Git Commands Used
- `git init`: Initialize the local Git repository.
- `git branch -M main`: Set default branch to main.
- `git add .`: Stage files for commit.
- `git commit -m "Initial commit"`: Commit staged changes.
- `git checkout -b feature`: Create and switch to the feature branch.
- `git checkout main`: Switch back to the main branch.
- `git merge feature`: Merge changes from feature branch into main branch.
- `git status`: Check the status of working tree and conflicts.
- `git log --graph --oneline --all`: View commit history and branch graph.
- `git push origin main feature`: Push both branches to GitHub repository.

## Merge Conflict Creation Process
1. On the `main` branch, the initial account status was set to `"Active"`.
2. A branch named `feature` was created, where `account_status()` in `account.py` was updated to `"Suspended"`, followed by a commit with message `"Initial commit"`.
3. Returning to the `main` branch, the exact same line in `account.py` was modified to `"Verified"`, followed by a commit with message `"Initial commit"`.
4. Merging `feature` into `main` (`git merge feature`) resulted in a content conflict on the status assignment line in `account.py`.

## Manual Merge Conflict Resolution
During the merge, Git inserted conflict markers:
```python
<<<<<<< HEAD
    status = "Verified"
=======
    status = "Suspended"
>>>>>>> feature
```
The conflict was manually resolved by removing the conflict markers and combining the status as:
```python
    status = "Active and Verified"
```
The resolved file was staged using `git add account.py` and committed using `git commit -m "Initial commit"`.

## Expected Output
```
Account Status: Active and Verified
```
