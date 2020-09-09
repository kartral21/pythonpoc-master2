FROM python:3.6

WORKDIR /app

COPY . ./
COPY atfpoc.conf /opt/settings/

#RUN commands
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

RUN cd app && nosetests tests --with-coverage --cover-erase --cover-package=source --cover-html

EXPOSE 8081

#RUN app
RUN cd app && export FLASK_APP=run.py
RUN cd app && flask run

