import pandas as pd
import plotly.express as px


def bar(df: pd.DataFrame,
        x: str = "x",
        y: str = "y",
        x_axis_title: str = "x-axis",
        y_axis_title: str = "y-axis",
        color_group: str = None,
        save_as: str = None
        ) -> None:

    fig = px.bar(df,
                 x=x,
                 y=y,
                 labels={x: x_axis_title,
                         y: y_axis_title},
                 title=f"{x_axis_title} to {y_axis_title} with {color_group}",
                 color=color_group)

    fig.show()

    if save_as:
        with open(save_as, "w") as f:
            f.write(fig.to_html())
