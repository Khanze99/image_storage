# image_storage

Разработать REST API сервер для хранения фотографий. Сервер предполагает наличие двух запросов, с помощью которых можно будет отправлять
для хранения фотографии и просматривать все добавленные ранее фотографии. Помимо запросов требуется реализовать панель администратора,
в которой можно просматривать добавленные фотографии.


1. Download zip/clone repository
2. docker-compose up --build
3. docker exec -it CONTAINER_ID bash
4. python3 manage.py migrate
5. python3 manage.py collectstatic
