import pandas as pd
import plotly.express as px


def scatter(df: pd.DataFrame,
            x: str = "x",
            y: str = "y",
            x_axis_title: str = "x-axis",
            y_axis_title: str = "y-axis",
            color_group: str = None,
            trend_line: str = "ols",
            save_as: str = None
            ) -> None:

    fig = px.scatter(df,
               x=x,
               y=y,
               labels={x: x_axis_title,
                       y: y_axis_title},
               color=color_group,
               trendline=trend_line)

    fig.show()

    if save_as:
        with open(save_as, "w") as f:
            f.write(fig.to_html())
