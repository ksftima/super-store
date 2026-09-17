"""
Data dictionary for data/supermarket_sales.csv
Source: Kaggle, rohitsahoo/sales-forecasting ("Superstore" sales dataset).
One row = one line item within an order.
"""

METADATA = {
    "Row ID": {
        "description": "Unique identifier for each row (line item) in the dataset.",
        "type": "Identifier",
        "dtype": "int64",
    },
    "Order ID": {
        "description": "Identifier for the order. One order can span multiple rows.",
        "type": "Identifier",
        "dtype": "object (string)",
    },
    "Order Date": {
        "description": "Date the order was placed. Stored as day/month/year "
                        "(e.g. 15/04/2018).",
        "type": "Date",
        "dtype": "object (string) -> convert to datetime64",
    },
    "Ship Date": {
        "description": "Date the order was shipped. Ship Date - Order Date = "
                        "shipping delay.",
        "type": "Date",
        "dtype": "object (string) -> convert to datetime64",
    },
    "Ship Mode": {
        "description": "Shipping method chosen (e.g. Standard Class, Second Class, "
                        "First Class, Same Day).",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Customer ID": {
        "description": "Unique identifier for the customer.",
        "type": "Identifier",
        "dtype": "object (string)",
    },
    "Customer Name": {
        "description": "Customer's name.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Segment": {
        "description": "Customer segment: Consumer, Corporate, or Home Office.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Country": {
        "description": "Country of the order (dataset is US-only).",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "City": {
        "description": "City the order shipped to.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "State": {
        "description": "State the order shipped to.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Postal Code": {
        "description": "ZIP/postal code of the shipping address.",
        "type": "Identifier (numeric-looking, not a quantity)",
        "dtype": "float64",
    },
    "Region": {
        "description": "Sales region: East, West, Central, or South.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Product ID": {
        "description": "Unique identifier for the product.",
        "type": "Identifier",
        "dtype": "object (string)",
    },
    "Category": {
        "description": "Top-level product category: Furniture, Office Supplies, "
                        "or Technology.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Sub-Category": {
        "description": "More specific product grouping within a Category "
                        "(e.g. Chairs, Binders, Phones).",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Product Name": {
        "description": "Full name/description of the product.",
        "type": "Categorical",
        "dtype": "object (string)",
    },
    "Sales": {
        "description": "Revenue for that line item, in USD.",
        "type": "Numerical (continuous)",
        "dtype": "float64",
    },
}

if __name__ == "__main__":
    for column, info in METADATA.items():
        print(f"{column}: {info}")
