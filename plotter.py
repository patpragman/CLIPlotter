"""
This script is the command line tool to route to the appropriate function.
"""
from plots.scatter import scatter
from plots.scatter3d import scatter3d
from plots.bar import bar
from defaultargs import parser
from routing import load_df

if __name__ == "__main__":
    args = parser.parse_args()

    df = load_df(args.f)

    x_name = args.x
    y_name = args.y
    z_name = args.z
    latitude = args.latitude
    longitude = args.longitude

    x_axis_title = args.x_axis_title
    y_axis_title = args.y_axis_title
    z_axis_title = args.z_axis_title

    if args.plot_type == "scatter":
        scatter(df, x_name, y_name, x_axis_title, y_axis_title,
                args.color_group,
                args.trend_line,
                args.save
                )
    elif args.plot_type == "scatter3d":
        scatter3d(df,
                  x_name,
                  y_name,
                  z_name,
                  x_axis_title,
                  y_axis_title,
                  z_axis_title,
                  args.color_group,
                  args.save
                  )
    elif args.plot_type == "bar":

        bar(df,
            x_name,
            y_name,
            x_axis_title,
            y_axis_title,
            args.color_group,
            args.save
            )
