FROM python:3.6

WORKDIR /app

COPY . ./
COPY atfpoc.conf /opt/settings/

#RUN commands
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

#RUN nosetests tests --with-coverage --cover-erase --cover-package=flaskpoc --cover-html

EXPOSE 8081

#RUN cd pythonpoc
RUN cd app && export FLASK_APP=run.py
RUN cd app && flask run

