## Тестовое задание

1. Клонировать репозиторий.
2. Установить все пакеты из файла requirements.txt командой "pip install -r requirements.txt"
3. Если у вас Ubuntu и установлены redis и postresql то следует остановить их перед запуском:
- sudo systemctl stop postgresql
- sudo service redis-server stop

4. Собрать образ командой sudo docker-compose build
5. Запустить docker командой sudo docker-compose up
6. Выполнить sudo docker-compose exec app python manage.py csu



* сслылки для пользования 
* http://localhost:8001/admin для входа в админку
* http://localhost:8001/chat/ для выбора чата
* http://localhost:8001/docs/ документация