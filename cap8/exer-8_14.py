def info_car(manufacturer, model, **info):
    record = {}
    record['Manufacturer'] = manufacturer
    record['Model'] = model
    for key, value in info.items():
        record[key] = value
    return record

car = info_car('Fiat', 'Toro', Cor='Pearly White', Ano='2020')
print(car)

def make_product(amount, batch, **info_product):
    data_product = {}
    data_product['Amount']= amount
    data_product['Batch']= batch
    for key, value in info_product.items():
        data_product[key] = value
    return data_product

product = make_product('3000', '500/2024-1234', buyer='China', dealine='90 days')
print(product)