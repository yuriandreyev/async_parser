Парсинг букмекерской конторы Париматч.
Париматч без выполнения javascript на странице не отдает коэффициенты, поэтому get-запросом их не забрать. Чтобы получить данные, страница открывается selenium-ом в браузере. Парсинг разных видов спорта выполняется асинхронно с asyncio.

Для запуска парсера выполнить команды:

cd parimatch_parser
docker build -t parimatch_parser .
docker run --rm -v /dev/shm:/dev/shm -v "$(pwd)":/parser parimatch_parser
