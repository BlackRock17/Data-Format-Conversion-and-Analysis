import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sales_data(days=30, seed=42):
    """
    Генерира примерни данни за продажби

    Args:
        days (int): Брой дни за генериране на данни
        seed (int): Seed за възпроизводими резултати

    Returns:
        pd.DataFrame: DataFrame с генерираните данни
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
    Генерира примерни данни за продажби

    Args:
        days (int): Брой дни за генериране на данни
        seed (int): Seed за възпроизводими резултати

    Returns:
        pd.DataFrame: DataFrame с генерираните данни
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