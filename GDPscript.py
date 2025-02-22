#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print ("hello world")
class DataProcessingScript:
    def __init__(self, file_path):
        self.file_path = file_path
        print ("hello world2")
        #self.file_path = r"C:\Users\Owner\GeneralDataProcessor"
        self.data = None 

    def read_file(self):
        """Reads the file based on its extension and loads the data into a pandas DataFrame."""
        print ("hello world3")
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
            plt.hist(self.data[y_col], bins=20)
            plt.xlabel(y_col)
            plt.title(f"Histogram of {y_col}")
        elif plot_type == 'boxplot':
            sns.boxplot(x=self.data[y_col])
            plt.title(f"Boxplot of {y_col}")
        else:
            raise ValueError("Unsupported plot type. Choose from 'scatter', 'line', 'histogram', 'boxplot'.")

        plt.grid(True)
        #ax.xaxis.set_major_locator(mdates.AutoDateLocator())  # Auto tick spacing
        #plt.xticks(rotation=45)  # Rotate labels for readability

        plt.show()

# Example usage:
file_path = r"C:\Users\Owner\Documents\Ryan\2025 GitHub\data.csv"
print(file_path)

script = DataProcessingScript(file_path)
script.read_file()

stats = script.get_statistics()

# Convert x_col to datetime if not already
script.data[script.data.columns[0]] = pd.to_datetime(script.data[script.data.columns[0]])
x_col = script.data.columns[0]  # The first column as x-axis
x_values = script.data[x_col]  # Get x-axis values

for y_col in script.data.columns[1:]:
     y_values = script.data[y_col]  # Get y-axis values
     
     filtered = script.filter_sigma(x_col, 2)
     script.plot_data(x_col, y_col, plot_type='scatter')

for y_col in script.data.columns[1:]:
     y_values = script.data[y_col]  # Get y-axis values
     
     filtered = script.filter_sigma(x_col, 2)
     script.plot_data(x_col, y_col, plot_type='histogram')