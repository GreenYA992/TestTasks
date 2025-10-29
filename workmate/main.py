import argparse
from parser import BrandAnalyzer, ReportGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Анализатор рейтингов брендов из CSV файлов"
    )
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV файлам (можно несколько)"
    )

    parser.add_argument(
        "--report",
        choices=["average-rating"],
        required=True,
        help="Тип отчета (average-rating)",
    )

    # python main.py --files products1.csv products2.csv --report average-rating

    args = parser.parse_args()

    try:
        # Анализируем все файлы
        report_data = BrandAnalyzer.analyze_files(args.files)

        ReportGenerator.generate_table(report_data)

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
