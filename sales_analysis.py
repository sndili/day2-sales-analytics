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
    #Calculate the total revenue from all valid sales
    total = 0

    for row in rows:
        total += row["quantity"] * row["unit_price_kes"]

    return total    


def revenue_by(rows: list[dict], field: str) -> dict[str, float]:
    """Total revenue grouped by any column (product, store, payment_method...)."""
    totals = {}

    for row in rows:
        category = row[field]
        revenue = row["revenue"]

        if category not in totals:
            totals[category] = 0

        totals[category] += revenue

    return totals        


def top_n(totals: dict[str, float], n: int = 3) -> list[tuple[str, float]]:
    """Return the n highest (key, value) pairs, highest first."""
    ranked_totals = sorted(
        totals.items(),
        key=lambda item: (-item[1], item[0])
    )

    return ranked_totals[:n]


def high_value(rows: list[dict], threshold: float) -> list[dict]:
    """Transactions whose revenue is at or above threshold (use a comprehension)."""
    return [row for row in rows if row["revenue"] >= threshold]


# Reusable statistics - implement these yourself, no statistics module.
def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot calculate mean of an empty list")

    return sum(values) / len(values)


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot calculate median of an empty list")

    sorted_values = sorted(values)
    middle = len(sorted_values) // 2

    if len(sorted_values) % 2 == 1:
        return sorted_values[middle]

    return(sorted_values[middle - 1] + sorted_values[middle]) / 2


def minimum_maximum(values: list[float]) -> tuple[float, float]:
    if not values:
        raise ValueError("Cannot find minimum and maximum empty list")

    minimum = values[0]
    maximum = values[0]

    for value in values:
        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value


    return minimum, maximum            


def verify_with_pandas(path: Path, my_results: dict) -> None:
    """Recompute the headline numbers with pandas and print whether each one matches."""
    raise NotImplementedError


if __name__ == "__main__":
    # TODO

    # Task 1 : Read CSV file and inspect the first raw redord
    sales = read_sales()
    #print(sales[0])


    # Task 2 : Convert numeric values, calculate revenues and record skipped rows
    clean_sales, skipped_sales = convert_rows(sales)


    print(f"Rows used: {len(clean_sales)}")
    print(f"Rows skipped: {len(skipped_sales)}")
    print(f"Skipped rows: {skipped_sales}")
    print(f"First cleaned row: {clean_sales[0]}")


    # Task 3 : Calculate and show total revenue
    revenue = total_revenue(clean_sales)
    print(f"Total revenue: KES {revenue:,.2f}")


    # Task 4 : Calculate revenue by product, store and payment method
    product_revenue = revenue_by(clean_sales, "product")
    store_revenue = revenue_by(clean_sales, "store")
    payment_revenue = revenue_by(clean_sales, "payment_method")

    print(f"Revenue by product: {product_revenue}")
    print(f"Revenue by store: {store_revenue}")
    print(f"Revenue by payment method: {payment_revenue}")


    # Task 5 : Display the three products with the highest revenue
    top_products = top_n(product_revenue, 3)
    print(f"Top 3 products: {top_products}")


    # Task 6 : Find hgh values sales and count them by store
    high_value_sales = high_value(clean_sales, 50000)

    high_value_counts = {
        store: sum(1 for row in high_value_sales if row["store"] == store)
        for store in store_revenue
    }

    print(f"High-value transactions: {high_value_sales}")
    print(f"High-value transaction count: {len(high_value_sales)}")
    print(f"High-value sales by store: {high_value_counts}")


    # Task 7 : Calculate statistics for individual sale revenue
    sales_revenue = [row["revenue"] for row in clean_sales]

    average_revenue = mean(sales_revenue)
    median_revenue = median(sales_revenue)
    minimum_revenue, maximum_revenue = minimum_maximum(sales_revenue)


    print(f"Mean revenue: KES {average_revenue:,.2f}")
    print(f"Median revenue: KES {median_revenue:,.2f}")
    print(f"Minimum revenue: KES {minimum_revenue:,.2f}")
    print(f"Maximum revenue: KES {maximum_revenue:,.2f}")




