import numpy as np
from scipy import optimize

import streamlit as st
from scipy.optimize import minimize

def optimize_function(x):
    return x**2 + 5*x

st.title("Optimization App")
x0 = st.number_input("Initial value for x:")
res = minimize(optimize_function, x0)
st.write("Optimized value of x:", res.x)
