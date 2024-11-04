import pandas as pd


class DataAnalyzer:
    @staticmethod
    def basic_analysis(df):
        """
        Performs basic data analysis

        Args:
            df (pd.DataFrame): DataFrame for analysis

        Returns:
            dict: Dictionary of analysis results
        """
        analysis = {
            'basic_stats': df.describe(),
            'product_sales': df.groupby('product_id').agg({
                'quantity': 'sum',
                'total_amount': 'sum'
            }).round(2),
            'daily_sales': df.groupby('date')['total_amount'].sum().round(2),
            'top_customers': df.groupby('customer_id')['total_amount'].sum().sort_values(ascending=False).head()
        }

        return analysis
