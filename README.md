A business analyst practice project exploring the Kaggle "Superstore" sales dataset:
trends, segmentation, and growth analysis, done as a self-guided assignment.

## Project structure

| File | Purpose |
|---|---|
| `eda.ipynb` | Main notebook — exploratory analysis, charts, and calculations. |
| `eda.py` | Script version / scratch space for quick checks. |
| `metadata.py` | Data dictionary as a Python dict (`METADATA`) — column names, descriptions, and types. |
| `data/supermarket_sales.csv` | The dataset (not tracked in git — see below). |
| `requirements.txt` | Python dependencies. |

## Dataset

Source: [Kaggle — rohitsahoo/sales-forecasting](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
(the "Superstore" sales dataset). One row = one line item within an order.

The CSV isn't committed to this repo. To get it:

```bash
kaggle datasets download rohitsahoo/sales-forecasting --unzip
```

See `metadata.py` for a full column-by-column data dictionary.

## Setup

```bash
pip install -r requirements.txt
```

Requires Kaggle API credentials configured (`KAGGLE_USERNAME`/`KAGGLE_KEY` or
`KAGGLE_API_TOKEN` as an environment variable) if you need to re-download the data.

## What's covered so far

- Data cleaning: null checks, date type conversion, deduplication
- Monthly and yearly sales trends, with a fitted trend line
- Month-over-month and year-over-year growth rates
- Sales segmentation by region, category, and customer
