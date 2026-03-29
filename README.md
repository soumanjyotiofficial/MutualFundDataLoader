# MutualFundDataLoader


A lightweight Python library for **programmatically downloading Indian Mutual Fund data**, including fund lists, latest NAV, and historical NAV data.

This library is designed for **financial analysts, data scientists, and quantitative researchers** who want to automate mutual fund data collection in Python.

---

## Why this project?

Collecting **Indian mutual fund data** for analysis is often difficult because:

- There is **no widely used Python SDK** for mutual fund data.
- Manual data collection is **time-consuming**.
- Automation for research or analytics becomes difficult.

To solve this problem, **MutualFundDataLoader** provides a simple interface to:

- Retrieve the **complete list of mutual funds**
- Identify **funds eligible for historical NAV data**
- Download **historical NAV data**
- Retrieve **latest NAV information**

This makes it easier to build:

- Investment research tools
- Portfolio analytics dashboards
- Quantitative finance models
- Personal finance tracking systems

---

# Features

- Fetch **complete mutual fund list**
- Identify **funds eligible for historical NAV data**
- Download **historical NAV data**
- Retrieve **latest NAV**
- Easy **pandas integration**
- Lightweight and easy to use

---

# Installation

Download the file from dist and then open the command prompt in download folder and type the following command

### Install from wheel

```bash
pip install mutualfunddataloader-0.1.0-py3-none-any.whl
```

### Install from source

```bash
pip install mutualfunddataloader-0.1.0.tar.gz
```

---

# Quick Start

```python
from mutualfunddataloader import MutualFundDataLoader
import pandas as pd

mf_loader = MutualFundDataLoader()
```

---

# Usage Examples

## 1. Get list of all mutual funds

```python
all_mf_list = mf_loader.get_all_mf_list()
all_mf_df = pd.DataFrame(all_mf_list)

print(all_mf_df.head())
```

---

## 2. Get funds eligible for historical NAV data

```python
eligible_mf_list = mf_loader.mf_eligible_for_historical()
eligible_mf_df = pd.DataFrame(eligible_mf_list)

print(eligible_mf_df.head())
```

---

## 3. Download historical NAV data

Example: **Edelweiss Nifty Next 50 Index Fund**

```python
nav_historical = mf_loader.get_historical_nav(
    scheme_code="150898",
    start_date="2023-01-01",
    end_date="2023-12-31"
)

historical_nav_df = pd.DataFrame(nav_historical["data"])

print(historical_nav_df.head())
```

---

## 4. Get latest NAV

```python
latest_nav = mf_loader.get_latest_nav("150898")

meta_data = latest_nav.get("meta")
nav_data = latest_nav.get("data")

print(meta_data)
print(nav_data)
```

---

# Output Format

### Historical NAV Data

| Date | NAV |
|-----|-----|
| 2023-01-01 | 15.42 |
| 2023-01-02 | 15.48 |

### Latest NAV

Includes:

- Scheme name
- Scheme code
- Latest NAV value
- Date of NAV

---

# Use Cases

This library can be used for:

- Financial Data Analysis
- Mutual Fund Research
- Portfolio Performance Tracking
- Quantitative Finance Projects
- Automated Data Pipelines
- Investment Analytics Tools

---

# Project Structure

```
mutualfunddataloader/
│
├── mutualfunddataloader/
│   ├── __init__.py
│   ├── mutualfunddataloader.py
│
├── dist/
│   ├── .whl
│   ├── .tar.gz
│
├── setup.py
├── LICENSE
└── README.md
```

---

# License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute

for personal or commercial purposes.

---

# Author

**Souman Jyoti**

Finance professional with a strong interest in:

- Financial Data Analysis
- Python for Finance
- Quantitative Research
- Automation in Investment Analysis

---

# Contributing

Contributions are welcome.

You can help by:

- Improving documentation
- Adding new features
- Fixing bugs
- Improving performance

Feel free to open an **issue** or submit a **pull request**.

---

# Future Improvements

Possible enhancements:

- Direct installation via **PyPI**
- Portfolio analytics utilities
- Mutual fund return calculations
- Risk metrics
- Integration with financial dashboards

---

# Support

If you find this project useful, consider:

⭐ Starring the repository  
🐛 Reporting issues  
🤝 Contributing improvements

---
