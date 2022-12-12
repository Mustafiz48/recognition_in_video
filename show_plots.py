import argparse
import pandas as pd
from plots import Plot


def show_plots(data_frame):
    plots.scatter_plot(data_frame)
    plots.unique_character(data_frame)
    plots.histogram(data_frame)


parser = argparse.ArgumentParser(description='Command line options for start and end time')
parser.add_argument('-st', '--start_time', required=True, help="Start time of the scene to analyze")
parser.add_argument('-et', '--end_time', required=True, help="End time of the scene to analyze")
args = vars(parser.parse_args())

df = pd.read_csv(r'Appearance/Appearance_sheet.csv', sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')
# print(df.head())
plots = Plot()

start_time = float(args["start_time"])
end_time = float(args["end_time"])
print("\nAnalyzing time slice:")
print(f"{start_time} to  {end_time}\n")


if (start_time == float(-1)) or (end_time == float(-1)):
    show_plots(data_frame=df)
else:
    time_slice = df.loc[(df['TimeStamp'] >= start_time) & (df['TimeStamp'] <= end_time)]
    show_plots(data_frame=time_slice)
