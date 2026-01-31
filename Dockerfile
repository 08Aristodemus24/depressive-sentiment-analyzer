FROM python:3.12-slim-bookworm

# install apt-utils to avoid dependency issues
# for apps that run C++ code e.g. lightgbm
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

# copy local server-side dir's contents into the newly made
# server-side dir in the docker container 
# this will also copy local machines path to 
# requirements.txt to containers directory
COPY server-side ./server-side

# switch to server-side directory
WORKDIR /server-side/


# install dependencies from requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt


# we essentially sa expose the port 5000 in the docker container
# so when we run docker run -p 80:5000 depressive-sentiment-analyzer
# we essentially say when this container is up and running
# on our end we want to access it at port 80, so port 80 in our
# local machine will bind to the exposed port 5000 in the container
EXPOSE 5000

CMD ["python", "index.py"]

