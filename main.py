import  pandas as pd

months = [f"{i:02d}" for i in range(1, 13)]

for month in months:
    input_path = f"Data/Raw/yellow_tripdata_2025-{month}.parquet"
    output_file = f"Data/Cleaned/yellow_tripdata_2025-{month}_cleaned.parquet"
     
    try:
        df = pd.read_parquet(input_path)
    except FileNotFoundError:
        print(f"File nahi mili: {input_path}, agle mahine par chal rahe hain...")
        continue

    print ("Head", df.head())
    print ("Shape", df.shape)
    print ("null value", df.isnull().sum()) 
    print ("Duplicate value", df.duplicated().sum())
    print("Data type", df.dtypes)

    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    df['trip_duration_mins'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
    intial_row = len( df)
    df = df[(df['trip_duration_mins'] > 0) & (df['trip_duration_mins'] <= 1440)]
    final_row = len(df)
    print (f"Initial row: {intial_row}, Final row: {final_row}, Removed rows: {intial_row - final_row}  ")

    befor_filter = len(df)
    df = df[(df['trip_distance'] > 0) & (df['trip_distance'] <= 100)]
    df = df[(df['fare_amount'] > 0) & (df['total_amount'] >= 0)]
    after_filter = len(df)
    print(f"Ab total rows bachi hain: {befor_filter}") 
    print(f"Distance/Fare validation ke baad remove ki gayi rows: {befor_filter - after_filter}")
    print(f"Ab total rows bachi hain: {after_filter}")

    before_pax = len(df)
    df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 6)] 
    print(f"Invalid passenger count ki wajah se remove rows: {before_pax - len(df)}")
    df = df.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'PULocationID', 'DOLocationID'])
    print(f"Final Cleaned Rows (January 2025): {len(df)}")

    df.to_parquet(output_file, index=False)
print("file save successfully")