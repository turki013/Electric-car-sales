import pandas as pd
import numpy as np                  
import matplotlib.pyplot as plt 
from time import sleep                      
import config as cfg 


def load_data():
    try:
        df = pd.read_csv("IEA-EV-dataEV salesHistoricalCars.csv")
        return df                   
    except FileNotFoundError:
        print("Sorry file not found")
    except Exception as e:
        print(f"Sorry something went wrong {e}")


def save_img(filename):
    def on_key(event):
        if event.key == 'S':
            plt.savefig(filename)
            print(f"📸 Snapshot saved! File: {filename}")
    plt.gcf().canvas.mpl_connect("key_press_event", on_key)


class Region:
    def __init__(self, df, region, years=None):
        self.df = df
        self.region = region
        self.years = years
        self.filtered = self.filter_data()
    
    def filter_data(self):
        data = self.df[
            (self.df["region"] == self.region) &
            (self.df["parameter"].isin(["EV sales", "EV stock"])) &
            (self.df["unit"] == "Vehicles")
        ]
        if self.years:
            data = data[data["year"].isin(self.years)]
        return data

    def total(self):
        return self.filtered["value"].sum()
    
    def average(self):
        return self.filtered["value"].mean()


def bar_chart(df):
    regions = ["Canada", "USA", "China", "Europe"]
    objects = [Region(df, r) for r in regions]
    totals = [obj.total() for obj in objects]
    sorted_totals_regions = sorted(zip(totals, regions))
    sorted_totals, sorted_regions = zip(*sorted_totals_regions)
    bar_colors = [cfg.colors[region] for region in sorted_regions]
    
    plt.bar(sorted_regions, sorted_totals, color=bar_colors)
    plt.title(cfg.title, fontsize=cfg.main_font_size, fontweight=cfg.font_weight)
    plt.xlabel("Region", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.ylabel("Vehicles Sold", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_img(filename="bar.png")
    plt.show()


def scatter(df):
    regions = ["China", "USA", "Canada", "Europe"]
    objects = [Region(df, r) for r in regions]
    avgs = [obj.average() for obj in objects]

    plt.scatter(range(1, 5), avgs)
    plt.xticks(range(1, 5), regions)
    plt.title(cfg.title, fontsize=cfg.main_font_size, fontweight=cfg.font_weight)
    plt.xlabel("Region", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.ylabel("Value", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.tight_layout()
    save_img(filename="scatter.png")
    plt.show()


def stacked_bar(df):
    subset = df[
        (df['parameter'].isin(["EV sales", "EV stock", "EV sales share", "EV stock share"])) &
        (df['unit'] == "Vehicles") &
        (df['region'].isin(["Canada", "Belgium", "USA", "Brazil", "China", "Costa Rica", "Denmark", "Europe"]))
    ]
    grouped = subset.groupby(['region', 'parameter'])["value"].sum().unstack(fill_value=0)
    grouped['total'] = grouped.sum(axis=1)
    grouped = grouped.sort_values("total")
    grouped = grouped.drop(columns="total")

    ax = grouped.plot(kind='bar', stacked=True, figsize=(12, 6),
                      color=[cfg.ev_sales_color, cfg.ev_stock_color])
    ax.legend(["EV sales", "EV stock"], title="Category")
    plt.title(cfg.title, fontsize=cfg.main_font_size, fontweight=cfg.font_weight)
    plt.ylabel("Value", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.xlabel("Region", fontsize=cfg.font_size, fontweight=cfg.font_weight)
    plt.xticks(rotation=90)
    plt.tight_layout()
    save_img(filename="stacked.png")
    plt.show()


if __name__ == "__main__":
    df = load_data()
    if df is not None:
        while True:
            print("Welcome to Electric car sales")
            print("1. Bar chart")
            print("2. Stacked bar")
            print("3. Scatter")
            print("4. Exit")
            user = input("Enter the number: ")
            if user == "1":
                bar_chart(df)
            elif user == "2":
                stacked_bar(df)
            elif user == "3":
                scatter(df)
            elif user == "4":
                print("Exiting the app...")
                break
            else:
                print("Invalid choice, please try again.")
                sleep(1)
