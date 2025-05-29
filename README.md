# Electric Vehicle Sales & Stock Visualizer 🚗📊


![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![CLI App](https://img.shields.io/badge/CLI%20App-Interactive-lightgrey)
![Menu Driven](https://img.shields.io/badge/Navigation-Menu%20Based-blue)
![Dataset](https://img.shields.io/badge/Data-CSV-orange)
![Status](https://img.shields.io/badge/Status-Ready-green)

This project is a command-line Python application designed to visualize electric vehicle (EV) data in different ways:

* Bar charts
* Stacked bar charts
* Scatter plots

The user interacts with the program via a menu system.

## File: `main.py`

* Entry point of the project.
* Provides user-friendly CLI for selecting chart types.
* Uses modular functions like `bar_chart()`, `stacked_bar()`, and `scatter()`.

## How It Works

When the user runs the program:

1. A menu appears.
2. The user selects a chart option.
3. The corresponding visualization function is called and displayed.

## Requirements

* Python 3.10+
* pandas
* matplotlib

Run with:

```bash
python main.py
```

Make sure the `IEA-EV-dataEV salesHistoricalCars.csv` file is properly placed and that `config.py` contains your styling settings.

---

Created for a data visualization assignment focused on electric vehicle trends.
