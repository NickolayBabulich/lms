# LMS - проект в рамках изучения DRF (домашняя работа)

### О проекте:
- Тестовые данные для моделей представлены в файлах users_data.json и course_data.json
- Для загрузки тестовых данных необходимо ввести следующую команду:
- ``` python manage.py loaddata users_data.json ``` - Загрузка данных приложения пользователей
- ``` python manage.py loaddata course_data.json ``` - Загрузка данных приложения курсов
- логины и пароли:
  - суперпользователь: логин - admin@mailing.com / пароль - 1
  - модер: логин - moder@mailing.com / пароль - 1
  - пользователь: логин - man@mailing.com / пароль - 1

#### Выполнены задания 24.1
- Создан проект Django, подключен DRF, выполненны настройки
- Созданы приложения с моделями: Пользователи, Курс (Урок)
- Описаны контроллеры CRUD, для модели Course с использованием ViewSets, для модели Lesson с использованием Generics
- Реализован CRUD для модели Users на основе ViewSets

#### Выполнены задания 24.2
- Двумя способами реализована кастомизация сериализатора Course для вывода количества уроков в курсе
- Добавлена модель Payments (Платежи), создана фикстуры для заполнения моделей первичными данными
  - users_data.json
  - course_data.json
- Для сериализатора модели Course путем вложенного объекта реализованно поле вывода уроков курса
- Настроены фильтрации для списка платежей:
  - меняется порядок сортировки по дате оплаты
  - фильтруется по курсу или уроку
  - фильтруется по способу оплаты (способы оплаты: 1 - Наличные, 2 - Перевод на счет)
- Для профиля пользователя сделан вывод его платежей, для платежей сделан вывод пользователя данного платежа
#### Выполнены задания 25.1
- Настроена JWT-авторизация и закрыты доступы к эндпоинтам по IsAuthenticated
- Создан модератор (команда для создания модератора ``` python manage.py cm ```), описаны права
- Описаны права доступа, пользователи могут просматривать только свои курсы и уроки