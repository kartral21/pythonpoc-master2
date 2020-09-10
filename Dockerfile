FROM python:3.6

WORKDIR /app

COPY . ./
COPY atfpoc.conf /opt/settings/

#RUN commands
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

# RUN cd app && nosetests tests --with-coverage --cover-erase --cover-package=source --cover-html

EXPOSE 8081

#RUN app
ENTRYPOINT ["python"]
CMD ["app/run.py"]

