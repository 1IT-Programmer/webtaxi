Инструкция по сборке
Создайте структуру файлов как указано выше

Активируйте виртуальное окружение:

bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows
Установите зависимости:

bash
pip install django python-dotenv
Примените миграции:

bash
python manage.py makemigrations
python manage.py migrate
Создайте администратора:

bash
python manage.py createsuperuser
Запустите сервер:

bash
python manage.py runserver
Важные особенности реализации
Роутинг разделен между проектом и приложением

Декоратор role_required проверяет права доступа

Шаблоны наследуют базовую разметку из base.html

Переменные окружения защищают чувствительные данные

Админ-панель кастомизирована для удобного управления
