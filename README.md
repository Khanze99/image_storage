# image_storage

Разработать REST API сервер для хранения фотографий. Сервер предпо-
лагает наличие двух запросов, с помощью которых можно будет отправлять
для хранения фотографии и просматривать все добавленные ранее фото-
графии. Помимо запросов требуется реализовать панель администратора,
в которой можно просматривать добавленные фотографии.


1. Download zip/clone repository
2. Create virtualenv with python3 (virtualenv -p python3 venv)
3. Activate virtualenv source venv/bin/activate
4. pip3 install -r requirements.txt (install required packages)
5. cd rest_api_storage
6. python3 manage.py migrate
7. python3 manage.py collectstatic
8. python3 manage.py runserver

-------------------With docker-------------------

1. Download zip/clone repository
2. docker-compose up --build
3. docker exec -it CONTAINER_ID bash
4. python3 manage.py migrate
5. python3 manage.py collectstatic
