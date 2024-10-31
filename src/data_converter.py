import pandas as pd
import json
import yaml
import os


class DataConverter:
    def __init__(self, output_dir='output'):
        """
        Инициализира конвертора с базова директория за изход

        Args:
            output_dir (str): Път до изходната директория
        """
        self.output_dir = output_dir
        self._ensure_directories()

    def _ensure_directories(self):
        """Създава необходимите директории, ако не съществуват"""
        for format_dir in ['csv', 'json', 'parquet']:
            os.makedirs(os.path.join(self.output_dir, format_dir),
                        exist_ok=True)

    def save_to_csv(self, df, filename):
        """Запазва DataFrame в CSV формат"""
        path = os.path.join(self.output_dir, 'csv', filename)
        df.to_csv(path, index=False)
        return path

    def save_to_json(self, df, filename):
        """Запазва DataFrame в JSON формат"""
        path = os.path.join(self.output_dir, 'json', filename)
        with open(path, 'w') as f:
            json.dump(df.to_dict(orient='records'), f, indent=2)
        return path

    def save_to_parquet(self, df, filename):
        """Запазва DataFrame в Parquet формат"""
        path = os.path.join(self.output_dir, 'parquet', filename)
        df.to_parquet(path)
        return path

    def get_file_sizes(self, filename):
        """
        Връща размера на файловете във всички формати

        Returns:
            dict: Речник с размерите на файловете
        """
        sizes = {}
        for format_name in ['csv', 'json', 'parquet']:
            path = os.path.join(self.output_dir, format_name, filename)
            if os.path.exists(path):
                sizes[format_name] = os.path.getsize(path)
        return sizes