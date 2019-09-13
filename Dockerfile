FROM python:3
COPY . /project
WORKDIR project
RUN pip3 install -r requirements.txt
CMD ['gunicorn']