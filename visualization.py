import matplotlib.pyplot as plt

def plot_fig(df):
    if df.empty:
        print("No Observation found")
        return

    plt.bar(df["Target"], df["Exposure (s)"])

    plt.xlabel("Target name")
    plt.ylabel("Exposure time (second)")
    plt.title("Target vs exposure time")

    plt.show()