Парсинг букмекерской конторы Париматч.<br>
Париматч без выполнения javascript на странице не отдает коэффициенты, поэтому get-запросом их не забрать. Чтобы получить данные, страница открывается selenium-ом в браузере. Парсинг разных видов спорта выполняется асинхронно с asyncio. Данные по спортивным событиям в JSON-формате будут записаны в файл "parsed_parimatch.json" в рабочей директории.

Для запуска парсера выполнить команды:<br>

cd parimatch_parser<br>
docker build -t parimatch_parser .<br>
docker run --rm -v /dev/shm:/dev/shm -v "$(pwd)":/parser parimatch_parser
