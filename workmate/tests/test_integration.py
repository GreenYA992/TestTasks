import os
import subprocess
import sys
# noinspection PyUnresolvedReferences
from parser import BrandAnalyzer

import pytest


def test_integration_with_real_files():
    """Интеграционный тест с реальными CSV файлами проекта"""
    # Проверяем существование тестовых файлов
    if not (os.path.exists("products1.csv") and os.path.exists("products2.csv")):
        pytest.skip("Тестовые файлы не найдены, пропускаем интеграционный тест")

    result = BrandAnalyzer.analyze_files(["products1.csv", "products2.csv"])

    # Проверяем, что все бренды присутствуют
    brands = [item["brand"] for item in result]
    assert "apple" in brands
    assert "samsung" in brands
    assert "xiaomi" in brands

    # Проверяем сортировку по рейтингу (убывание)
    ratings = [item["average_rating"] for item in result]
    assert ratings == sorted(ratings, reverse=True)


def test_main_with_correct_arguments():
    """Тестируем запуск main.py с корректными аргументами"""
    if not (os.path.exists("products1.csv") and os.path.exists("products2.csv")):
        pytest.skip("Тестовые файлы не найдены")

    result = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files",
            "products1.csv",
            "products2.csv",
            "--report",
            "average-rating",
        ],
        capture_output=True,
        text=True,
        cwd=".." if os.path.basename(os.getcwd()) == "tests" else ".",
    )

    # Проверяем что программа завершилась успешно
    assert result.returncode == 0
    # Проверяем что в выводе есть ожидаемые бренды
    assert (
        "apple" in result.stdout
        or "samsung" in result.stdout
        or "xiaomi" in result.stdout
    )


def test_main_missing_report_argument():
    """Тестируем запуск main.py без аргумента --report"""
    result = subprocess.run(
        [sys.executable, "main.py", "--files", "products1.csv"],
        capture_output=True,
        text=True,
        cwd=".." if os.path.basename(os.getcwd()) == "tests" else ".",
    )

    # Проверяем что программа завершилась с ошибкой
    assert result.returncode != 0
    assert "--report" in result.stderr


def test_main_invalid_report_argument():
    """Тестируем запуска main.py с неверным аргументом --report"""
    if not os.path.exists("products1.csv"):
        pytest.skip("Тестовые файлы не найдены")

    result = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files",
            "products1.csv",
            "--report",
            "invalid-report",
        ],
        capture_output=True,
        text=True,
        cwd=".." if os.path.basename(os.getcwd()) == "tests" else ".",
    )

    # Проверяем что программа завершилась с ошибкой или показала сообщение
    assert "не поддерживается" in result.stdout or result.returncode != 0
