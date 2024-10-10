import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def read_sales_data(file_path):
    sales = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            product_name, quantity, price, date = row
            sales.append({
                'product_name': product_name,
                'quantity': int(quantity),
                'price': float(price),
                'date': date
            })
    return sales

def total_sales_per_product(sales_data):
    sales_summary = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        sales_summary[sale['product_name']] += total_sale
    return sales_summary

def sales_over_time(sales_data):
    time_summary = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        time_summary[sale['date']] += total_sale
    return time_summary

def main(file_path):
    sales_data = read_sales_data(file_path)
    
    # Анализ данных
    product_sales = total_sales_per_product(sales_data)
    date_sales = sales_over_time(sales_data)

    # Определение продукта с наибольшей выручкой
    best_product = max(product_sales, key=product_sales.get)
    print(f"Продукт с наибольшей выручкой: {best_product}, сумма: {product_sales[best_product]}")

    # Определение дня с наибольшими продажами
    best_date = max(date_sales, key=date_sales.get)
    print(f"День с наибольшими продажами: {best_date}, сумма: {date_sales[best_date]}")

    # Построение графиков
    # График общей суммы продаж по каждому продукту
    plt.figure(figsize=(10, 5))
    plt.bar(product_sales.keys(), product_sales.values(), color='blue')
    plt.title('Общая сумма продаж по продуктам')
    plt.xlabel('Продукты')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # График общей суммы продаж по дням
    plt.figure(figsize=(10, 5))
    plt.bar(date_sales.keys(), date_sales.values(), color='green')
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Даты')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main('sales_data.csv')  # Укажите имя вашего файла с данными
