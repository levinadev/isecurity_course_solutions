r"""
Курс ИБ на примерах из "Мистера Робота"
Модуль 4 "Серия 1.2: d3bug", урок 4.3 "Письмо от "службы безопасности"", шаг 8

Напишите простой почтовый фильтр. Он начисляет письму по баллу за каждый признак фишинга:

1) домен отправителя (часть адреса после `@`) чужой;
2) в первой строке письма нет имени получателя;
3) хотя бы одна ссылка ведёт на чужой сайт.

Сайт или домен свой, если он совпадает с доменом сервиса или заканчивается на точку и домен сервиса:
для `mail.com` свои `mail.com` и `login.mail.com`, а `securemail.com` и `mail.com.evil.io` чужие.
Регистр букв не важен, имя получателя тоже ищите без учёта регистра.

Ввод: домен сервиса; имя получателя; адрес отправителя; первая строка письма; число ссылок `k` и `k`
строк с именами сайтов, на которые ведут ссылки.

Вывод: в первой строке число баллов, во второй `в карантин`, если баллов 2 или больше, иначе `во
входящие`.

Пример ввода:
    mail.com
    Shayla
    update@security-mail.info
    Dear User,
    1
    login.security-mail.info

Пример вывода:
    3
    в карантин
"""

service = input().strip().lower()
name = input().strip().lower()
sender = input().strip().lower()
greeting = input().strip().lower()
k = int(input())
hosts = [input().strip().lower() for _ in range(k)]


def own(host):
    return host == service or host.endswith("." + service)


score = 0
if not own(sender.split("@")[-1]):
    score += 1
if name not in greeting:
    score += 1
if any(not own(h) for h in hosts):
    score += 1
print(score)
print("в карантин" if score >= 2 else "во входящие")
