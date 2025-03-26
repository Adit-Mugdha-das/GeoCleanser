# GeoCleanser

GeoCleanser is a Python-based tool designed to clean, convert, and validate geographic coordinates. Whether you're working with messy coordinate data in Degrees, Minutes, Seconds (DMS) format or decimal degrees, this tool provides a seamless way to standardize, filter, and save cleaned results by creating an Excel file for further geospatial analysis. Additionally, GeoCleanser allows for **data migration**, enabling the transfer of valid data from one column pair to another to address missing or incomplete blocks, ensuring a comprehensive and accurate dataset.

With GeoCleanser, you can easily process **multiple column pairs simultaneously** by simply specifying the column headings for latitude and longitude. This feature ensures flexibility and efficiency when working with datasets containing multiple coordinate pairs, making it ideal for large-scale geospatial preprocessing.

> **Attention**: GeoCleanser is configured to work within the geographical ranges of **Bangladesh**:
> - Latitude: `20.34` to `26.63`
> - Longitude: `88.01` to `92.68`
> If you are working with data for another country, you will need to adjust these ranges in the script.

---

##  Features
- **Coordinate Cleaning**: Strips unnecessary characters and validates latitude/longitude data in DMS format.
- **Conversion**: Converts DMS format to Decimal Degrees with high precision.
- **Validation**: Filters latitude and longitude values within user-defined geographical ranges.
- **Data Migration**: Moves data between columns for missing blocks, ensuring completeness.
- **Excel Output**: Saves cleaned and processed data into a structured Excel file.
- **Simultaneous Processing**: Handles multiple column pairs simultaneously for large datasets.

---

##  How It Works
1. **Input**: Provide an Excel file containing columns with latitude and longitude data.
2. **Processing**:
   - Cleans invalid or messy coordinate data.
   - Converts DMS coordinates to Decimal Degrees.
   - Filters coordinates by specified geographical ranges:
     - Latitude range: `20.34` to `26.63`
     - Longitude range: `88.01` to `92.68`
   - Handles invalid or missing data gracefully by setting them to `None`.
   - Optionally migrates data from one column pair to another for missing blocks.
3. **Output**:
   - The cleaned data is saved in an Excel file named `cleaned_coordinates_YYYYMMDD_HHMMSS.xlsx`, where the timestamp ensures uniqueness.
   - Saved in the same directory as the input file.

---

##  Directory Structure
```
GeoCleanser/
├── GeoCleanser.py        # Main Python script for cleaning and processing coordinates
├── LICENSE               # License file
├── README.md             # Project documentation
```

---

##  Example Usage
### Input Data
| Latitude          | Longitude         |
|--------------------|-------------------|
| 23°34'12.7"N     | 90°24'36.1"E    |
| 22°12'45.0"N     | Invalid data      |
| 25°45'15.3"N     | 88°12'30.7"E    |

### Output Data
| Latitude  | Longitude  |
|-----------|------------|
| 23.5702   | 90.4100    |
| None      | None       |
| 25.7543   | 88.2085    |

---

##  Requirements
- Python 3.6 or later
- Required libraries:
  - `pandas`
  - `openpyxl`
  - `re`

Install the dependencies using:
```bash
pip install pandas openpyxl
```

---

##  How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GeoCleanser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd GeoCleanser
   ```
3. Run the script:
   ```bash
   python GeoCleanser.py
   ```
4. Follow the prompts to:
   - Provide the input Excel file path.
   - Specify column pairs for latitude and longitude.
   - Enable or disable data migration for blank blocks.
5. Retrieve the cleaned output Excel file from the same directory as the input.

---

## Use Cases
- Preprocessing geospatial data for GIS applications.
- Cleaning messy GPS coordinates for machine learning models.
- Validating geographic data within a specific region.

---

##  License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

##  Contributing
Contributions are welcome! If you'd like to improve the project, feel free to:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

##  Acknowledgements
- Special thanks to the open-source community for tools like `pandas` and `openpyxl`.
- Project created and maintained by **Adit Mugdha Das**.

---
