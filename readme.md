# **DEVELOPMENT FINISHED, DEPLOYMENT PENDING DUE TO EXCEEDING FILE SIZE OF 300MB**

# This project aims to analyze depressive or non depressive messages using the depressive sentiment dataset from. Built with React.js, Flask, Scikit-Learn

# requirements:
1. git
2. conda
3. python

# Source code usage
1. assuming git is installed clone repository by running `git clone https://github.com/08Aristodemus24/<repo name>`
2. assuming conda is also installed run `conda create -n <environment name e.g. some-environment-name> python=3.11.5`. Note python version should be `3.11.5` for the to be created conda environment to avoid dependency/package incompatibility.
3. run `conda activate <environment name used>` or `activate <environment name used>`.
4. run `conda list -e` to see list of installed packages. If pip is not yet installed run conda install pip, otherwise skip this step and move to step 5.
5. navigate to directory containing the `requirements.txt` file.
5. run `pip install -r requirements.txt` inside the directory containing the `requirements.txt` file
6. after installing packages/dependencies run `python index.py` while in this directory to run app locally

# App usage:
1. you can run the app via command: `python index.py`
2. once run navigate to local host url `http://127.0.0.1:5000/`
3. In control panel of app it will have 2 inputs: The dropdown field which allows the user to choose the gradient boosted model to test for different outcomes or performance of each model, and the message field which allows user to enter a certain message or sentence and then upload it to the server for further preprocessing and subsequently fed to the chosen trained model to predict a probability of whether such a message is classified as depressive or non depressive

# File structure:
```
|- client-side
    |- public
    |- src
        |- assets
            |- mediafiles
        |- boards
            |- *.png/jpg/jpeg/gig
        |- components
            |- *.svelte/jsx
        |- App.svelte/jsx
        |- index.css
        |- main.js
        |- vite-env.d.ts
    |- index.html
    |- package.json
    |- package-lock.json
    |- ...
|- server-side
    |- modelling
        |- data
        |- figures & images
            |- *.png/jpg/jpeg/gif
        |- final
            |- misc
            |- models
            |- weights
        |- metrics
            |- __init__.py
            |- custom.py
        |- models
            |- __init__.py
            |- arcs.py
        |- research papers & articles
            |- *.pdf
        |- saved
            |- misc
            |- models
            |- weights
        |- utilities
            |- __init__.py
            |- loaders.py
            |- preprocessors.py
            |- visualizers.py
        |- __init__.py
        |- experimentation.ipynb (where data loading, preprocessing, visualization, as well as model training, hyper parameter tuning, testing, and evaluation is done)
    |- static
        |- assets
            |- *.js
            |- *.css
        |- index.html
    |- index.py
    |- server.py
    |- requirements.txt
|- demo-video.mp4
|- .gitignore
|- readme.md
```