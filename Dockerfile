FROM python:3.8.0

# Set the file maintainer (your name - the file's author)
MAINTAINER Babu

# install the python requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

## run the app 
ADD app.py app.py

## expose the port
EXPOSE 5000

## start the command
CMD ["python", "app.py"]
