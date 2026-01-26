# **DEVELOPMENT FINISHED, DEPLOYMENT PENDING DUE TO EXCEEDING FILE SIZE OF 300MB**
1. run docker build -t depressive-sentiment-analyzer . to build image
2. once image is built run docker run -p 5000:5000 to run image as container
3. 


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

# Insights:
* inside the `vercel.json` file in our root folder containing `index.py` or the script that runs the flask app, why we don't need to explicitly mention or state in vercel the `pip install -r requirements.txt` command is because we already provide vercel the information to use its own python somehow to do this installation for us. By virtue of mentioning python via `@vercel/python` we state that vercel automatically install the python dependencies the app has by using `pip install -r requirements.txt`
``` 
{
    "version": 2,
    "builds": [
        { "src": "./index.py", "use": "@vercel/python" }
    ],
    "routes": [
        { "src": "/(.*)", "dest": "/" }
    ]
}
```

* deployment issues:
could be solved by using google cloud platform, azure, or aws, by using higher storage capacity for app. The idea is we would set up a remote server that can be accessed locally in your machine. This server will host the app you have by first requiring you to copy the necessaary files to this server by accessing it via your local machine kind of like virtual machines, which will require an ssh key.

once files are copied to the server we can run the app remotely using our local machine, and once the app is running on the server it is live, and from here the idea is we can somehow change its domain name such that it runs not only with a localhost:5000 etc. domain but with a searchable one

https://www.youtube.com/watch?v=5gSG5jwOJSY for deploying app to aws ec2 instance, or a virtual server you can access via ssh keys

# Errors To Resolve:
```
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 1466, in wsgi_app

    response = self.handle_exception(e)

               ^^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask_cors/extension.py", line 176, in wrapped_function

    return cors_after_request(app.make_response(f(*args, **kwargs)))

                                                ^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi_app

    response = self.full_dispatch_request()

               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 872, in full_dispatch_request

    rv = self.handle_user_exception(e)

         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask_cors/extension.py", line 176, in wrapped_function

    return cors_after_request(app.make_response(f(*args, **kwargs)))

                                                ^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 870, in full_dispatch_request

    rv = self.dispatch_request()

         ^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 855, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/server-side/server.py", line 152, in predict

    Y_preds = model.predict(features)

              ^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/xgboost/sklearn.py", line 1553, in predict

    class_probs = super().predict(

                  ^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/xgboost/sklearn.py", line 1168, in predict

    predts = self.get_booster().inplace_predict(

             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.12/site-packages/xgboost/core.py", line 2428, in inplace_predict

    raise ValueError(

ValueError: Feature shape mismatch, expected: 9014, got 11361
```

this is due to scikit learn now changing its number of features from 11355 to now 9008, we had originally 11355 + 6 hand made features in training our model, but because tfidf in certain version maybe now went from 11355 to 9008 for our dataset, the total features would now just be 9008 + 6 hand made features or 9014 which our model did not train on

we need to implement also here a way of reimplementing feature engineering to include n punctuations, and rebalancing our dataset to the right amount of classes 

so kaya pala pati docker nag eerror kasi the predict function doesn't actually return anything because the error is intercepted quickly