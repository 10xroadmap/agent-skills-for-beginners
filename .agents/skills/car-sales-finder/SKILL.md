---
name: car-sales-finder
description: Find the number of cars being sold in a given month and year
---
# Instructions
To Find the number of cars being sold you need month and year as input
## Available scripts
- **`scripts/car-sales-lookup.py`** — Generates number of cars being sold using  month and year as parameters
Usage: scripts/car-sales-lookup.py [OPTIONS] 
accept input data and produce a summary report.
Options:
  --month month        input parameter month
  --year year       input parameter year

Examples:
  scripts/car-sales-lookup.py --year 2026 --month January

## Workflow
1. Run the script:
```bash
   python3 scripts/car-sales-lookup.py 
```
2. Print the output
