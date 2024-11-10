import os
import pandas as pd
import json
import numpy as np
from datetime import datetime, timedelta


class FormatExercises:
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        self._create_directories()

    def _create_directories(self):
        """Creates the necessary directories for the output files"""
        for format_type in ['csv', 'json', 'parquet']:
            directory = os.path.join(self.output_dir, format_type)
            os.makedirs(directory, exist_ok=True)
            print(f"Directory created: {directory}")

    def exercise_1_nested_data(self):
        """
        Exercise 1: Working with nested data
        Demonstrates why JSON is better suited for nested structures
        """
        # Create nested order data
        orders = {
            'order_id': [1, 2],
            'customer': [
                {
                    'id': 1,
                    'name': 'Иван Петров',
                    'address': {
                        'city': 'София',
                        'street': 'Витоша 15'
                    }
                },
                {
                    'id': 2,
                    'name': 'Мария Иванова',
                    'address': {
                        'city': 'Пловдив',
                        'street': 'Марица 10'
                    }
                }
            ],
            'items': [
                [
                    {'product': 'Лаптоп', 'quantity': 1, 'price': 1200},
                    {'product': 'Мишка', 'quantity': 2, 'price': 25}
                ],
                [
                    {'product': 'Монитор', 'quantity': 2, 'price': 300}
                ]
            ]
        }

        # Save to formats
        # JSON - native to nested data
        with open(f'{self.output_dir}/json/nested_orders.json', 'w', encoding='utf-8') as f:
            json.dump(orders, f, indent=2, ensure_ascii=False)

        # CSV - we need to "smooth" the data
        flattened_orders = []
        for i in range(len(orders['order_id'])):
            customer = orders['customer'][i]
            for item in orders['items'][i]:
                flattened_orders.append({
                    'order_id': orders['order_id'][i],
                    'customer_id': customer['id'],
                    'customer_name': customer['name'],
                    'customer_city': customer['address']['city'],
                    'customer_street': customer['address']['street'],
                    'product': item['product'],
                    'quantity': item['quantity'],
                    'price': item['price']
                })

        df = pd.DataFrame(flattened_orders)
        df.to_csv(f'{self.output_dir}/csv/flattened_orders.csv', index=False)

        return "Exercise 1 complete - check the nested_orders.json and flattened_orders.csv files"

    def exercise_2_time_series(self):
        """
        Exercise 2: Working with time series
        Demonstrates the benefits of Parquet for large volumes of data
        """
        # Generating sensor data for one year (hourly)
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='H')
        sensor_data = pd.DataFrame({
            'timestamp': dates,
            'temperature': np.random.normal(20, 5, len(dates)),
            'humidity': np.random.normal(60, 10, len(dates)),
            'pressure': np.random.normal(1013, 10, len(dates))
        })

        # Save in all formats
        sensor_data.to_csv(f'{self.output_dir}/csv/sensor_data.csv', index=False)
        sensor_data.to_json(f'{self.output_dir}/json/sensor_data.json', orient='records')
        sensor_data.to_parquet(f'{self.output_dir}/parquet/sensor_data.parquet')

        # Demonstration of reading part of the data
        print("\nRead only temperature data from various formats:")

        # CSV - we need to read the whole file
        start_time = datetime.now()
        csv_data = pd.read_csv(f'{self.output_dir}/csv/sensor_data.csv')['temperature']
        csv_time = (datetime.now() - start_time).total_seconds()

        # Parquet - we can read only the column we need
        start_time = datetime.now()
        parquet_data = pd.read_parquet(f'{self.output_dir}/parquet/sensor_data.parquet', columns=['temperature'])
        parquet_time = (datetime.now() - start_time).total_seconds()

        return {
            'csv_read_time': csv_time,
            'parquet_read_time': parquet_time,
            'csv_size': os.path.getsize(f'{self.output_dir}/csv/sensor_data.csv'),
            'parquet_size': os.path.getsize(f'{self.output_dir}/parquet/sensor_data.parquet')
        }

    def exercise_3_data_types(self):
        """
        Exercise 3: Working with different data types
        Demonstrates how different formats handle data types
        """
        #Create a DataFrame with different data types
        df = pd.DataFrame({
            'integer': [1, 2, 3],
            'float': [1.1, 2.2, 3.3],
            'string': ['a', 'b', 'c'],
            'date': pd.date_range('2023-01-01', periods=3),
            'boolean': [True, False, True],
            'category': pd.Categorical(['small', 'medium', 'large'])
        })

        # Save in all formats
        df.to_csv(f'{self.output_dir}/csv/datatypes.csv', index=False)
        df.to_json(f'{self.output_dir}/json/datatypes.json', orient='records')
        df.to_parquet(f'{self.output_dir}/parquet/datatypes.parquet')

        # Reading and checking data types
        csv_df = pd.read_csv(f'{self.output_dir}/csv/datatypes.csv')
        json_df = pd.read_json(f'{self.output_dir}/json/datatypes.json')
        parquet_df = pd.read_parquet(f'{self.output_dir}/parquet/datatypes.parquet')

        return {
            'csv_dtypes': csv_df.dtypes.to_dict(),
            'json_dtypes': json_df.dtypes.to_dict(),
            'parquet_dtypes': parquet_df.dtypes.to_dict()
        }


def main():
    exercises = FormatExercises()

    # Exercise 1: Nested data
    print("\nExercise 1: Working with nested data")
    print(exercises.exercise_1_nested_data())

    # Exercise 2: Time series
    print("\nExercise 2: Working with time series")
    results = exercises.exercise_2_time_series()
    print(f"CSV time to readе: {results['csv_read_time']:.4f} seconds")
    print(f"Parquet time to read: {results['parquet_read_time']:.4f} seconds")
    print(f"CSV size: {results['csv_size']:,} bytes")
    print(f"Parquet size: {results['parquet_size']:,} bytes")

    # Exercise 3: Data types
    print("\nExercise 3: Working with different data types")
    dtypes = exercises.exercise_3_data_types()
    print("\nData types in CSV:")
    print(dtypes['csv_dtypes'])
    print("\nData types in JSON:")
    print(dtypes['json_dtypes'])
    print("\nData types in Parquet:")
    print(dtypes['parquet_dtypes'])


if __name__ == "__main__":
    main()