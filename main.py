import pandas as pd
import math
import sqlite3
import numpy as np
from observation import Photometric_observation,Spectroscopic_observation
from visualization import plot_fig
from database import save_to_db



df = pd.DataFrame({
    "Type": pd.Series(dtype="string"),
    "Target": pd.Series(dtype="string"),
    "Observer": pd.Series(dtype="string"),
    "Filter": pd.Series(dtype="string"),
    "Exposure (s)": pd.Series(dtype="float64"),
    "Magnitude": pd.Series(dtype="float64"),
    "Wavelength (nm)": pd.Series(dtype="float64")})

def add_photometric_observation(df):
    
    target = input("Target: ")
    observer = input("Name of observer")
    filt = input("Filter name: ")

    try: 
        exposure = float(input("Exposure time(Second)"))
        if not math.isfinite(exposure) or exposure <= 0:
            print("Exposure must be a positive finite number")
            return df
    except ValueError:
        print("Exposure time should be an integer or float number")
        return df

    try:
        magnitude = float(input("Magnitude"))
        if not math.isfinite(magnitude):
                print("Magnitude must be a finite number")
                return df
    except ValueError:
        print("Magnitude should be an integer or float number")
        return df


    obs = Photometric_observation(target, observer, filt, exposure,magnitude)
    

    new_row = {
    "Type": "Photometric Observation",
    "Target": obs.target,
    "Observer": obs.observer,
    "Filter": obs.filter,
    "Exposure (s)": obs.exposure,
    "Magnitude": obs.magnitude,
    "Wavelength (nm)": np.nan}

    df = pd.concat([df, pd.DataFrame([new_row])],ignore_index=True)

    
    print("Photometric observation added Succesfully")

    return df


def add_spectroscopic_observation(df):
    
    target = input("Target: ")
    observer = input("Name of observer")
    filt = input("Filter name: ")

    try: 
        exposure = float(input("Exposure time(Second)"))
        if not math.isfinite(exposure) or exposure <= 0:
            print("Exposure must be a positive finite number")
            return df
    except ValueError:
        print("Exposure time should be an integer or float number")
        return df

    try:
        wavelength = float(input("Wavelength(nm)"))
        if not math.isfinite(wavelength) or  wavelength <= 0:
                print("Wavelength must be a positive finite number")
                return df 
    except ValueError:
        print("Wavelength should be an integer or float number")
        return df


    obs = Spectroscopic_observation(target, observer, filt, exposure,wavelength)
    


    new_row = {
        "Type": "Spectroscopic Observation",
        "Target": obs.target,
        "Observer": obs.observer,
        "Filter": obs.filter,
        "Exposure (s)": obs.exposure,
        "Magnitude": np.nan,
        "Wavelength (nm)": obs.wavelength}

    df = pd.concat([df, pd.DataFrame([new_row])],ignore_index=True)


    print("Spectroscopic observation added Succesfully")

    return df







def show_observation(df):
    if df.empty:
        print("No Observation found")
        return

    print(df)

def statistical_analysis(df, average=False, maximum=False, minimum=False, total=False):
    if df.empty:
        print("No Observation found")
        return

    if average:
        print(f"Average exposure time is  {df["Exposure (s)"].mean()} sec")

    if maximum:
        print(f"Maximum exposure time is  {df["Exposure (s)"].max()} sec")

    if minimum:
        print(f"Minimum exposure time is  {df["Exposure (s)"].min()} sec")

    if total:
        print(f"Total exposure time is  {df["Exposure (s)"].sum()} sec")



def search_observation(df):
    if df.empty:
        print("No Observation found")
        return

    target = input("Target: ")

    result = df[
        df["Target"].str.lower() == target.lower()
    ]

    if result.empty:
        print("No target name found")
    else:
        print("Observation found:")
        print(result)
        

def save_to_csv_file(df):
    if df.empty:
        print("No Observation found")
        return

    filename = input("Your file name: ")

    df.to_csv(
        f"{filename}.csv",
        index=True
    )

    print("Data saved successfully")


conn = sqlite3.connect("observation.db")
while True:
    print("=" * 40)
    print()
    print("Welcome to Observer Log".center(40))
    print()
    print("1. Add Photometric Observation")
    print("2. Add Spectroscopic Observation")
    print("3. Show Observation")
    print("4. Show Average exposure")
    print("5. Show Maximum exposure")
    print("6. Show Minimum exposure")
    print("7. Show Total exposure")
    print("8. Search target")
    print("9. Save to a csv file")
    print("10. Save to a database")
    print("11. Show bar chart for target  vs exposure time")
    print("12. Exit")
    
    choice = input("Choose:")
    
    if choice == "1":
        df = add_photometric_observation(df)
    elif choice == "2":
        df = add_spectroscopic_observation(df)
    elif choice == "3":
        show_observation(df)
    elif choice == "4":
        statistical_analysis(df, average=True)
    elif choice == "5":
        statistical_analysis(df, maximum=True)
    elif choice == "6":
        statistical_analysis(df, minimum=True)
    elif choice == "7":
        statistical_analysis(df, total=True)
    elif choice == "8":
        search_observation(df)
    elif choice == "9":
        save_to_csv_file(df)
    elif choice == "10":  
        save_to_db(df, conn)
    elif choice == "11":
        plot_fig(df)
    elif choice == "12":
        break
    else: 
        print("Please select 1 to 12")
conn.close()