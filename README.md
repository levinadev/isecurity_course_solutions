# isecurity_course_solutions

Решения задач курса **ИБ на примерах из "Мистера Робота"** на Stepik.

В репозитории собраны все 15 задач курса на программирование: условие, пример и решение, которое проходит проверку на Stepik. Репозиторий нужен, чтобы после решения задачи можно было сравнить свой код с вариантом автора курса.

Все задачи — учебные модели на стороне защиты. Программы работают только со строками, которые получают через `input()`, и не подключаются к чужим компьютерам и сайтам.

## Как пользоваться

1. Сначала решите задачу сами и отправьте решение на Stepik.
2. Найдите файл задачи: папка модуля → папка урока → `step_NN.py`, где `NN` — номер шага в уроке.
3. Сравните решения. Если они отличаются, это нормально: у большинства задач несколько правильных решений. Подумайте, чем ваш вариант лучше или хуже.

Если задача не получается, не открывайте решение сразу. Перечитайте теорию урока, запустите код на своих данных, посмотрите комментарии под шагом на Stepik. Подсмотренное решение почти ничему не учит.

## Как запустить решение

Нужен Python 3.10 или новее, сторонние библиотеки не нужны. Решения читают входные данные через `input()`, как на Stepik:

```bash
python 02_hellofriend/01_krista_password/step_09.py
```

После запуска введите данные с клавиатуры, по одному значению в строке. Пример входных данных есть в начале каждого файла.

## Содержание

Номер модуля в названии папки совпадает с номером модуля в курсе, номер урока — с номером урока внутри модуля.

### Серия 1.0: hellofriend

| Урок | Файл |
|---|---|
| 2.1 Пароль Кристы | [`02_hellofriend/01_krista_password/step_09.py`](02_hellofriend/01_krista_password/step_09.py) |
| 2.3 Секрет владельца кофейни | [`02_hellofriend/03_coffee_shop/step_09.py`](02_hellofriend/03_coffee_shop/step_09.py) |
| 2.4 DDoS как дымовая завеса | [`02_hellofriend/04_ddos_smokescreen/step_08.py`](02_hellofriend/04_ddos_smokescreen/step_08.py) |

### Серия 1.1: ones-and-zer0es

| Урок | Файл |
|---|---|
| 3.1 Устаревший сервер и пароли | [`03_ones_and_zeroes/01_outdated_server_and_passwords/step_09.py`](03_ones_and_zeroes/01_outdated_server_and_passwords/step_09.py) |
| 3.3 Диск от незнакомца | [`03_ones_and_zeroes/03_strangers_disk/step_06.py`](03_ones_and_zeroes/03_strangers_disk/step_06.py) |

### Серия 1.2: d3bug

| Урок | Файл |
|---|---|
| 4.1 Подменённый анализ | [`04_d3bug/01_tampered_record/step_08.py`](04_d3bug/01_tampered_record/step_08.py) |
| 4.3 Письмо от "службы безопасности" | [`04_d3bug/03_security_team_email/step_08.py`](04_d3bug/03_security_team_email/step_08.py) |

### Серия 1.3: da3m0ns

| Урок | Файл |
|---|---|
| 5.1 Тихий перегрев | [`05_da3m0ns/01_silent_overheating/step_08.py`](05_da3m0ns/01_silent_overheating/step_08.py) |
| 5.3 Машина без ключа | [`05_da3m0ns/03_keyless_car/step_08.py`](05_da3m0ns/03_keyless_car/step_08.py) |

### Серия 1.4: 3xpl0its

| Урок | Файл |
|---|---|
| 6.3 Копия пропуска | [`06_3xpl0its/03_badge_copy/step_07.py`](06_3xpl0its/03_badge_copy/step_07.py) |

### Серия 1.5: br4ve-trave1er

| Урок | Файл |
|---|---|
| 7.1 Флешка на парковке | [`07_br4ve_trave1er/01_parking_lot_usb/step_07.py`](07_br4ve_trave1er/01_parking_lot_usb/step_07.py) |

### Серия 1.7: wh1ter0se

| Урок | Файл |
|---|---|
| 9.1 Приманка | [`09_wh1ter0se/01_honeypot/step_07.py`](09_wh1ter0se/01_honeypot/step_07.py) |

### Серия 1.8: m1rr0r1ng

| Урок | Файл |
|---|---|
| 10.1 Зачем шифруют данные | [`10_m1rr0r1ng/01_why_encrypt/step_09.py`](10_m1rr0r1ng/01_why_encrypt/step_09.py) |

### Серия 1.9: zer0-day

| Урок | Файл |
|---|---|
| 11.1 Данные, которые не вернуть | [`11_zer0_day/01_lost_data/step_07.py`](11_zer0_day/01_lost_data/step_07.py) |
| 11.2 Уничтожение данных | [`11_zer0_day/02_data_destruction/step_07.py`](11_zer0_day/02_data_destruction/step_07.py) |
