Анализатор рейтингов брендов
Простой и эффективный скрипт для анализа CSV файлов с рейтингами товаров и генерации отчетов по брендам.

Установите зависимости:
   ```bash
   pip install -r requirements.txt
     
   ```
Использование

Запуск:
   ```bash
   python main.py --files products1.csv products2.csv --report average-rating
   ```
Получение справки:
   ```bash
   python main.py --help
     
   ```

Формат входных данных

CSV файл должен содержать следующие колонки:
   ```CSV
   name,brand,price,rating
   iphone 15 pro,apple,999,4.9
   galaxy s23 ultra,samsung,1199,4.8
   redmi note 12,xiaomi,199,4.6
   iphone 14,apple,799,4.7
   galaxy a54,samsung,349,4.2
   
   ```
Пример вывода
   ```text
   +----+---------+-------------------+
   | №  | Бренд   |   Средний рейтинг |
   +====+=========+===================+
   | 1  | apple   |               4.8 |
   +----+---------+-------------------+
   | 2  | xiaomi  |               4.6 |
   +----+---------+-------------------+
   | 3  | samsung |               4.5 |
   +----+---------+-------------------+
   
   ```

Архитектура проекта
   ```text
   brand-rating-analyzer/
   ├── main.py              # Основной скрипт
   ├── task_script.py       # Бизнес-логика обработки данных
   └── README.md            # Документация
   
   ```
Запуск тестов
   ```bash
   pytest
   
   ```
Покрытие кода
   ```bash
   pytest --cov=parser --cov-report=term-missing
   
   ```
