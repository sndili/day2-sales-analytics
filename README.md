# Tech Hub Kenya : Sales Analytics Without Pandas

## Project Overview

This project analyses September 2026 sales data for Tech Hub Kenya using Python's standard library. It calculates total revenue, groups revenue by product, store, and payment method, identifies high-value transactions, and calculates transaction revenue statistics.

> Pandas is used only in Task 8 to independently verify the results produced by the standard-library implementation.

## Project Structure

```text
day2-sales-analytics/
├── sales_analysis.py
├── data/
│   └── electronics_sales.csv
├── output/
│   └── sales_report.txt
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10 or later
- pandas for Task 8 verification
- The sales CSV file in `data/electronic_sales.csv`

The analysis in Tasks 1 to 7 uses Python's standard library, including `csv`, `pathlib`, `contextlib` and `io`.

## Setup and Installation

1. Clone the repository and navigate into the project directory.

   ```bash
   git clone <your-repository-url>
   cd day2-sales-analytics
   ```

2. Create a virtual environment.

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment.

   **Windows PowerShell:**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   **Git Bash:**

   ```bash
   source .venv/Scripts/activate
   ```

4. Install the project dependencies.

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Analysis

Run the script from the project root directory:

```bash
python sales_analysis.py
```

The script reads `data/electronics_sales.csv`, performs the analysis, prints the results and generates `output/sales_report.txt`. The output directory is created automatically if it does not exist. The report is overwritten each time the script runs.

## Analysis Tasks

### Task 1: Read the CSV

The `read_sales()` function uses `csv.DictReader` to read the file into a list of dictionaries. It reports the number of rows read and the available column names.

### Task 2: Clean and Convert Numeric Values

The `parse_number()` function converts numeric strings into floating-point numbers. The `convert_rows()` function processes the sales records, calculates transaction revenue and separates valid records from skipped records.

**Cleaning rules and assumptions:**

- Leading and trailing whitespace is removed before conversion.
- Commas used as thousands separators are removed. For example, `"1,500"` becomes `1500.0`.
- Empty strings and strings that cannot be converted to numbers are treated as invalid.
- A row with an invalid quantity or unit price is skipped and recorded with its sale ID and reason.
- If both fields are invalid, the quantity is checked first, so the recorded reason is `Invalid quantity`.
- Valid quantities and unit prices are converted to numbers and revenue is calculated as quantity multiplied by unit price.
- The original sales CSV is not rewritten by the cleaning process.

These rules allow the analysis to continue without including transactions with invalid numeric values.

### Task 3: Calculate Total Revenue

The `total_revenue()` function calculates the total revenue from valid transactions using quantity multiplied by unit price. Results are displayed in Kenyan shillings (KES), with thousands separators and two decimal places.

### Task 4: Group Revenue

The `revenue_by()` function uses a regular dictionary to calculate total revenue grouped by a selected field. It supports product, store, and payment method.

The report displays product revenue in descending order, with alphabetical ordering used when revenues are equal. Store and payment method breakdowns are also included.

### Task 5: Identify the Top Three Products

The `top_n()` function sorts categories by revenue in descending order and returns the requested number of results.

**Tie-breaking rule:** When two categories have equal revenue, their names are sorted alphabetically.

### Task 6: Identify High-Value Transactions

The `high_value()` function uses a list comprehension to select transactions with revenue greater than or equal to KES 50,000.

A dictionary comprehension counts qualifying transactions for each store, including stores with zero qualifying transactions.

### Task 7: Calculate Transaction Statistics

The project implements `mean()`, `median()` and `minimum_maximum()` without using the `statistics` module. The minimum and maximum values are found through iteration rather than the built-in `min()` and `max()` functions. All three functions raise a `ValueError` when given an empty list.

The statistics are calculated using individual valid transaction revenues, not grouped product or store totals.

### Task 8: Verify Results with Pandas

The `verify_with_pandas()` function independently reads and cleans the CSV using pandas and recalculates the headline results.

It compares pandas results with the results produced by the standard-library functions for:

- Total revenue
- Revenue by product
- Top three products
- Mean transaction revenue
- Median transaction revenue

Each comparison reports `MATCH` or `MISMATCH`. This provides a way to check the accuracy of the main implementation without using pandas for Tasks 1 to 7.

## Results Summary

Using the supplied dataset, the analysis produces the following results:

| Metric | Result |
|---|---:|
| Rows read | 50 |
| Valid rows used | 45 |
| Rows skipped | 5 |
| Total revenue | KES 1,291,813.00 |
| High-value transactions | 5 |
| Mean transaction revenue | KES 28,706.96 |
| Median transaction revenue | KES 10,998.00 |
| Minimum transaction revenue | KES 1,499.00 |
| Maximum transaction revenue | KES 259,996.00 |

The three highest-revenue products are HP 15 Laptop, Hisense 43in Smart TV and Lenovo Tab M10.

The complete breakdowns, high-value transactions, skipped-row reasons and pandas verification results are available in `output/sales_report.txt`.

## Output

The generated sales report includes:

- Row counts and skipped-record reasons
- Total revenue
- Revenue by product, store, and payment method
- Top three products by revenue
- High-value transactions and counts by store
- Transaction revenue statistics
- Pandas verification results

## Side Notes

- Run the script from the project root so the relative file paths resolve correctly.
- Keep the supplied CSV in `data/electronics_sales.csv`.
- Install pandas before running the script because Task 8 imports it.
- The generated report is reproducible from the input CSV and the analysis code.
