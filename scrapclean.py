from tkinter import Label
import pandas as pd


def main():

    filepath = r".\ScrapData.csv"
    df=pd.read_csv(filepath)
    df_new = df[['Lot', 'Tool', 'Scrap Qty', 'Scrap Date','Scrap Comments']]
    df_new.sort_values(by=['Tool'], inplace=True)
    print(df_new)
    df_new.to_csv('.\CleanScrap.csv')

if __name__ == "__main__":
    main()  