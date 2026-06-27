'''
PEP 723 defines a standard format for inline script metadata. 
Declare dependencies in a TOML block inside
'''
# /// script
# dependencies = [
# pandas
# ]
# ///

import sys
import json
import pandas as pd
import argparse
def get_car_sales(year: str, month: str):
    df = pd.read_csv("car-sales.csv")
    df["year"] = df["year"].astype(str)
    result = df.query(f"year == '{year}' and month == '{month}'")
    return result["sales"].iloc[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate car sales for a given year and month.')
    parser.add_argument('--year', type=str, help='input parameter year')
    parser.add_argument('--month', type=str, help='input parameter month')
    args, unknown = parser.parse_known_args()
    # Fallback to positional if flags are not used, to be safe
    year = args.year
    month = args.month
    if not year or not month:
        if len(sys.argv) >= 3:
            year = sys.argv[1]
            month = sys.argv[2]
        else:
            print(json.dumps({"error": "Missing arguments. year: --year <year> --month <month>"}))
            sys.exit(1)         
    print(get_car_sales(year, month))


