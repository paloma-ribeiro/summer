FROM python:3.9

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY . .

# install dependencies
RUN pip install -r requirements/dev.txt

# command to run on container start
CMD [ "python", "./main.py" ]