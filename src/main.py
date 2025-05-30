import pandas as pd
import numpy as np                  
import matplotlib.pyplot as plt                       
import config as cfg 


def data():
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
    plt.gcf().canvas.mpl_connect("key_press_event" , on_key)    
    
    
def bar_chart(df):
    
    canada_sales = df[(df['region'] == 'Canada' ) & 
                 (df['parameter'].isin(["EV sales" ,"EV stock"])) &
                   (df['unit'] == "Vehicles")]
    
    china_sales = df [
        (df["region"] == "China")&
        (df["parameter"].isin(["EV sales" ,"EV stock"]))&
        (df["unit"] == "Vehicles") 
    ]
    usa_sales = df [
        (df["region"] == "USA")&
        (df["parameter"].isin(["EV sales" ,"EV stock"])) &
        (df["unit"] == "Vehicles")
    ]
    europe_sales = df [
        (df["region"] == "Europe")&
        (df["parameter"].isin(["EV sales" ,"EV stock"])) &
        (df["unit"] == "Vehicles")
    ]
    
    canada_total = canada_sales["value"].sum()
    usa_total = usa_sales["value"].sum()
    europe_total = europe_sales["value"].sum()
    china_total = china_sales["value"].sum()
    
    regions = ["Canada", "USA", "China", "Europe"]
    totals = [canada_total, usa_total, china_total, europe_total]
    sorted_totals_regions = sorted(zip(totals, regions))
    sorted_totals, sorted_regions = zip(*sorted_totals_regions)
    bar_colors = [cfg.colors[region] for region in sorted_regions]
    plt.bar( sorted_regions, sorted_totals, color=bar_colors)
    plt.title(cfg.title , fontsize=cfg.main_font_size , fontweight=cfg.font_weight)
    plt.xlabel("Region" , fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.ylabel("Vehicles Sold" , fontsize=cfg.font_size , fontweight=cfg.font_weight )
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_img(filename="bar.png")
    plt.show()

def stacked_bar(df):
    subset = df[
        (df['parameter'].isin(["EV sales", "EV stock", "EV sales share", "EV stock share"])) &
        (df['unit'] == "Vehicles") &
        (df['region'].isin(["Canada", "Belgium" , "USA" , "Brazil" , "China" , "Costa Rica" , "Denmark" , "Europe"]))
    ]
    grouped = subset.groupby(['region' ,'parameter' ])["value"].sum().unstack(fill_value=0)
    grouped['total'] = grouped.sum(axis=1)
    grouped = grouped.sort_values("total")
    grouped = grouped.drop(columns="total")
    ax = grouped.plot(kind='bar' , stacked=True , figsize=(12, 6) , color=[cfg.ev_sales_color ,cfg.ev_stock_color ])
    ax.legend(["EV sales" , "EV stock"] ,  title="Category")
    plt.title(cfg.title , fontsize=cfg.main_font_size , fontweight= cfg.font_weight)
    plt.ylabel("Value",  fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.xlabel("Region",  fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.xticks(rotation=90)
    plt.tight_layout()
    save_img(filename="bar.png")
    plt.show()
    
def scatter(df):
    china_sales = df [
        (df["region"] == "China")&
        (df["parameter"].isin(["EV sales" ,"EV stock"]))&
        (df["unit"] == "Vehicles") 
    ]
    usa_sales = df [
        (df["region"] == "USA")&
        (df["parameter"].isin(["EV sales" ,"EV stock"])) &
        (df["unit"] == "Vehicles")
    ]
    canada_sales = df [
        (df["region"] == "Canada")&
        (df["parameter"].isin(["EV sales" ,"EV stock"])) & 
        (df["unit"] == "Vehicles")
    ]
    europe_sales = df [
        (df["region"] == "Europe")&
        (df["parameter"].isin(["EV sales" ,"EV stock"])) &
        (df["unit"] == "Vehicles")
    ]
    china_ava = np.mean(china_sales["value"])
    usa_ava = np.mean(usa_sales["value"])
    canada_ava = np.mean(canada_sales["value"])
    europe_ava = np.mean(europe_sales["value"])
    
    plt.scatter([1,2,3,4],[china_ava , usa_ava , canada_ava , europe_ava])
    plt.xticks([1,2,3,4], ["China" , "USA" , "Canada" , "Europe"])
    plt.title(cfg.title , fontsize=cfg.main_font_size , fontweight=cfg.font_weight)
    plt.xlabel("region" , fontsize=cfg.font_size ,fontweight=cfg.font_weight )
    plt.ylabel("Value" ,fontsize=cfg.font_size ,fontweight=cfg.font_weight )
    plt.tight_layout()
    save_img(filename="bar.png")
    plt.show()
 
            
if __name__ == "__main__":
    df = data()
    while True:
        print("Welcome to Electric car sales")
        print("1. Bar chart")
        print("2. stacked bar")
        print("3. scatter")
        print("4. Exit")
        user = input("Enter the number:")
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
            print("invalid choice please try again")               