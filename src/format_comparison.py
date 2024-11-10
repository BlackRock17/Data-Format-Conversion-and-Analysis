import pandas as pd
import time
import os


class FormatComparison:
    def __init__(self, base_dir='output'):
        self.base_dir = base_dir

    def read_file(self, format_type, filename):
        """Read a file of a certain format and measure the time"""
        filepath = os.path.join(self.base_dir, format_type, filename)
        start_time = time.time()

        if format_type == 'csv':
            df = pd.read_csv(filepath)
        elif format_type == 'json':
            df = pd.read_json(filepath)
        elif format_type == 'parquet':
            df = pd.read_parquet(filepath)

        end_time = time.time()
        return df, end_time - start_time

    def compare_formats(self, filename_base):
        """Compares various aspects of the formats"""
        results = {}

        for format_type in ['csv', 'json', 'parquet']:
            filename = f"{filename_base}.{format_type}"
            filepath = os.path.join(self.base_dir, format_type, filename)

            # File size
            file_size = os.path.getsize(filepath)

            # Reading speed
            _, read_time = self.read_file(format_type, filename)

            results[format_type] = {
                'file_size': file_size,
                'read_time': read_time
            }

        return results