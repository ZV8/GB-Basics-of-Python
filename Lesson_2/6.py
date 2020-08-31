products = []
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
while True:
    action = input('Желаете добавить новый товар? (да/нет): ')
    if action == 'да':
        print(action)
        print('Укажите характеристики товара')
        name = input('название: ')
        price = input('цена: ')
        quantity = input('количество: ')
        unit = input('единица измерения: ')
        products.append((len(products) + 1, {'название': name, 'цена': price, 'количество': quantity, 'ед': unit}))
    else:
        print(action)
        break
for n, el in products:
    analytics['название'].append(el.get('название'))
    analytics['цена'].append(el.get('цена'))
    analytics['количество'].append(el.get('количество'))
    analytics['ед'].append(el.get('ед'))
analytics['название'] = list(set(analytics['название']))
analytics['цена'] = list(set(analytics['цена']))
analytics['количество'] = list(set(analytics['количество']))
analytics['ед'] = list(set(analytics['ед']))
print(f'Список товаров: {products}')
print(f'Аналитика: {analytics}')
