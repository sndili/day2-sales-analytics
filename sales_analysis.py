"""
Day 2 - Sales Analytics Without Pandas
Squad Python Specialization - Data Science, AI & Analytics

Tasks 1-7 use only the standard library. pandas is allowed in task 8, to check your work.
"""
import csv
from pathlib import Path

DATA_PATH = Path("data") / "electronics_sales.csv"


def read_sales(path: Path = DATA_PATH) -> list[dict[str, str]]:
    """Read the CSV with the csv module and return the raw rows."""
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        sales_reader = csv.DictReader(file)
        rows = list(sales_reader)

    
    print(f"Rows read: {len(rows)}")
    print(f"Column names: {sales_reader.fieldnames}")


    return rows   


def parse_number(value: str) -> float | None:
    """Convert a messy numeric string to a float, or return None if it cannot be trusted."""
    if not value or not value.strip():
        return None


    value = value.replace(",", "").strip()


    try:
        return float(value)
    except ValueError:
        return None


def convert_rows(rows: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    """Return (clean_rows, skipped_rows). Clean rows have numeric quantity, unit price and revenue."""
    clean_rows = []
    skipped_rows = []

    for row in rows:
        quantity = parse_number(row["quantity"])
        unit_price = parse_number(row["unit_price_kes"])

        if quantity is None:
            skipped_rows.append({
                "sale_id": row["sale_id"],
                "reason": "Invalid quantity"
            })
            continue

        if unit_price is None:
            skipped_rows.append({
                "sale_id": row["sale_id"],
                "reason": "Invalid unit price"
            })
            continue

        row["quantity"] = quantity
        row["unit_price_kes"] = unit_price
        row["revenue"] = quantity * unit_price

        clean_rows.append(row)

    
    return clean_rows, skipped_rows    


def total_revenue(rows: list[dict]) -> float:
    raise NotImplementedError


def revenue_by(rows: list[dict], field: str) -> dict[str, float]:
    """Total revenue grouped by any column (product, store, payment_method...)."""
    raise NotImplementedError


def top_n(totals: dict[str, float], n: int = 3) -> list[tuple[str, float]]:
    """Return the n highest (key, value) pairs, highest first."""
    raise NotImplementedError


def high_value(rows: list[dict], threshold: float) -> list[dict]:
    """Transactions whose revenue is at or above threshold (use a comprehension)."""
    raise NotImplementedError


# Reusable statistics - implement these yourself, no statistics module.
def mean(values: list[float]) -> float:
    raise NotImplementedError


def median(values: list[float]) -> float:
    raise NotImplementedError


def minimum_maximum(values: list[float]) -> tuple[float, float]:
    raise NotImplementedError


def verify_with_pandas(path: Path, my_results: dict) -> None:
    """Recompute the headline numbers with pandas and print whether each one matches."""
    raise NotImplementedError


if __name__ == "__main__":
    # TODO
    # Task 1 : Read CSV file and inspect the first raw redord
    sales = read_sales()
    #print(sales[0])


    #Task 2 : Convert numeric values, calculate revenues and record skipped rows
    clean_sales, skipped_sales = convert_rows(sales)
    

    print(f"Rows used: {len(clean_sales)}")
    print(f"Rows skipped: {len(skipped_sales)}")
    print(f"Skipped rows: {skipped_sales}")
    print(f"First cleaned row: {clean_sales[0]}")


