markdown
# Interactive Data Dashboard for Gender-Based Beneficiaries Analysis in Abu Dhabi for 2023

## Overview
This repository contains a Python-based script to create an interactive data dashboard for analyzing the "Beneficiaries Distribution for 2023" dataset. The dashboard includes visualizations such as bar charts and pie charts to help users better understand gender distribution, quarterly trends, and demographic insights in Abu Dhabi for 2023.

## Features
- **Interactive Bar Chart**: Visualize the distribution of beneficiaries by gender.
- **Interactive Pie Chart**: Understand gender percentage distribution among beneficiaries.
- **Cleaned Data Export**: Save processed data in a new Excel file for further analysis.

## Requirements
- Python 3.8+
- Required Python Libraries:
  - pandas
  - plotly
  - openpyxl

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/YourGithubUsername/BeneficiariesDashboard2023.git
   cd BeneficiariesDashboard2023
   

2. Install the required Python libraries:
   bash
   pip install pandas plotly openpyxl
   

3. Download the dataset files (e.g., `Distribution_of_Beneficiaries_per_Gender_Q1_2023.xlsx`) from the Abu Dhabi Open Data Platform and place them in the repository folder.

## Usage
1. Open the Python script `dashboard.py`.
2. Update the file path in the `pd.read_excel` function to the path of your dataset file.
3. Run the script:
   bash
   python dashboard.py
   
4. View the interactive charts directly in your browser.
5. The cleaned data will be saved as a new Excel file with the prefix `Cleaned_` added to the original file name.

## How to Interpret the Dashboard
- **Bar Chart**: Use this chart to compare the total number of male and female beneficiaries for the selected quarter.
- **Pie Chart**: Use this chart to analyze the percentage composition of male and female beneficiaries for the selected quarter.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open issues for bugs and feature requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact [Your Contact Information].
