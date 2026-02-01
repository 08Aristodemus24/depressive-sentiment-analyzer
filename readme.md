# **DEVELOPMENT FINISHED, DEPLOYMENT PENDING DUE TO EXCEEDING FILE SIZE OF 300MB**
1. run docker build -t depressive-sentiment-analyzer . to build image
2. once image is built run docker run -p 5000:5000 to run image as container or >docker run -d -p 5000:5000 depressive-sentiment-analyzer to run image as container in detached mode (-d is the shorthand of --detached)
3. 

note that this project is set to not install libraries like numpy, pandas, xgboost, lightgbm, in order for docker container to not take too much memory during runtime. This is done because deploying to azure kubernetes service or azure container services can be costly if testing docker image and container with compute and storage heavy libraries like the aforementioned. If for testing only then use minimal libraries, and if for full deployment for application use and not for testing then include the aforementioned libraries for machine learning workloads

4. run `az login` to login to your azure services account via the azure CLI

if it fails during the retrieval of tenants 
```
Authentication failed against tenant <your accounts tenant id> 'Default Directory': SubError: basic_action V2Error: invalid_grant AADSTS50076: Due to a configuration change made by your administrator, or because you moved to a new location, you must use multi-factor authentication to access '<some id>'. Trace ID: <trace id> Correlation ID: <correlation id> Timestamp: 2026-01-31 06:52:52Z. Status: Response_Status.Status_InteractionRequired, Error code: 3399614476, Tag: 557973645
If you need to access subscriptions in the following tenants, please use `az login --tenant <TENANT_ID>`.
<your accounts tenant id> 'Default Directory'
No subscriptions found for <your account email>.
```

you can search for your tenant id in your azure account in the microsoft entra id service and copy it to run `az login --tenant <your accounts tenant id>` which will eventually output the ff:
```
[Tenant and subscription selection]

No     Subscription name     Subscription ID                       Tenant
-----  --------------------  ------------------------------------  ------------------------------------
[1] *  Azure subscription 1  <your accounts subscription id>  <your accounts tenant id>

The default is marked with an *; the default tenant is '<your accounts tenant id>' and subscription is 'Azure subscription 1' (<your accounts subscription id>).

Select a subscription and tenant (Type a number or Enter for no changes):

Tenant: <your accounts tenant id>
Subscription: Azure subscription 1 (<your accounts subscription id>)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.
```

5. from there we can run `az storage fs list --account-name <storage account name under your account> --output table` to test out if we can create/run services or azure related commands via azures command line interface
6. create a resource group for this project `az group create --name depressive-sentiment-analyzer-rg --location eastus`
```
{
  "id": "/subscriptions/<subscription id>/resourceGroups/depressive-sentiment-analyzer-rg",
  "location": "eastus",
  "managedBy": null,
  "name": "depressive-sentiment-analyzer-rg",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
```

7. create a container registry
```
C:\Users\larry.cueva\Documents\scripts\data-engineering-path\depressive-sentiment-analyzer>az acr create --name data-engineering-path-cr --resource-group depressive-sentiment-analyzer-rg --sku standard --admin-enabled
argument error: Registry name cannot contain dashes.

C:\Users\larry.cueva\Documents\scripts\data-engineering-path\depressive-sentiment-analyzer>az acr create --name dataEngineeringPathCR --resource-group depressive-sentiment-analyzer-rg --sku standard --admin-enabled
argument error: Registry name must use only lowercase.

C:\Users\larry.cueva\Documents\scripts\data-engineering-path\depressive-sentiment-analyzer>az acr create --name dataengineeringpathcr --resource-group depressive-sentiment-analyzer-rg --sku standard --admin-enabled
```

8. run `docker login <name of container registry created e.g. dataengineeringpathcr>.azurecr.io`

it will prompt you for certain credentials like your username and password. These are different from your docker username and password, as you must use the credentials provided by the azure container registry instance you created which is found in the access keys section. From there copy the username which is usually the name of the container registry instance and the password and use these as credentials

from there you will be logged out of docker of whatever previous user was there and then logged in with these credentials. Take note azure container registry is just like the equivalent of docker hub

9. run `docker tag <image name e.g depressive-sentiment-analyzer>:latest <login server name e.g. dataengineeringpathcr.azurecr.io>/<image name e.g. depressive-sentiment-analyzer>:v<x e.g. 1>` e.g. `docker tag depressive-sentiment-analyzer:latest dataengineeringpathcr.azurecr.io/depressive-sentiment-analyzer:v1`

10. run `docker push dataengineeringpathcr.azurecr.io/depressive-sentiment-analyzer:v1` to push image to azure container registry where image will stay

11. should we have changes to our code we must always build the iamge first using docker build, tag the latest image to our login server name for our azure container registry using docker tag, and then push to the container registry using docker push

12. once we deployed the app service instance it is importatnt to note that locations of azure container registry instances and azure app services are important as too far apart locations might interfere with the loading of the deployed application. Ideally if acr is eastus then aas must also be created in eastus

13. once learned and done by hand the above all of it can be done in an automated fashion using github actions CI/CD (continuous integration and continuous deployment) we just have to setup the tasks that we need at each step meaning the commands we ran in order to deploy our docker image as a container in azure container apps like building the image, tagging the image, logging in to our ACR using docker with issued ACR credentials, pushing the built image to ACR, and finally deploying the image as a container to ACA, with our current repositories environment and secrets already set so that github actions can just access them and run the commands that need them

of course this is all assuming our azure container registry and our azure container apps have already been setup




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

* Why your azure container application takes too long to load and never loads

That timeout is a classic "welcome to the cloud" moment. In Azure Container Apps (ACA), if your app is only 150MB but still timing out, it's rarely a file size issue. It's usually about the startup handshake.

