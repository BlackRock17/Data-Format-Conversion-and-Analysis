# main.py
from src.data_generator import generate_sales_data
from src.data_converter import DataConverter
from src.data_analyzer import DataAnalyzer


def main():
    # 1. Генериране на данни
    print("1. Генериране на примерни данни...")
    sales_df = generate_sales_data(days=30)
    print("Данните са генерирани успешно!")

    # 2. Конвертиране в различни формати
    print("\n2. Конвертиране на данните в различни формати...")
    converter = DataConverter()

    # Запазване във всички формати
    filename = 'sales_data'
    csv_path = converter.save_to_csv(sales_df, f'{filename}.csv')
    json_path = converter.save_to_json(sales_df, f'{filename}.json')
    parquet_path = converter.save_to_parquet(sales_df, f'{filename}.parquet')

    print("Данните са запазени в следните формати:")
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")
    print(f"Parquet: {parquet_path}")

    # 3. Сравнение на размерите на файловете
    print("\n3. Сравнение на размерите на файловете:")
    sizes = converter.get_file_sizes(f'{filename}.csv')
    for format_name, size in sizes.items():
        print(f"{format_name.upper()}: {size:,} bytes")

    # 4. Анализ на данните
    print("\n4. Анализ на данните:")
    analyzer = DataAnalyzer()
    analysis_results = analyzer.basic_analysis(sales_df)

    print("\nОбобщена статистика:")
    print(analysis_results['basic_stats'])

    print("\nПродажби по продукти:")
    print(analysis_results['product_sales'])

    print("\nТоп 5 клиенти по обем на продажби:")
    print(analysis_results['top_customers'])


if __name__ == "__main__":
    main()