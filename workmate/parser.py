import csv
from collections import defaultdict
from typing import Dict, List

from tabulate import tabulate


class DataReader:
    """Класс для чтения данных из различных источников"""

    @staticmethod
    def read_csv(file_path: str) -> List[Dict]:
        """Читает данные из CSV файла"""
        products = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(
                    {
                        "name": row["name"],
                        "brand": row["brand"],
                        "price": float(row["price"]),
                        "rating": float(row["rating"]),
                    }
                )
        return products

    @staticmethod
    def read_json(file_path: str) -> List[Dict]:
        pass


class BrandAnalyzer:
    """Анализатор брендов со статическими методами"""

    @staticmethod
    def analyze_files(file_paths: List[str]) -> List[Dict]:
        """
        Анализирует несколько CSV файлов и возвращает объединенную статистику
        """
        all_products = []

        for file_path in file_paths:
            products = DataReader.read_csv(file_path)
            all_products.extend(products)

        return BrandAnalyzer.calculate_brand_stats(all_products)

    @staticmethod
    def calculate_brand_stats(products: List[Dict]) -> List[Dict]:
        """
        Вычисляет статистику по брендам на основе списка продуктов
        """
        brand_stats = defaultdict(lambda: {"ratings": [], "prices": [], "count": 0})

        for product in products:
            brand = product["brand"]
            brand_stats[brand]["ratings"].append(product["rating"])
            brand_stats[brand]["prices"].append(product["price"])
            brand_stats[brand]["count"] += 1

        report_data = []
        for brand, stats in brand_stats.items():
            avg_rating = sum(stats["ratings"]) / len(stats["ratings"])
            avg_price = sum(stats["prices"]) / len(stats["prices"])
            report_data.append(
                {
                    "brand": brand,
                    "average_rating": round(avg_rating, 2),
                    "average_price": round(avg_price, 2),
                    "total_products": stats["count"],
                }
            )

        # Сортировка по убыванию рейтинга
        report_data.sort(key=lambda x: x["average_rating"], reverse=True)
        return report_data


class ReportGenerator:
    """Генератор отчетов со статическими методами"""

    @staticmethod
    def generate_table(report_data: List[Dict]) -> None:
        """
        Генерирует и выводит табличный отчет
        """
        if not report_data:
            print("Нет данных для отображения")
            return

        headers = [
            "№",
            "Бренд",
            "Средний рейтинг",
        ]  # , 'Средняя цена', 'Количество товаров'
        table_data = []

        for i, item in enumerate(report_data, 1):
            table_data.append(
                [
                    i,
                    item["brand"],
                    item["average_rating"],
                    # f"${item['average_price']}",
                    # item['total_products']
                ]
            )

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
