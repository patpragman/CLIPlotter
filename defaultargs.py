import argparse

parser = argparse.ArgumentParser(description="Plot a .csv")
parser.add_argument("-t", "--plot_type", type=str, default="scatter")
parser.add_argument("-f", type=str)
parser.add_argument("-x", type=str, default='x')
parser.add_argument("--x_axis_title", type=str, default='x')

parser.add_argument("-y", type=str, default='y')
parser.add_argument("--y_axis_title", type=str, default='y')

parser.add_argument("-z", type=str, default='z')
parser.add_argument("--z_axis_title", type=str, default='z')

parser.add_argument("-lat", "--latitude", type=str, default='latitude')
parser.add_argument("-lon", "-long", "--longitude", type=str, default="longitude")

parser.add_argument("--save", "-s", type=str, default=None)
parser.add_argument("--trend_line", "-l", type=str, default="ols")
parser.add_argument("--color_group", "-g", type=str, default=None)