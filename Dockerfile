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
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "index.py"]

