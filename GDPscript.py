%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print ("hello world")
class DataProcessingScript:
    def __init__(self, file_path):
        #self.file_path = file_path
        self.file_path = r"C:\Users\Owner\GeneralDataProcessor"
        self.data = None

    def read_file(self):
        """Reads the file based on its extension and loads the data into a pandas DataFrame."""
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
            self.data = pd.read_excel(self.file_path)
        elif self.file_path.endswith('.json'):
            self.data = pd.read_json(self.file_path)
        else:
            raise ValueError("Unsupported file format.")
        print("File successfully read.")

    def get_statistics(self):
        """Generates general statistics for the dataset."""
        if self.data is not None:
            stats = self.data.describe(include='all').transpose()
            print("Statistics:")
            print(stats)
            return stats
        else:
            raise ValueError("Data has not been loaded. Please read the file first.")

    def filter_sigma(self, column, num_sigma):
        """Filters data within a specified number of standard deviations (sigma) from the mean."""
        if column not in self.data.columns:
            raise ValueError(f"Column {column} not found in data.")

        mean = self.data[column].mean()
        std = self.data[column].std()
        filtered_data = self.data[(self.data[column] >= mean - num_sigma * std) & (self.data[column] <= mean + num_sigma * std)]
        print(f"Data filtered to within {num_sigma} sigma.")
        return filtered_data

    def plot_data(self, x_col, y_col, plot_type='scatter'):
        """Generates a plot based on the selected type."""
        if x_col not in self.data.columns or y_col not in self.data.columns:
            raise ValueError(f"Columns {x_col} and/or {y_col} not found in data.")

        if plot_type == 'scatter':
            plt.scatter(self.data[x_col], self.data[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f"Scatter Plot of {x_col} vs {y_col}")
        elif plot_type == 'line':
            plt.plot(self.data[x_col], self.data[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f"Line Plot of {x_col} vs {y_col}")
        elif plot_type == 'histogram':
            plt.hist(self.data[x_col], bins=20)
            plt.xlabel(x_col)
            plt.title(f"Histogram of {x_col}")
        elif plot_type == 'boxplot':
            sns.boxplot(x=self.data[x_col])
            plt.title(f"Boxplot of {x_col}")
        else:
            raise ValueError("Unsupported plot type. Choose from 'scatter', 'line', 'histogram', 'boxplot'.")

        plt.grid(True)
        plt.show()

# Example usage:
# script = DataProcessingScript('data.xlsx')
# script.read_file()
# stats = script.get_statistics()
# filtered = script.filter_sigma('column_name', 2)
# script.plot_data('x_column', 'y_column', plot_type='scatter')
