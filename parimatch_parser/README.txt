Для запуска парсера выполнить команды:

cd parimatch_parser
docker build -t parimatch_parser .
docker run -v /dev/shm:/dev/shm -v "$(pwd)":/parser parimatch_parser
