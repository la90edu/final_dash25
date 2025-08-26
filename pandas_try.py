import pandas as pd
import numpy as np
import streamlit as st

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]

df=pd.DataFrame(data)
st.dataframe(df)
answer=df.mean()
st.dataframe(answer)
answer= np.mean(answer)
st.write(answer)