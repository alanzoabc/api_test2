FROM python:3.9
#base image
WORKDIR /pythonApp
#working directory
COPY ./requirements.txt /pythonApp/requirements.txt
#copying requirments to working directory
RUN pip install --upgrade --no-cache-dir  -r /pythonApp/requirements.txt
#Installing requirments for the app using pip
COPY ./app /pythonApp/app
#Copying app into directory
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#running the app in cmd