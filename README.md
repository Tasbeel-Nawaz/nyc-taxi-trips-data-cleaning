# NYC Yellow Taxi Trips 2025 - Data Cleaning Project

## Project Overview
This project cleans and validates NYC Yellow Taxi trip data for all 12 months of 2025 using Python and Pandas.

## Dataset
- Dataset: NYC Yellow Taxi Trips
- Year: 2025
- Format: Parquet
- Coverage: January to December 2025

## Data Cleaning Steps
- Loaded monthly Parquet files.
- Checked missing values and duplicate rows.
- Converted pickup and drop-off columns to datetime.
- Calculated trip duration in minutes.
- Removed invalid trip durations.
- Filtered invalid trip distances and fare amounts.
- Validated passenger counts.
- Removed rows missing essential trip information.
- Saved cleaned monthly files in Parquet format.

## Technologies Used
- Python
- Pandas
- PyArrow
- Parquet

## How to Run
1. Install Python.
2. Install dependencies using `pip install -r requirements.txt`.
3. Place raw monthly Parquet files in `Data/Raw/`.
4. Run `python main.py`.

## Output
Cleaned monthly Parquet files are saved in `Data/Cleaned/`.

## Note
Raw and cleaned datasets are excluded from GitHub because of their size. Obtain the original dataset separately before running this project.
