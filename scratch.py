import numpy as np
import pandas as pd


t = np.linspace(0, 2*np.pi, 1000)
y = np.random.choice([-1, -0.4, 0, 1, 2, 3, 4], size=t.size)

df = pd.DataFrame(data={"x": t,
                        "y": y}
                  )

df['grp'] = df['y'].apply(lambda r: "high" if r > 0 else "low")

df.to_csv("test_data/bardata.csv")