# Assignment: Superstore Sales Analysis

**Role:** You are the Business Analyst for a retail chain ("Superstore"). Leadership
wants to understand what's driving sales performance and where to focus next quarter.

**Dataset:** `train.csv` (Kaggle: rohitsahoo/sales-forecasting)

Work through the stages below roughly in order. Each stage has a business question,
a task, and a deliverable. Don't skip to the code — write the question down first,
in your own words, before you touch pandas.

---

## Stage 0 — Get oriented
- [ ] Load the data. What are the columns? What does one row represent?
- [ ] Check for nulls, duplicate rows, and the date range covered.
- [ ] Convert `Order Date` / `Ship Date` to actual datetime types.

**Deliverable:** 5-bullet "data dictionary" — what each key column means, in plain English.

---

## Stage 1 — Overall performance
**Business question:** *How is the business doing overall, and is it growing?*
- [ ] Total sales, total number of orders, total unique customers.
- [ ] Monthly sales trend over the full period. Is there seasonality?
- [ ] Year-over-year growth rate.

**Deliverable:** One line chart (monthly sales) + 3 headline numbers, written like you'd
put them in a slide title (e.g. "Sales grew 18% YoY, driven by Q4").

---

## Stage 2 — Segmentation
**Business question:** *Where does the sales come from, and where should we focus?*
- [ ] Sales by Region, by Category, by Sub-Category, by Customer Segment.
- [ ] Rank sub-categories by total sales. Which 3 are the biggest? Smallest?
- [ ] Top 10 customers by total sales — how much of revenue do they represent?
      (Hint: this is a Pareto / 80-20 question.)

**Deliverable:** A bar chart of sales by sub-category, and one sentence on whether
revenue is concentrated in a few customers/products or spread evenly.

---

## Stage 3 — Trend & timing
**Business question:** *When should we plan promotions or staffing?*
- [ ] Sales by month-of-year (aggregated across all years) — find the seasonal pattern.
- [ ] Which region/category grew fastest year over year? Which declined?
- [ ] Average shipping delay (`Ship Date` − `Order Date`) — does it vary by `Ship Mode`
      or region?

**Deliverable:** A short memo (5-8 sentences, written for a non-technical VP) covering:
what's growing, what's shrinking, and one recommendation.

---

## Stage 4 — Forecasting (stretch goal)
**Business question:** *What should we expect for sales next quarter?*
- [ ] Aggregate sales to monthly totals.
- [ ] Try a simple forecast: a moving average or `statsmodels`/`Prophet` model.
- [ ] Plot actual vs. forecast for the last few known months to sanity-check it.

**Deliverable:** A forecast chart for the next 3 months + one sentence of caveats
(e.g. "assumes no major promotions or supply disruptions").

---

## Stage 5 — Package it up
- [ ] Turn your best 3-4 charts + the memo from Stage 3 into a one-page summary
      (markdown, slide, or a simple dashboard — your choice of tool).
- [ ] Push it to your `super-store` repo with a proper commit message.

---

### Ground rules for practicing well
- Write the business question in your own words before writing code for it.
- Prefer a clear finding over a fancy chart — a BA's job is the sentence, not the plot.
- If you get stuck on *how* to compute something in pandas, ask for the pandas
  technique specifically — but try to answer the business question yourself first.
