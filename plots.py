import matplotlib.pyplot as plt


class Plot:

    def unique_character(self, df):
        print("\nUnique Characters in this time slice:")
        print(df["Name"].unique())

    def scatter_plot(self, df):
        plt.figure(figsize=(80, 10))
        plt.scatter(df["TimeStamp"], df["Name"])
        # plt.xticks(df["TimeStamp"].unique())
        plt.show()
        plt.savefig("Scatter.jpg")

    def plot(self, df):
        plt.figure(figsize=(20, 3))
        plt.plot(df["TimeStamp"], df["Name"])
        plt.show()
        plt.savefig("Plot.jpg")

    def bar_plot(self, df):
        plt.figure(figsize=(20, 3))
        plt.bar(df["TimeStamp"], df["Name"])
        plt.show()
        plt.savefig("Bar.jpg")

    def histogram(self, df):
        hist = df.groupby('Name').count()
        hist.reset_index(inplace=True)
        hist.rename(columns={'TimeStamp': 'Count'}, inplace=True, errors='raise')
        hist = hist.sort_values(by=["Count"], ascending=False)
        print("\nCharacters occurance in this time stamp:")
        print(hist)
        plt.bar(hist["Name"], hist["Count"])
        plt.yticks(hist["Count"])
        plt.show()
        plt.savefig("Count.jpg")
