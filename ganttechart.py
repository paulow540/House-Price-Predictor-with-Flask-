import numpy as np
import pandas as pd
import plotly_express as px
import plotly





housing = pd.read_csv("Housing.csv")

categorical_features = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]
print(housing)