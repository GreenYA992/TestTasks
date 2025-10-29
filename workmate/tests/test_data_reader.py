import os
import tempfile
import textwrap
# noinspection PyUnresolvedReferences
from parser import DataReader

import pytest


class TestDataReader:
    """Тесты для класса DataReader"""

    def test_read_csv_valid_file(self):
        """Тестируем чтение корректного CSV файла с товарами"""
        # Создаем временный CSV файл
        csv_content = textwrap.dedent("""\
                name,brand,price,rating
                iphone 15,apple,999,4.9
                galaxy s23,samsung,899,4.8
            """)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            temp_file = f.name

        try:
            result = DataReader.read_csv(temp_file)

            assert len(result) == 2
            assert result[0]["name"] == "iphone 15"
            assert result[0]["brand"] == "apple"
            assert result[0]["price"] == 999.0
            assert result[0]["rating"] == 4.9
            assert result[1]["brand"] == "samsung"
        finally:
            os.unlink(temp_file)

    def test_read_csv_nonexistent_file(self):
        """Тестируем обработку ошибки при чтении несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            DataReader.read_csv("nonexistent_file.csv")

    def test_read_csv_empty_file(self):
        """Тестируем чтение пустого CSV файла (только заголовки)"""
        csv_content = "name,brand,price,rating\n"

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            temp_file = f.name

        try:
            result = DataReader.read_csv(temp_file)
            assert result == []
        finally:
            os.unlink(temp_file)
