1. Create the project folder, i.e., ccnshs-80
2. Add a requirements.txt file with a content:
    "django>=3.2,<3.3"
3. Save the workspace inside the project folder and name the workspace the same as he project, ccnshs-80
4. Add the python extension (the one from Intellesense) in VS Code
5. Go to terminal within VS Code (Ctrl - ~)
6. Create the virtual env:
    python3 -m venv .
7. Set the python interpreter in VS Code to the one in bin/python inside the venv
8. Install django from the requirements.txt
    pip install -r requirements.txt
9. Create the django project:
    python -m django startproject ccnshs80 .
10. Create a git repo
    git init
    (Add a gitignore from here: https://github.com/github/gitignore/)
    git add --all
    git commit -m "Initial commit"
    (When pushing to github, do not add .gitignore and readme)