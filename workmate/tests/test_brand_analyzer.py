import os
import tempfile
import textwrap
# noinspection PyUnresolvedReferences
from parser import BrandAnalyzer

import pytest


class TestBrandAnalyzer:
    """Тесты для класса BrandAnalyzer"""

    def test_calculate_brand_stats_empty_list(self):
        """Тестируем расчет статистики для пустого списка товаров"""
        result = BrandAnalyzer.calculate_brand_stats([])
        assert result == []

    def test_calculate_brand_stats_single_brand(self):
        """Тестируем расчет статистики для одного бренда с несколькими товарами"""
        products = [
            {"name": "p1", "brand": "apple", "price": 100.0, "rating": 4.0},
            {"name": "p2", "brand": "apple", "price": 200.0, "rating": 5.0},
        ]

        result = BrandAnalyzer.calculate_brand_stats(products)

        assert len(result) == 1
        assert result[0]["brand"] == "apple"
        assert result[0]["average_rating"] == 4.5
        assert result[0]["average_price"] == 150.0
        assert result[0]["total_products"] == 2

    def test_calculate_brand_stats_multiple_brands(self):
        """Тестируем расчет статистики для нескольких брендов и проверяет сортировку по рейтингу"""
        products = [
            {"name": "p1", "brand": "apple", "price": 100.0, "rating": 4.0},
            {"name": "p2", "brand": "samsung", "price": 200.0, "rating": 5.0},
            {"name": "p3", "brand": "apple", "price": 300.0, "rating": 3.0},
        ]

        result = BrandAnalyzer.calculate_brand_stats(products)

        assert len(result) == 2
        # Проверяем сортировку по рейтингу (убывание)
        assert result[0]["brand"] == "samsung"  # рейтинг 5.0
        assert result[1]["brand"] == "apple"  # рейтинг 3.5

    def test_analyze_files_integration(self):
        """Интеграционный тест: анализ нескольких CSV файлов и объединение данных"""
        # Создаем два временных CSV файла
        csv1_content = textwrap.dedent("""\
        name,brand,price,rating
        iphone 15,apple,999,4.9
        galaxy s23,samsung,899,4.8""")

        csv2_content = textwrap.dedent("""\
        name,brand,price,rating
        iphone 14,apple,799,4.7
        poco x5,xiaomi,299,4.5""")


        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f1:
            f1.write(csv1_content)
            temp_file1 = f1.name

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f2:
            f2.write(csv2_content)
            temp_file2 = f2.name

        try:
            result = BrandAnalyzer.analyze_files([temp_file1, temp_file2])

            assert len(result) == 3  # apple, samsung, xiaomi

            # Проверяем apple (объединенные данные из двух файлов)
            apple_data = next(item for item in result if item["brand"] == "apple")
            assert apple_data["total_products"] == 2
            assert apple_data["average_rating"] == 4.8  # (4.9 + 4.7) / 2

        finally:
            os.unlink(temp_file1)
            os.unlink(temp_file2)

    def test_analyze_files_nonexistent(self):
        """Тестируем обработку ошибки при анализе несуществующих файлов"""
        with pytest.raises(FileNotFoundError):
            BrandAnalyzer.analyze_files(["nonexistent.csv"])
