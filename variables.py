class TextMessages:
    OK_CREATE = '{"ok":true}'
    LOGIN_BUSY = "Этот логин уже используется. Попробуйте другой."
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"

    person_data = [
        ['Гиви', 'Владимирович', 'Абакан, ул. Новинского', '42', '+7 800 555 35 35', '12', '2020-06-06',
         'Эхма вот поеду ка я', "BLACK"],
        ['Владилен', 'Мойшевич', 'Гомель, главная площадь', '6', '+7 800 555 35 35', '3', '2020-06-06',
         'Красота в глазах смотрящего', "GREY"],
        ['Гвиневра', 'Стулова', 'Лиссабон, около моста', '12', '+7 800 555 35 35', '11', '2020-06-06',
         'Из пруда не вытащишь', "BLACK, GREY"],
        ['Сэмуэль', 'Эйджексон', 'Стрелитамак, Аптекарский переулок .', '3', '+7 800 555 35 35', '1', '2020-06-06',
         'Два сапога', ""]
    ]


class Urls:
    CREATE_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    RECEIVING_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'



