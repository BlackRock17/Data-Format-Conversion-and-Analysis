from src.data_generator import generate_sales_data
from src.data_converter import DataConverter
from src.data_analyzer import DataAnalyzer
from src.format_comparison import FormatComparison


def main():
    # 1. Data generation
    print("1. Generating sample data...")
    sales_df = generate_sales_data(days=30)
    print("Data generated successfully!")

    # 2. Convert to different formats
    print("\n2. Convert the data to different formats...")
    converter = DataConverter()

    # Save in all formats
    filename = 'sales_data'
    csv_path = converter.save_to_csv(sales_df, f'{filename}.csv')
    json_path = converter.save_to_json(sales_df, f'{filename}.json')
    parquet_path = converter.save_to_parquet(sales_df, f'{filename}.parquet')

    print("Data is saved in the following formats:")
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")
    print(f"Parquet: {parquet_path}")

    # 3. File size comparison
    print("\n3. File size comparison:")
    sizes = converter.get_file_sizes(f'{filename}.csv')
    for format_name, size in sizes.items():
        print(f"{format_name.upper()}: {size:,} bytes")

    # 4. Data analysis
    print("\n4. Data analysis:")
    analyzer = DataAnalyzer()
    analysis_results = analyzer.basic_analysis(sales_df)

    print("\nSummary Statistics:")
    print(analysis_results['basic_stats'])

    print("\nSales by product:")
    print(analysis_results['product_sales'])

    print("\nTop 5 customers by sales volume:")
    print(analysis_results['top_customers'])


def compare_formats():
    print("\n5. Detailed format comparison:")
    comparator = FormatComparison()
    results = comparator.compare_formats('sales_data')

    print("\nComparative analysis:")
    print("-" * 60)
    print(f"{'Format':<10} {'Size (bytes)':<20} {'Read Time (sec)':<20}")
    print("-" * 60)

    for format_type, metrics in results.items():
        print(f"{format_type:<10} {metrics['file_size']:<20} {metrics['read_time']:.4f}")


if __name__ == "__main__":
    main()
    compare_formats()