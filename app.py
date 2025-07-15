from config import assets, portfolio_allocations
from data_loader import fetch_asset_data
from analysis import analyze_portfolio
from questionnaire import launch_questionnaires
import gradio as gr
import pandas as pd
from optimization import efficient_frontier_plot


# Load preprocessed return data
df_return = pd.read_csv("assets/asset_returns.csv", index_col=0, parse_dates=True)

# === 1. Personal Info + Risk Profile UI ===
user_ui, risk_ui = launch_questionnaires()

# === 2. Portfolio Analyzer Tab ===
portfolio_analyzer_ui = gr.Interface(
    fn=lambda risk, esg: analyze_portfolio(risk, esg, df_return, portfolio_allocations),
    inputs=[
        gr.Radio(["Conservative", "Moderate", "Aggressive"], label="📊 Risk Profile"),
        gr.Radio(["Yes", "No"], label="🌿 ESG Preference")
    ],
    outputs=[
        gr.Plot(label="📈 Portfolio Growth"),
        gr.Plot(label="📉 Correlation Heatmap"),
        gr.Dataframe(label="🧮 Asset-Level Metrics"),
        gr.Dataframe(label="💼 Portfolio Summary")
    ],
    title="📈 Portfolio Analyzer",
    description="Simulates how your portfolio might perform over time based on your risk and ESG preference."
)

# === 3. Efficient Frontier Tab ===
efficient_frontier_ui = gr.Interface(
    fn=efficient_frontier_plot,
    inputs=gr.Radio(["ESG", "Non-ESG"], label="🌿 Portfolio Type"),
    outputs=[
        gr.Plot(label="📊 Efficient Frontier"),
        gr.Dataframe(label="💼 Portfolio Weights"),
        gr.Dataframe(label="📈 Expected Returns")
    ],
    title="Efficient Frontier: ESG vs Non-ESG",
    description="Visualize the risk-return trade-offs and optimal portfolios."
)

# === Final Layout ===
gr.TabbedInterface(
    [user_ui, risk_ui, portfolio_analyzer_ui, efficient_frontier_ui],
    tab_names=["👤 Personal Info", "🧭 Risk Profile", "📈 Portfolio Analyzer", "📉 Efficient Frontier"]
).launch()
