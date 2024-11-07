import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sales_data(days=30, seed=42):
    """
    Generates sample sales data

    Args:
        days (int): Number of days to generate data
        seed (int): Seed for reproducible results

    Returns:
        pd.DataFrame: DataFrame with the generated data
    """
    np.random.seed(seed)

    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d')
             for x in range(days)]

    sales_data = pd.DataFrame({
        'date': dates,
        'product_id': np.random.randint(1000, 1005, days),
        'quantity': np.random.randint(1, 50, days),
        'price': np.random.uniform(10.0, 100.0, days).round(2),
        'customer_id': np.random.randint(1, 100, days)
    })

    sales_data['total_amount'] = (sales_data['quantity'] *
                                  sales_data['price']).round(2)

    return sales_data


def generate_sales_data(days=30, seed=42):
    """
    Generates sample sales data

    Args:
        days (int): Number of days to generate data
        seed (int): Seed for reproducible results

    Returns:
        pd.DataFrame: DataFrame with the generated data
    """
    np.random.seed(seed)

    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d')
             for x in range(days)]

    sales_data = pd.DataFrame({
        'date': dates,
        'product_id': np.random.randint(1000, 1005, days),
        'quantity': np.random.randint(1, 50, days),
        'price': np.random.uniform(10.0, 100.0, days).round(2),
        'customer_id': np.random.randint(1, 100, days)
    })

    sales_data['total_amount'] = (sales_data['quantity'] *
                                  sales_data['price']).round(2)

    return sales_data