import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/aidanlynde/ECON415/energy-consumption-analysis/data/owid-energy-data.csv"

def load_and_clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Selecting relevant columns for analysis
    columns_of_interest = [
        'country', 'year', 'energy_per_capita', 'fossil_fuel_consumption', 'renewables_consumption', 'primary_energy_consumption'
    ]

    # Filter the dataframe
    df_filtered = df[columns_of_interest]

    # Drop rows with missing values in the essential columns
    df_filtered = df_filtered.dropna(subset=['energy_per_capita', 'fossil_fuel_consumption', 'renewables_consumption', 'primary_energy_consumption'])
    
    return df_filtered

def visualize_data(df_filtered):
    # Aggregate data by year
    yearly_data = df_filtered.groupby('year').mean()

    # Plotting the trends
    plt.figure(figsize=(15, 7))
    plt.plot(yearly_data.index, yearly_data['energy_per_capita'], label='Energy per Capita')
    plt.plot(yearly_data.index, yearly_data['fossil_fuel_consumption'], label='Fossil Fuel Consumption')
    plt.plot(yearly_data.index, yearly_data['renewables_consumption'], label='Renewables Consumption')
    plt.plot(yearly_data.index, yearly_data['primary_energy_consumption'], label='Primary Energy Consumption')
    plt.title('Global Energy Consumption Trends (1965-2022)')
    plt.xlabel('Year')
    plt.ylabel('Energy Consumption (Wh per capita)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Additional Visualization 1: Heatmap of Energy Consumption per Capita
    heatmap_data = df_filtered[df_filtered['year'] >= 2012].pivot_table(
        index='country', 
        columns='year', 
        values='energy_per_capita'
    )
    plt.figure(figsize=(15, 10))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=False, cbar_kws={'label': 'Energy Consumption per Capita'})
    plt.title("Heatmap of Energy Consumption per Capita by Country (2012-2022)")
    plt.xlabel("Year")
    plt.ylabel("Country")
    plt.show()

    # Additional Visualization 2: Bar Chart of Renewable vs Fossil Fuel Consumption
    bar_chart_data = df_filtered[df_filtered['year'] >= 2017].groupby('country').mean()[['fossil_fuel_consumption', 'renewables_consumption']]
    bar_chart_data.sort_values(by='fossil_fuel_consumption', ascending=False).plot(kind='bar', stacked=True, figsize=(15, 10))
    plt.title("Average Renewable vs Fossil Fuel Consumption by Country (2017-2022)")
    plt.xlabel("Country")
    plt.ylabel("Average Consumption")
    plt.legend(["Fossil Fuel Consumption", "Renewables Consumption"])
    plt.show()

def analyze_data(df_filtered):
    # Basic Descriptive Statistics
    descriptive_stats = df_filtered.describe()
    return descriptive_stats

# Load, clean, and analyze the data
df_filtered = load_and_clean_data(file_path)
visualize_data(df_filtered)
descriptive_stats = analyze_data(df_filtered)

# Print the descriptive statistics
print(descriptive_stats)
