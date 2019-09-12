FROM python:3
COPY . .
RUN rm /etc/systemd/system/gunicorn.service
COPY ./gunicorn/gunicorn.service /etc/systemd/system/
RUN pip3 install -r requirements.txt
WORKDIR image_storage
EXPOSE 8000
CMD ['runserver']