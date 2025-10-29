# noinspection PyUnresolvedReferences
from parser import ReportGenerator

import pytest


class TestReportGenerator:
    """Тесты для класса ReportGenerator"""

    def test_generate_table_empty_data(self, capsys):
        """Тестируем генерацию таблицы для пустых данных"""
        ReportGenerator.generate_table([])
        captured = capsys.readouterr()
        assert "Нет данных для отображения" in captured.out

    def test_generate_table_with_data(self, capsys):
        """Тестируем генерацию таблицы с данными о брендах"""
        report_data = [
            {
                "brand": "apple",
                "average_rating": 4.8,
                "average_price": 899.0,
                "total_products": 2,
            },
            {
                "brand": "samsung",
                "average_rating": 4.6,
                "average_price": 799.0,
                "total_products": 1,
            },
        ]

        ReportGenerator.generate_table(report_data)
        captured = capsys.readouterr()

        # Проверяем, что вывод содержит ожидаемые данные
        assert "apple" in captured.out
        assert "samsung" in captured.out
        assert "4.8" in captured.out
        assert "4.6" in captured.out

    def test_generate_table_headers(self, capsys):
        """Тестируем наличие заголовков в сгенерированной таблице"""
        report_data = [
            {
                "brand": "test",
                "average_rating": 5.0,
                "average_price": 100.0,
                "total_products": 1,
            }
        ]

        ReportGenerator.generate_table(report_data)
        captured = capsys.readouterr()

        # Проверяем наличие заголовков
        assert "Бренд" in captured.out
        assert "Средний рейтинг" in captured.out
