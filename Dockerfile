FROM python:3.6

WORKDIR /app

COPY . ./


#RUN commands
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
RUN cd pythonpoc
RUN pwd
RUN cd pythonpoc  && ls -lrt

#RUN nosetests tests --with-coverage --cover-erase --cover-package=flaskpoc --cover-html

EXPOSE 5000

#CMD [ "python3", "run.py" ]

#RUN cd pythonpoc
RUN cd pythonpoc && export FLASK_APP=run.py
RUN cd pythonpoc && flask run

