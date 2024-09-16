"""
Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def total_num_sales_product(products):
    # Посчитать и вывести суммарное количество продаж для каждого товара
    sum_numb = 0
    key_name = ''

    for prod in products:
        for key, values in prod.items():
            if isinstance(values, str):
                key_name = values
                continue
            for num in values:
                sum_numb += num
            print(f"{key_name}: {sum_numb}")


def average_num_salesproduct(products):
    # Посчитать и вывести среднее количество продаж для каждого товара
    pass


def total_num_sales_products(products):
    # Посчитать и вывести суммарное количество продаж всех товаров
    pass


def average_num_salesproducts(products):
    # Посчитать и вывести среднее количество продаж всех товаров
    pass


def main():
    products = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    total_num_sales_product(products)
    average_num_salesproduct(products)
    total_num_sales_products(products)
    average_num_salesproducts(products)


if __name__ == "__main__":
    main()