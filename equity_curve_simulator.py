import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to simulate equity curves
def simulate_equity_curves(risk_reward_ratio, win_rate, num_trades, num_simulations):
    equity_curves = []
    for _ in range(num_simulations):
        equity = 0
        equity_curve = []
        for _ in range(num_trades):
            if np.random.rand() < win_rate / 100.0:
                equity += risk_reward_ratio
            else:
                equity -= 1
            equity_curve.append(equity)
        equity_curves.append(equity_curve)
    return equity_curves

# Streamlit interface
st.title("Equity Curve Simulator")

st.sidebar.write("Adjust the parameters below:")

# Parameters
risk_reward_ratio = st.sidebar.slider('Risk-to-Reward Ratio', 0.5, 10.0, 2.0, step=0.1)
win_rate = st.sidebar.slider('Win Rate (%)', 0, 100, 40, step=1)
num_trades = st.sidebar.slider('Number of Trades', 100, 1000, 500, step=10)
num_simulations = st.sidebar.slider('Number of Simulations', 10, 100, 30, step=1)

# Simulate equity curves
equity_curves = simulate_equity_curves(risk_reward_ratio, win_rate, num_trades, num_simulations)

# Plot equity curves
st.subheader("Equity Curves")
fig, ax = plt.subplots()
for curve in equity_curves:
    ax.plot(curve)
ax.set_xlabel("Number of Trades")
ax.set_ylabel("Equity")
st.pyplot(fig)

# Footer
st.write("Created by [@yourusername](https://twitter.com/yourusername)")

