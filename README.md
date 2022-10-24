# best_shop api

База данных, таблицы:
1. Товар (Название, Картинка, Контент, Стоимость)
2. Заказ (Итоговая сумма, Статус, Время создания, Время подтверждения)
3) Платеж (Сумма, Статус, Тип оплаты)

АPI
1. /api/goods/list - получение списка товаров
2. /api/orders/list - GET-запрос списка заказов
3. /api/orders/list - POST-запрос создания нового Заказа (передать список id списка Товаров по ключу order_parts).
4. /api/payments/list - GET-запрос списка платежей
5. /api/payments/list - POST-запрос создания нового платежа (передать id заказа по ключу order_id)

Админка модели Заказ имеет кнопку подтверждения заказа. Её статус меняется в зависимости от значения поля статус таблицы
Платеж (кнопка доступна при статусе “Оплачен”). 
При подтверждении заказа отправляется POST-запрос по адресу https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4 
с телом JSON {"id":ИД_ЗАКАЗА, "amount":СУММА_ЗАКАЗА,”date”:ВРЕМЯ_ПОДТВЕРЖДЕНИЯ}
