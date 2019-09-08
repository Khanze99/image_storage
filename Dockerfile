FROM python:3
COPY . .
RUN pip3 install -r requirements.txt
WORKDIR image_storage
EXPOSE 8000
CMD ['runserver']