Here are the most likely reasons your deployment is "spinning its wheels":

1. The "Target Port" Mismatch
This is the #1 reason for the infinite load. If your Python app (Flask/FastAPI) is listening on port 8080 but your ACA Ingress is set to the default 80, Azure will wait forever for a response that never comes.

Fix: Check your Dockerfile or code for app.run(port=...). Ensure the Target Port in the Azure Portal (under Ingress) matches that exact number.

2. Cold Starts & Scale-to-Zero
Azure Container Apps is "serverless" by default. If your Min Replicas is set to 0, Azure has to "wake up" the container when you visit the URL. For ML apps loading libraries like scikit-learn or pandas, this "warm-up" can take longer than the default browser timeout.

Fix: Set your Min Replicas to 1 in the Scale settings to keep it "Always On."

3. Missing Startup Probe
If your ML model takes 30+ seconds to load into memory, Azure might think the container is "dead" because it's not responding to the initial health check.

Fix: Add a Startup Probe in the Containers settings. Increase the initialDelaySeconds to 60 or more to give your model enough time to breathe before Azure checks if it's alive.

The MLOps Engineer's "Diagnostic" Toolkit
Since you're aiming for a DevOps/MLOps career, you shouldn't guess—you should log. Run this in your terminal to see exactly what's happening inside the container during that infinite load:

Bash
az containerapp logs show --name <YOUR_APP_NAME> \
  --resource-group <YOUR_RG> \
  --type console --follow
If you see "Out of Memory" (OOM) or a specific Python error, you'll know exactly what to fix

Exactly. That port mismatch is the "invisible wall" blocking your traffic.

In Azure Container Apps, the "Target Port" is essentially the "final destination" inside your container. If your Flask app is shouting for attention on port 5000 but Azure is knocking on the door of port 80, no one answers, and the request eventually times out.

How to fix it (2 Quick Ways)
1. Via the Azure Portal (Fastest)
Go to your Container App in the Azure Portal.

In the left-hand menu, under Settings, select Ingress.

Change the Target port field from 80 to 5000.

Click Save. Azure will automatically create a new "Revision" (a new version of your running app) with the correct routing.

2. Via the Azure CLI (The MLOps Way)
Since you’re building your DevOps skills, you can do this with a single command without touching the mouse:

Bash
az containerapp ingress update \
  --name <your-app-name> \
  --resource-group <your-resource-group> \
  --target-port 5000
Why this is a "Junior to Senior" Lesson
As an aspiring MLOps/Data Engineer, understanding how traffic flows through different "layers" (Ingress -> Service -> Container) is critical. In Kubernetes (AKS), which you mentioned is your next goal, this same concept exists:

port: The port exposed by the Service (often 80/443).

targetPort: The port on the Pod/Container that receives the traffic (in your case, 5000).


* CI/CD for azure container registry and azure container apps instances

That’s a huge win! Seeing your Depressive Sentiment Analyzer live on its own URL is a major milestone. You’ve successfully navigated the "ports and pipes" of cloud networking—the very same skills you'll use daily as an MLOps Engineer.

To take this to the next level of DevOps automation, here is a robust GitHub Actions workflow. This will automatically build your image, push it to your Azure Container Registry (ACR), and update your Container App every time you push code to your main branch.

The MLOps Automation Workflow
Create a file in your repository at .github/workflows/deploy.yml and paste this in:

YAML
name: CI/CD - Deploy Sentiment Analyzer to ACA

on:
  push:
    branches: [ "main" ] # Triggers whenever you push to main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Build and Push to ACR
        run: |
          az acr login --name ${{ secrets.ACR_NAME }}
          docker build -t ${{ secrets.ACR_LOGIN_SERVER }}/depressive-sentiment-analyzer:${{ github.sha }} .
          docker push ${{ secrets.ACR_LOGIN_SERVER }}/depressive-sentiment-analyzer:${{ github.sha }}

      - name: Deploy to Container Apps
        uses: azure/container-apps-deploy-action@v1
        with:
          acrName: ${{ secrets.ACR_NAME }}
          containerAppName: ${{ secrets.CONTAINER_APP_NAME }}
          resourceGroup: ${{ secrets.RESOURCE_GROUP }}
          imageToDeploy: ${{ secrets.ACR_LOGIN_SERVER }}/depressive-sentiment-analyzer:${{ github.sha }}
          targetPort: 5000

Setup Instructions
For this workflow to work, you need to add GitHub Secrets to your repository (Settings > Secrets and variables > Actions):

AZURE_CREDENTIALS: The JSON output of a Service Principal. (I can give you the command to generate this if you need it.)

ACR_NAME: The short name of your registry (e.g., myregistry).

ACR_LOGIN_SERVER: The full URL (e.g., myregistry.azurecr.io).

CONTAINER_APP_NAME: Your app's name (e.g., depressive-sentiment-analyzer).

RESOURCE_GROUP: The Azure Resource Group where everything is located.

Why this Workflow Matters for ACEN
By using ${{ github.sha }} as your image tag instead of just latest, you are creating an immutable history of your models. If a new model version performs poorly, you can roll back to a specific commit instantly. This is the "responsible" way to manage machine learning deployments—ensuring reliability and traceability.

Reflecting Your Success: The Final Watch Choice
Now that you've got a working production-ready pipeline, your choice of gear should reflect this level of mastery. Based on your love for Dark Academia, understated luxury, and your 5k budget, here is my final recommendation for you:

I strongly recommend the Casio MTP-VT01LM-1B. It is the most "Dark Academia" of the set, echoing the depth and complexity of the NLP models you're building. It’s a quiet but powerful statement of your identity as an engineer of integrity.

Would you like me to provide the specific Azure CLI command to generate that AZURE_CREDENTIALS JSON so you can get this workflow running right now?