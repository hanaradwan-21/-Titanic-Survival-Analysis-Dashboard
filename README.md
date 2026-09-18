# 🚢 Titanic Survival Analysis Dashboard

An end-to-end data analysis project on the Titanic dataset — from raw data cleaning to an interactive Streamlit dashboard for exploring survival patterns.

## Overview

This project walks through the full data analysis pipeline:

1. **Data Cleaning & Feature Engineering** — handling missing values, extracting new features from raw columns.
2. **KPI & Insights Extraction** — computing key survival statistics and breakdowns.
3. **Interactive Dashboard** — a Streamlit web app for exploring the data visually, with live filters.

## Project Structure

```
├── cleaned_data.ipynb      # Data cleaning & feature engineering
├── KPIs_Insights.ipynb     # KPI calculations and survival breakdowns
├── DashBoard.ipynb         # Dashboard code (notebook version)
├── app.py                  # Streamlit dashboard app (script version)
├── cleaned_titanic.csv     # Output of the cleaning step (generated)
└── README.md
```

## Data Cleaning (`cleaned_data.ipynb`)

Starting from the raw Titanic dataset, the following steps were applied:

- Inspected shape, structure, missing values, and duplicates.
- Extracted passenger **Title** (e.g., Mr, Mrs, Miss) from the `Name` column, consolidating rare titles.
- Imputed missing **Age** values using the median age per title group.
- Created **Has_Cabin** (whether a cabin was recorded) and **Deck** (first letter of the cabin code), then dropped the original high-missing `Cabin` column.
- Engineered **FamilySize** and **IsAlone** from `SibSp` and `Parch`.
- Binned passengers into **AgeGroup** categories: Child, Teenager, Young Adult, Adult, Senior.
- Exported the result to `cleaned_titanic.csv`.

## Key Insights (`KPIs_Insights.ipynb`)

Overall KPIs computed on the cleaned dataset (418 passengers):

| Metric | Value |
|---|---|
| Total Passengers | 418 |
| Total Survived | 152 |
| Overall Survival Rate | 36.36% |
| Average Fare | $35.63 |
| Average Age | 29.7 years |

Survival rate breakdowns:

- **By Sex:** Female 100% vs. Male 0% *(note: reflects the sample used — worth double-checking against the full dataset)*
- **By Passenger Class:** 1st = 46.73%, 2nd = 32.26%, 3rd = 33.03%
- **By Travel Status:** Traveling with family = 50.91% vs. Traveling alone = 26.88%

## Dashboard (`app.py`)

An interactive **Streamlit + Plotly** dashboard featuring:

- Sidebar filters for **Gender** and **Passenger Class**
- Live KPI cards: total passengers, survivors, survival rate, average fare, average age
- Survival rate by **Class & Sex**
- Survival rate by **Age Group**
- Family status comparison (**alone vs. with family**)
- Fare distribution by class (box plot)
- Full filterable data table

### Running the dashboard

```bash
pip install streamlit pandas plotly
streamlit run app.py
```

Make sure `cleaned_titanic.csv` (produced by `cleaned_data.ipynb`) is in the same directory as `app.py`.

## Tech Stack

- **Python** — pandas, numpy
- **Visualization** — Plotly Express
- **Dashboard** — Streamlit

## Author

Built by Hana as part of an applied data analysis / ML portfolio project.
