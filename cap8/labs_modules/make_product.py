def make_product(amount, batch, **info_product):
    data_product = {}
    data_product['Amount']= amount
    data_product['Batch']= batch
    for key, value in info_product.items():
        data_product[key] = value
    return data_product
