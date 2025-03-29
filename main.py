import streamlit as st
import pandas as pd
from utils import get_safe_function
from optimizer import gold_ratio_search
from animate import animate_gss
import numpy as np

st.set_page_config(page_title="Golden Section Search", layout="wide")
st.title("🔍 Golden Section Search Visualization")

# Inputs
f_expr_str = st.text_input("Function:", "np.sin(x)")
a = st.number_input("Start (a)", value=0.0)
b = st.number_input("End (b)", value=10.0)
tol = st.number_input("Tolerance", value=1e-4, format="%.8f")
extreme_type = st.radio("Optimization Type", ["max", "min"], horizontal=True)
show_steps = st.checkbox("Show steps", value=False)

# Start
if st.button("▶️ Start"):
    f = get_safe_function(f_expr_str)
    if f:
        try:
            opt_x, history, const_a, const_b = gold_ratio_search(f, a, b, extreme_type=extreme_type, tol=tol, show=show_steps)
            opt_val = f(opt_x)

            st.success(f"🔍 Optimum x ≈ {opt_x:.5f}")
            st.json({
                "Optimum Value": float(opt_val) if np.isfinite(opt_val) else "Undefined",
                "Number of Steps": len(history),
                "Tolerance": tol
            })

            # Step table
            if show_steps:
                df = pd.DataFrame(history, columns=["a", "b", "x1", "x2", "f(x1)", "f(x2)"])
                st.subheader("📜 Search Steps")
                st.dataframe(df.style.format(precision=5))

            # Plot
            fig = animate_gss(f, history, const_a, const_b)
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Invalid function expression.")
