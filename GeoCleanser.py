import pandas as pd
import re
import os
from datetime import datetime

# Function to clean the latitude and longitude data
def clean_coordinates(value):
    if pd.isnull(value):  # Check for null values
        return None
    value = str(value).strip()  # Strip leading/trailing spaces
    match = re.search(r'(\d+°\s*\d+\'\s*\d+(\.\d+)?")', value)  # Extract only valid DMS format
    if match:
        value = match.group(1)  # Keep only the matched DMS value
    else:
        value = re.sub(r'[^0-9°\'".-]', '', value)  # Keep only valid DMS characters
    
    value = value.replace('N', '').replace('E', '').replace('S', '').replace('W', '')  # Remove directional indicators
    return value

# Function to convert DMS to Decimal Degrees
def dms_to_decimal(value):
    if pd.isnull(value):
        return Nonea
    match = re.match(r'(?P<deg>\d+)°\s*(?P<min>\d{1,2})\'\s*(?P<sec>\d+(\.\d+)?)\"?', str(value))  # Allow optional double quotes
    if match:
        degrees = float(match.group('deg'))
        minutes = float(match.group('min'))
        seconds = float(match.group('sec'))
        return round(degrees + (minutes / 60) + (seconds / 3600), 8)  # Convert and round to 8 decimal places
    else:
        try:
            return float(value)  # If already decimal
        except ValueError:
            return None  # Handle invalid data gracefully

# Function to filter latitude and longitude by range
def filter_by_range(value, min_value, max_value):
    try:
        decimal_value = float(value)
        return decimal_value if min_value <= decimal_value <= max_value else None
    except (ValueError, TypeError):
        return None

# Ask the user for the input file path
input_file = input("Enter the full path of the input Excel file: ").strip()

if not os.path.exists(input_file):
    raise FileNotFoundError(f"The specified file does not exist: {input_file}")

# Generate a unique output file name using timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(os.path.dirname(input_file), f'cleaned_coordinates_{timestamp}.xlsx')

# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)

# Take the number of column pairs as input
num_columns = int(input("Enter the number of column pairs you want to clean: "))
column_pairs = []

# Take input for column names for latitude and longitude pairs
for i in range(num_columns):
    latitude_column = input(f"Enter the column name for Latitude (Pair {i+1}): ")
    longitude_column = input(f"Enter the column name for Longitude (Pair {i+1}): ")
    if latitude_column not in df.columns or longitude_column not in df.columns:
        raise ValueError(f"One or both specified columns in Pair {i+1} were not found in the file.")
    column_pairs.append((latitude_column, longitude_column))

# Process each pair of columns
for latitude_column, longitude_column in column_pairs:
    df[latitude_column] = (
        df[latitude_column]
        .apply(clean_coordinates)
        .apply(dms_to_decimal)
        .apply(lambda x: filter_by_range(x, 20.34, 26.63))
    )
    df[longitude_column] = (
        df[longitude_column]
        .apply(clean_coordinates)
        .apply(dms_to_decimal)
        .apply(lambda x: filter_by_range(x, 88.01, 92.68))
    )
    # If one column is invalid, set both to None
    df.loc[df[latitude_column].isnull() | df[longitude_column].isnull(), [latitude_column, longitude_column]] = None

# Ask the user if they want to move data for blank blocks
move_data = input("Do you want to move data from one pair to another for blank blocks? (yes/no): ").strip().lower()

if move_data == "yes":
    source_lat = input("Enter the column name for the source Latitude: ")
    source_lon = input("Enter the column name for the source Longitude: ")
    target_lat = input("Enter the column name for the target Latitude: ")
    target_lon = input("Enter the column name for the target Longitude: ")

    if source_lat not in df.columns or source_lon not in df.columns or target_lat not in df.columns or target_lon not in df.columns:
        raise ValueError("One or more specified columns were not found in the file.")

    # Move data for blank blocks
    df.loc[df[target_lat].isnull(), target_lat] = df.loc[df[target_lat].isnull(), source_lat]
    df.loc[df[target_lon].isnull(), target_lon] = df.loc[df[target_lon].isnull(), source_lon]

# Save the cleaned and filtered DataFrame to a new Excel file
df.to_excel(output_file, index=False)
print(f"Cleaned, converted, and filtered data saved to {output_file}")
