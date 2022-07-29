import pandas as pd
import plotly.express as px


def scatter3d(df: pd.DataFrame,
              x: str = "x",
              y: str = "y",
              z: str = "z",
              x_axis_title: str = "x-axis",
              y_axis_title: str = "y-axis",
              z_axis_title: str = "z-axis",
              color_group: str = None,
              save_as: str = None
              ) -> None:

    fig = px.scatter_3d(df,
                        x=x,
                        y=y,
                        z=z,
                        labels={x: x_axis_title,
                                y: y_axis_title,
                                z: z_axis_title},
                        color=color_group)

    fig.show()

    if save_as:
        with open(save_as, "w") as f:
            f.write(fig.to_html())
