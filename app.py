# import streamlit as st
# import pandas as pd
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, IsolationForest
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.metrics import accuracy_score, r2_score
# from sklearn.impute import SimpleImputer
# from fuzzywuzzy import fuzz
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from io import StringIO
# from datetime import datetime

# # ===================== PAGE CONFIG =====================
# st.set_page_config(
#     page_title="DataForge — Data Analysis Suite",
#     page_icon="⬡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ===================== DESIGN SYSTEM =====================
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Syne:wght@400;500;600;700;800&display=swap');

# :root {
#     --bg:            #07090f;
#     --surface:       #0e1117;
#     --surface-2:     #161b27;
#     --surface-3:     #1c2333;
#     --border:        rgba(255,255,255,0.06);
#     --border-active: rgba(99,179,237,0.35);
#     --accent:        #5ba4e8;
#     --accent-2:      #38bdf8;
#     --accent-soft:   rgba(91,164,232,0.12);
#     --success:       #4ade80;
#     --success-soft:  rgba(74,222,128,0.10);
#     --warning:       #fbbf24;
#     --warning-soft:  rgba(251,191,36,0.10);
#     --danger:        #f87171;
#     --danger-soft:   rgba(248,113,113,0.10);
#     --text:          #dce6f0;
#     --text-muted:    #6b7a90;
#     --text-dim:      #3d4a5c;
#     --mono:          'JetBrains Mono', monospace;
#     --display:       'Syne', sans-serif;
# }

# /* ── Global Reset ── */
# html, body, [class*="css"] {
#     font-family: var(--mono);
#     background-color: var(--bg) !important;
#     color: var(--text);
# }
# .main .block-container {
#     padding: 0 2rem 4rem 2rem;
#     max-width: 1380px;
# }
# * { box-sizing: border-box; }

# /* ── Scrollbar ── */
# ::-webkit-scrollbar { width: 4px; height: 4px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: var(--border-active); border-radius: 2px; }

# /* ══════════════════════════════════════════
#    SIDEBAR
# ══════════════════════════════════════════ */
# section[data-testid="stSidebar"] {
#     background: var(--surface) !important;
#     border-right: 1px solid var(--border) !important;
#     width: 260px !important;
# }
# section[data-testid="stSidebar"] > div {
#     padding: 0 !important;
# }
# section[data-testid="stSidebar"] * {
#     color: var(--text) !important;
# }

# /* Sidebar inner wrapper */
# .sb-wrap {
#     display: flex;
#     flex-direction: column;
#     height: 100%;
#     padding: 0;
# }

# /* Brand */
# .sb-brand {
#     display: flex;
#     align-items: center;
#     gap: 10px;
#     padding: 22px 20px 18px;
#     border-bottom: 1px solid var(--border);
# }
# .sb-brand-icon {
#     font-size: 1.6rem;
#     filter: drop-shadow(0 0 10px rgba(91,164,232,0.5));
# }
# .sb-brand-name {
#     font-family: var(--display);
#     font-size: 1.15rem;
#     font-weight: 700;
#     color: var(--text) !important;
#     letter-spacing: -0.3px;
# }
# .sb-brand-version {
#     font-size: 0.6rem;
#     color: var(--text-muted) !important;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     margin-top: 1px;
# }

# /* Upload zone */
# .sb-upload-zone {
#     padding: 16px 16px 12px;
#     border-bottom: 1px solid var(--border);
# }

# /* Nav section label */
# .sb-nav-label {
#     font-size: 0.58rem;
#     letter-spacing: 0.16em;
#     text-transform: uppercase;
#     color: var(--text-dim) !important;
#     padding: 16px 20px 6px;
#     display: block;
# }

# /* Nav group */
# .sb-nav-group {
#     padding: 0 8px;
#     margin-bottom: 4px;
# }

# /* Status indicator */
# .sb-status {
#     padding: 12px 16px 16px;
#     border-top: 1px solid var(--border);
#     margin-top: auto;
# }
# .sb-status-row {
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     font-size: 0.72rem;
#     color: var(--text-muted) !important;
#     padding: 4px 0;
# }
# .sb-status-dot {
#     width: 6px; height: 6px;
#     border-radius: 50%;
#     display: inline-block;
# }
# .dot-green  { background: var(--success); box-shadow: 0 0 6px var(--success); }
# .dot-yellow { background: var(--warning); box-shadow: 0 0 6px var(--warning); }
# .dot-gray   { background: var(--text-dim); }
# .dot-blue   { background: var(--accent); box-shadow: 0 0 6px var(--accent); }

# /* Streamlit button → nav item */
# .stButton > button {
#     width: 100% !important;
#     background: transparent !important;
#     border: 1px solid transparent !important;
#     border-radius: 8px !important;
#     color: var(--text-muted) !important;
#     font-family: var(--mono) !important;
#     font-size: 0.8rem !important;
#     font-weight: 400 !important;
#     letter-spacing: 0.02em !important;
#     padding: 0.55rem 0.9rem !important;
#     text-align: left !important;
#     justify-content: flex-start !important;
#     transition: all 0.15s ease !important;
#     cursor: pointer !important;
# }
# .stButton > button:hover {
#     background: var(--accent-soft) !important;
#     border-color: var(--border-active) !important;
#     color: var(--accent) !important;
# }
# .stButton > button:active {
#     transform: scale(0.99) !important;
# }

# /* Active state hack */
# [data-active="true"] .stButton > button {
#     background: var(--accent-soft) !important;
#     border-color: var(--border-active) !important;
#     color: var(--accent) !important;
# }

# /* ══════════════════════════════════════════
#    TOPBAR
# ══════════════════════════════════════════ */
# .topbar {
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     padding: 18px 0 16px;
#     border-bottom: 1px solid var(--border);
#     margin-bottom: 24px;
# }
# .topbar-title {
#     font-family: var(--display);
#     font-size: 1.1rem;
#     font-weight: 600;
#     color: var(--text);
#     letter-spacing: -0.2px;
# }
# .topbar-breadcrumb {
#     font-size: 0.7rem;
#     color: var(--text-dim);
#     letter-spacing: 0.06em;
# }
# .topbar-right {
#     display: flex;
#     align-items: center;
#     gap: 10px;
# }
# .topbar-chip {
#     font-size: 0.65rem;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     color: var(--accent);
#     border: 1px solid var(--border-active);
#     background: var(--accent-soft);
#     padding: 4px 10px;
#     border-radius: 100px;
# }
# .topbar-time {
#     font-size: 0.68rem;
#     color: var(--text-dim);
# }

# /* ══════════════════════════════════════════
#    KPI CARDS
# ══════════════════════════════════════════ */
# .kpi-row {
#     display: grid;
#     grid-template-columns: repeat(4, 1fr);
#     gap: 12px;
#     margin-bottom: 24px;
# }
# .kpi-card {
#     background: var(--surface);
#     border: 1px solid var(--border);
#     border-radius: 12px;
#     padding: 18px 20px 16px;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.2s, box-shadow 0.2s;
# }
# .kpi-card:hover {
#     border-color: var(--border-active);
#     box-shadow: 0 4px 24px rgba(91,164,232,0.08);
# }
# .kpi-card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0; right: 0;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(91,164,232,0.4), transparent);
# }
# .kpi-label {
#     font-size: 0.62rem;
#     letter-spacing: 0.14em;
#     text-transform: uppercase;
#     color: var(--text-muted);
#     margin-bottom: 10px;
#     display: flex;
#     align-items: center;
#     gap: 6px;
# }
# .kpi-label-dot {
#     width: 5px; height: 5px;
#     border-radius: 50%;
#     background: var(--accent);
# }
# .kpi-value {
#     font-family: var(--display);
#     font-size: 2rem;
#     font-weight: 700;
#     color: var(--text);
#     line-height: 1;
#     letter-spacing: -1px;
# }
# .kpi-unit {
#     font-family: var(--mono);
#     font-size: 0.8rem;
#     color: var(--text-muted);
#     font-weight: 400;
#     letter-spacing: 0;
# }
# .kpi-sub {
#     font-size: 0.67rem;
#     color: var(--text-dim);
#     margin-top: 6px;
#     letter-spacing: 0.04em;
# }
# .kpi-score-good  { color: var(--success) !important; }
# .kpi-score-warn  { color: var(--warning) !important; }
# .kpi-score-bad   { color: var(--danger)  !important; }

# /* ══════════════════════════════════════════
#    CONTENT PANELS
# ══════════════════════════════════════════ */
# .panel {
#     background: var(--surface);
#     border: 1px solid var(--border);
#     border-radius: 14px;
#     padding: 24px;
#     margin-bottom: 20px;
# }
# .panel-header {
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     margin-bottom: 20px;
#     padding-bottom: 14px;
#     border-bottom: 1px solid var(--border);
# }
# .panel-title {
#     display: flex;
#     align-items: center;
#     gap: 10px;
# }
# .panel-icon {
#     width: 30px; height: 30px;
#     background: var(--accent-soft);
#     border: 1px solid var(--border-active);
#     border-radius: 7px;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 0.85rem;
# }
# .panel-name {
#     font-family: var(--display);
#     font-size: 0.92rem;
#     font-weight: 600;
#     color: var(--text);
#     letter-spacing: -0.2px;
# }
# .panel-badge {
#     font-size: 0.6rem;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     color: var(--text-dim);
#     border: 1px solid var(--border);
#     padding: 3px 8px;
#     border-radius: 100px;
# }

# /* ══════════════════════════════════════════
#    INSIGHTS
# ══════════════════════════════════════════ */
# .insight-block {
#     border-radius: 8px;
#     padding: 12px 16px;
#     margin: 6px 0;
#     border-left: 2px solid;
#     font-size: 0.82rem;
#     line-height: 1.55;
#     display: flex;
#     gap: 12px;
#     align-items: flex-start;
# }
# .insight-critical { background: var(--danger-soft);  border-color: var(--danger);  }
# .insight-warning  { background: var(--warning-soft); border-color: var(--warning); }
# .insight-info     { background: var(--accent-soft);  border-color: var(--accent);  }
# .insight-success  { background: var(--success-soft); border-color: var(--success); }
# .insight-icon     { font-size: 0.85rem; margin-top: 1px; flex-shrink: 0; }
# .insight-body     {}
# .insight-tag      { font-size: 0.62rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 3px; }
# .insight-msg      { font-size: 0.82rem; color: var(--text); }

# /* insight group header */
# .insight-group-label {
#     font-size: 0.62rem;
#     letter-spacing: 0.14em;
#     text-transform: uppercase;
#     color: var(--text-dim);
#     margin: 18px 0 6px;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }
# .insight-group-label::after {
#     content: '';
#     flex: 1;
#     height: 1px;
#     background: var(--border);
# }

# /* ══════════════════════════════════════════
#    COMPARISON
# ══════════════════════════════════════════ */
# .cmp-header {
#     font-size: 0.65rem;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     color: var(--text-muted);
#     margin-bottom: 10px;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }
# .cmp-dot-before { width:7px;height:7px;border-radius:50%;background:var(--text-dim);display:inline-block; }
# .cmp-dot-after  { width:7px;height:7px;border-radius:50%;background:var(--success);display:inline-block; }

# /* ══════════════════════════════════════════
#    TABS
# ══════════════════════════════════════════ */
# .stTabs [data-baseweb="tab-list"] {
#     background: var(--surface-2) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 9px !important;
#     padding: 3px !important;
#     gap: 2px !important;
# }
# .stTabs [data-baseweb="tab"] {
#     border-radius: 6px !important;
#     font-family: var(--mono) !important;
#     font-size: 0.74rem !important;
#     letter-spacing: 0.04em !important;
#     color: var(--text-muted) !important;
#     padding: 0.4rem 0.9rem !important;
# }
# .stTabs [aria-selected="true"] {
#     background: var(--accent-soft) !important;
#     color: var(--accent) !important;
#     border: 1px solid var(--border-active) !important;
# }

# /* ══════════════════════════════════════════
#    MISC STREAMLIT OVERRIDES
# ══════════════════════════════════════════ */
# .stSelectbox > div > div {
#     background: var(--surface-2) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 8px !important;
#     color: var(--text) !important;
#     font-family: var(--mono) !important;
#     font-size: 0.82rem !important;
# }
# .stDataFrame { border-radius: 10px; overflow: hidden; border: 1px solid var(--border); }
# .stAlert {
#     border-radius: 8px !important;
#     border: 1px solid var(--border) !important;
#     background: var(--surface-2) !important;
#     font-family: var(--mono) !important;
#     font-size: 0.78rem !important;
# }
# details summary {
#     font-family: var(--mono) !important;
#     font-size: 0.76rem !important;
#     letter-spacing: 0.06em !important;
#     color: var(--text-muted) !important;
# }
# hr {
#     border: none !important;
#     border-top: 1px solid var(--border) !important;
#     margin: 20px 0 !important;
# }
# .stProgress > div > div {
#     background: linear-gradient(90deg, var(--accent), var(--accent-2)) !important;
# }
# .stDownloadButton > button {
#     background: var(--accent) !important;
#     color: #07090f !important;
#     border: none !important;
#     font-family: var(--mono) !important;
#     font-size: 0.8rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.06em !important;
#     border-radius: 8px !important;
#     padding: 0.65rem 1.5rem !important;
# }
# .stDownloadButton > button:hover {
#     background: var(--accent-2) !important;
#     box-shadow: 0 0 20px rgba(91,164,232,0.3) !important;
# }
# [data-testid="stMetricValue"] {
#     font-family: var(--display) !important;
#     font-size: 1.5rem !important;
#     color: var(--text) !important;
# }
# [data-testid="stMetricLabel"] {
#     font-family: var(--mono) !important;
#     font-size: 0.7rem !important;
#     color: var(--text-muted) !important;
#     letter-spacing: 0.08em !important;
# }

# /* ══════════════════════════════════════════
#    WELCOME SCREEN
# ══════════════════════════════════════════ */
# .welcome-screen {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     min-height: 60vh;
#     text-align: center;
#     gap: 16px;
# }
# .welcome-glyph {
#     font-size: 4rem;
#     line-height: 1;
#     filter: drop-shadow(0 0 30px rgba(91,164,232,0.4));
#     margin-bottom: 8px;
#     animation: pulse-glow 3s ease-in-out infinite;
# }
# @keyframes pulse-glow {
#     0%, 100% { filter: drop-shadow(0 0 20px rgba(91,164,232,0.3)); }
#     50%       { filter: drop-shadow(0 0 40px rgba(91,164,232,0.7)); }
# }
# .welcome-heading {
#     font-family: var(--display);
#     font-size: 2.2rem;
#     font-weight: 700;
#     color: var(--text);
#     letter-spacing: -1px;
#     line-height: 1.15;
# }
# .welcome-heading span { color: var(--accent); }
# .welcome-sub {
#     font-size: 0.85rem;
#     color: var(--text-muted);
#     max-width: 380px;
#     line-height: 1.7;
# }
# .welcome-hint {
#     margin-top: 8px;
#     font-size: 0.72rem;
#     color: var(--text-dim);
#     border: 1px dashed var(--border);
#     padding: 10px 20px;
#     border-radius: 8px;
#     letter-spacing: 0.06em;
# }

# /* ══════════════════════════════════════════
#    FEATURE GRID (welcome)
# ══════════════════════════════════════════ */
# .feat-grid {
#     display: grid;
#     grid-template-columns: repeat(3, 1fr);
#     gap: 10px;
#     margin: 20px 0;
# }
# .feat-item {
#     background: var(--surface-2);
#     border: 1px solid var(--border);
#     border-radius: 10px;
#     padding: 14px 16px;
#     transition: border-color 0.2s;
# }
# .feat-item:hover { border-color: var(--border-active); }
# .feat-item-icon { font-size: 1.2rem; margin-bottom: 6px; }
# .feat-item-name {
#     font-size: 0.78rem;
#     font-weight: 500;
#     color: var(--text);
#     margin-bottom: 3px;
# }
# .feat-item-desc { font-size: 0.7rem; color: var(--text-muted); line-height: 1.5; }

# /* footer */
# .forge-footer {
#     text-align: center;
#     padding: 28px 0 16px;
#     font-size: 0.65rem;
#     color: var(--text-dim);
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
# }

# /* Divider with label */
# .divider-label {
#     display: flex;
#     align-items: center;
#     gap: 10px;
#     margin: 20px 0 16px;
#     font-size: 0.62rem;
#     letter-spacing: 0.14em;
#     text-transform: uppercase;
#     color: var(--text-dim);
# }
# .divider-label::before, .divider-label::after {
#     content: '';
#     flex: 1;
#     height: 1px;
#     background: var(--border);
# }

# /* Spinner override */
# .stSpinner > div { border-color: var(--accent) transparent transparent !important; }
# </style>
# """, unsafe_allow_html=True)


# # ===================== HELPER FUNCTIONS =====================

# def ensure_unique_columns(df: pd.DataFrame) -> pd.DataFrame:
#     df = df.copy()
#     seen: dict = {}
#     new_cols = []
#     for col in df.columns:
#         if col not in seen:
#             seen[col] = 0
#             new_cols.append(col)
#         else:
#             seen[col] += 1
#             new_cols.append(f"{col}_{seen[col]}")
#     df.columns = new_cols
#     return df


# # ===================== AI INSIGHTS ENGINE =====================

# class AIInsightsEngine:
#     def __init__(self, df: pd.DataFrame):
#         self.df = df

#     def generate_all_insights(self) -> list:
#         insights = []
#         df = self.df
#         rows, cols = df.shape

#         insights.append({'type': 'info', 'title': 'Dataset Overview',
#             'message': f"{rows:,} rows × {cols} columns loaded successfully.", 'priority': 'low'})

#         mem_mb = df.memory_usage(deep=True).sum() / 1024 ** 2
#         insights.append({'type': 'info', 'title': 'Memory Footprint',
#             'message': f"Dataset occupies {mem_mb:.2f} MB in memory.", 'priority': 'low'})

#         missing_pct = df.isnull().mean() * 100
#         critical_cols = missing_pct[missing_pct > 30]
#         moderate_cols = missing_pct[(missing_pct > 10) & (missing_pct <= 30)]

#         for col, pct in critical_cols.items():
#             insights.append({'type': 'critical', 'title': f'Critical Missing — {col}',
#                 'message': f"{pct:.1f}% values null. Consider dropping or imputing this column.",
#                 'priority': 'high'})

#         if not moderate_cols.empty:
#             cols_list = ", ".join(moderate_cols.index[:4])
#             insights.append({'type': 'warning', 'title': 'Moderate Missing Values',
#                 'message': f"{len(moderate_cols)} columns with 10–30% nulls: {cols_list}.",
#                 'priority': 'medium'})

#         total_missing = df.isnull().sum().sum()
#         if total_missing > 0:
#             overall_pct = total_missing / (rows * cols) * 100
#             insights.append({'type': 'info', 'title': 'Data Completeness',
#                 'message': f"{100 - overall_pct:.1f}% complete — {total_missing:,} missing cells.",
#                 'priority': 'medium'})
#         else:
#             insights.append({'type': 'success', 'title': 'Fully Complete Data',
#                 'message': "Zero missing values — excellent data integrity!", 'priority': 'low'})

#         numeric_cols = df.select_dtypes(include=[np.number]).columns
#         outlier_info = []
#         for col in numeric_cols[:8]:
#             series = df[col].dropna()
#             if len(series) < 4: continue
#             q1, q3 = series.quantile(0.25), series.quantile(0.75)
#             iqr = q3 - q1
#             if iqr == 0: continue
#             n_out = int(((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum())
#             if n_out > 0:
#                 outlier_info.append((col, n_out))
#         if outlier_info:
#             worst = sorted(outlier_info, key=lambda x: x[1], reverse=True)[0]
#             insights.append({'type': 'warning', 'title': 'Outliers Detected',
#                 'message': f"'{worst[0]}' has {worst[1]} outliers (IQR). {len(outlier_info)} col(s) affected.",
#                 'priority': 'medium'})

#         dup_count = int(df.duplicated().sum())
#         if dup_count == 0:
#             insights.append({'type': 'success', 'title': 'No Duplicate Rows',
#                 'message': "All rows are unique — great data hygiene!", 'priority': 'low'})
#         else:
#             dup_pct = dup_count / rows * 100
#             severity = 'critical' if dup_pct > 5 else 'warning'
#             insights.append({'type': severity, 'title': f'Duplicate Rows ({dup_pct:.1f}%)',
#                 'message': f"{dup_count:,} duplicate rows found. Remove before analysis.",
#                 'priority': 'high' if dup_pct > 5 else 'medium'})

#         cat_cols = df.select_dtypes(include='object').columns
#         insights.append({'type': 'info', 'title': 'Column Types',
#             'message': f"{len(numeric_cols)} numeric, {len(cat_cols)} categorical columns.",
#             'priority': 'low'})

#         if rows > 100 and len(numeric_cols) >= 2:
#             insights.append({'type': 'success', 'title': 'ML-Ready Dataset',
#                 'message': f"{rows:,} rows and {len(numeric_cols)} numeric features ready for ML.",
#                 'priority': 'low'})

#         return insights


# # ===================== DATA CLEANER =====================

# class AdvancedDataCleaner:
#     def __init__(self, df: pd.DataFrame):
#         self._original = ensure_unique_columns(df.copy())
#         self._cleaned = self._original.copy()
#         self.report: dict = {}

#     def find_fuzzy_duplicates(self, columns: list, threshold: int = 85) -> list:
#         df = self._cleaned
#         key = df[columns].astype(str).agg(' || '.join, axis=1) if len(columns) > 1 else df[columns[0]].astype(str)
#         matches = []
#         limit = min(500, len(df))
#         for i in range(limit):
#             for j in range(i + 1, min(i + 30, limit)):
#                 score = fuzz.ratio(key.iloc[i], key.iloc[j])
#                 if score >= threshold:
#                     matches.append({'row1': i, 'row2': j, 'similarity': score})
#         return matches

#     def remove_duplicates_smart(self, exact=True, fuzzy=False, fuzzy_threshold=85, columns_to_check=None):
#         to_drop: set = set()
#         subset = columns_to_check if columns_to_check else None
#         if exact:
#             dup_mask = self._cleaned.duplicated(subset=subset, keep='first')
#             to_drop.update(self._cleaned.index[dup_mask].tolist())
#             self.report['exact_removed'] = int(dup_mask.sum())
#         if fuzzy and columns_to_check:
#             fuzzy_cols = [c for c in columns_to_check if c in self._cleaned.columns]
#             if fuzzy_cols:
#                 matches = self.find_fuzzy_duplicates(fuzzy_cols, fuzzy_threshold)
#                 for m in matches:
#                     to_drop.add(m['row2'])
#                 self.report['fuzzy_removed'] = len(matches)
#         if to_drop:
#             self._cleaned = self._cleaned.drop(index=list(to_drop)).reset_index(drop=True)
#         self.report['total_removed'] = len(to_drop)

#     def full_clean(self, handle_fuzzy=False, fuzzy_threshold=85, columns_for_duplicates=None):
#         self._cleaned = self._original.copy()
#         self.report = {}
#         self.remove_duplicates_smart(exact=True, fuzzy=handle_fuzzy,
#             fuzzy_threshold=fuzzy_threshold, columns_to_check=columns_for_duplicates)
#         for col in self._cleaned.select_dtypes(include='object').columns:
#             self._cleaned[col] = self._cleaned[col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
#         for col in self._cleaned.columns:
#             null_count = self._cleaned[col].isnull().sum()
#             if null_count == 0: continue
#             if pd.api.types.is_numeric_dtype(self._cleaned[col]):
#                 self._cleaned[col] = self._cleaned[col].fillna(self._cleaned[col].median())
#             else:
#                 mode_vals = self._cleaned[col].mode()
#                 fill_val = mode_vals.iloc[0] if not mode_vals.empty else "Unknown"
#                 self._cleaned[col] = self._cleaned[col].fillna(fill_val)
#         return self.report

#     def get_original_df(self) -> pd.DataFrame: return self._original.copy()
#     def get_cleaned_df(self) -> pd.DataFrame: return self._cleaned.copy()
#     def export_cleaned_csv(self) -> str:
#         buf = StringIO(); self._cleaned.to_csv(buf, index=False); return buf.getvalue()


# # ===================== ML MODEL MANAGER =====================

# class MLModelManager:
#     def __init__(self, df: pd.DataFrame):
#         self.df = ensure_unique_columns(df)
#         self.model = None
#         self.feature_importance = None
#         self._scaler = StandardScaler()

#     def _prepare_X(self, df, cols):
#         X = df[cols].copy()
#         for c in X.select_dtypes(include='object').columns:
#             X[c] = LabelEncoder().fit_transform(X[c].astype(str))
#         X = pd.DataFrame(SimpleImputer(strategy='median').fit_transform(X), columns=cols)
#         return self._scaler.fit_transform(X)

#     def train_model(self, target_col: str):
#         feature_cols = [c for c in self.df.columns if c != target_col]
#         if not feature_cols: return None, None, None
#         X = self._prepare_X(self.df, feature_cols)
#         y_raw = self.df[target_col].copy()
#         if y_raw.dtype == 'object' or y_raw.nunique() <= 10:
#             y = LabelEncoder().fit_transform(y_raw.astype(str))
#             model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
#             problem = 'classification'
#         else:
#             y = SimpleImputer(strategy='median').fit_transform(y_raw.values.reshape(-1, 1)).ravel()
#             model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
#             problem = 'regression'
#         X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
#         model.fit(X_tr, y_tr)
#         y_pred = model.predict(X_te)
#         if problem == 'classification':
#             score = accuracy_score(y_te, y_pred); metrics = {'accuracy': score}
#         else:
#             score = r2_score(y_te, y_pred)
#             metrics = {'r2_score': score, 'rmse': float(np.sqrt(np.mean((y_te - y_pred) ** 2)))}
#         self.feature_importance = pd.DataFrame({
#             'feature': feature_cols, 'importance': model.feature_importances_
#         }).sort_values('importance', ascending=False).reset_index(drop=True)
#         self.model = model
#         return score, metrics, self.feature_importance

#     def detect_anomalies(self, contamination=0.1):
#         num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
#         if len(num_cols) < 2: return None
#         X = self._prepare_X(self.df, num_cols)
#         iso = IsolationForest(contamination=contamination, random_state=42, n_jobs=-1)
#         preds = iso.fit_predict(X)
#         return np.where(preds == -1)[0]


# # ===================== QUALITY SCORE =====================

# def calculate_quality_score(df: pd.DataFrame) -> float:
#     score = 100.0
#     n = len(df)
#     if n == 0: return 0.0
#     missing_pct = df.isnull().sum().sum() / (n * len(df.columns)) * 100
#     score -= missing_pct * 0.5
#     dup_pct = df.duplicated().sum() / n * 100
#     score -= dup_pct
#     for col in df.select_dtypes(include=[np.number]).columns[:3]:
#         series = df[col].dropna()
#         if len(series) < 4: continue
#         q1, q3 = series.quantile(0.25), series.quantile(0.75)
#         iqr = q3 - q1
#         if iqr == 0: continue
#         out_pct = ((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum() / n * 100
#         score -= out_pct * 0.2
#     return max(0.0, min(100.0, score))


# # ===================== PLOTLY THEME =====================

# PLOTLY_LAYOUT = dict(
#     paper_bgcolor='rgba(0,0,0,0)',
#     plot_bgcolor='rgba(14,17,23,0.8)',
#     font=dict(family='JetBrains Mono, monospace', color='#6b7a90', size=10),
#     margin=dict(l=28, r=28, t=36, b=28),
#     xaxis=dict(gridcolor='rgba(255,255,255,0.04)', linecolor='rgba(255,255,255,0.06)'),
#     yaxis=dict(gridcolor='rgba(255,255,255,0.04)', linecolor='rgba(255,255,255,0.06)'),
# )


# # ===================== VISUALIZATIONS =====================

# def create_visualizations(df: pd.DataFrame):
#     df = ensure_unique_columns(df)
#     numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
#     tab1, tab2, tab3, tab4 = st.tabs(["📈  Distribution", "🔗  Correlation", "🎻  Outlier / Nulls", "🔵  Scatter Explorer"])

#     with tab1:
#         if numeric_cols:
#             col = st.selectbox("Select column", numeric_cols, key="dist_col")
#             data = df[col].dropna()
#             if len(data):
#                 fig = make_subplots(rows=1, cols=2, subplot_titles=('Histogram', 'Box Plot'))
#                 fig.add_trace(go.Histogram(x=data, nbinsx=40,
#                     marker_color='#5ba4e8', marker_line_color='rgba(91,164,232,0.3)',
#                     marker_line_width=0.5, opacity=0.85), row=1, col=1)
#                 fig.add_trace(go.Box(x=data, boxmean='sd',
#                     marker_color='#38bdf8', line_color='#5ba4e8',
#                     fillcolor='rgba(91,164,232,0.12)'), row=1, col=2)
#                 fig.update_layout(height=400, showlegend=False, **PLOTLY_LAYOUT)
#                 st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.info("No numeric columns available.")

#     with tab2:
#         if len(numeric_cols) >= 2:
#             corr = df[numeric_cols].corr()
#             fig = px.imshow(corr, text_auto=".2f", aspect="auto",
#                 color_continuous_scale=[[0,'#07090f'],[0.5,'#1e3a5f'],[1,'#5ba4e8']],
#                 color_continuous_midpoint=0)
#             fig.update_layout(height=520, **PLOTLY_LAYOUT)
#             st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.info("Need ≥ 2 numeric columns for correlation matrix.")

#     with tab3:
#         if numeric_cols:
#             col = st.selectbox("Select column", numeric_cols, key="violin_col")
#             data = df[col].dropna()
#             if len(data):
#                 fig = go.Figure()
#                 fig.add_trace(go.Violin(y=data, box_visible=True, meanline_visible=True,
#                     fillcolor='rgba(91,164,232,0.12)', line_color='#5ba4e8',
#                     meanline=dict(color='#38bdf8', width=2)))
#                 fig.update_layout(title=col, height=380, **PLOTLY_LAYOUT)
#                 st.plotly_chart(fig, use_container_width=True)

#         null_sum = df.isnull().sum()
#         if null_sum.sum() > 0:
#             null_df = null_sum[null_sum > 0].reset_index()
#             null_df.columns = ['column', 'missing_count']
#             null_df['missing_pct'] = (null_df['missing_count'] / len(df) * 100).round(2)
#             fig2 = px.bar(null_df, x='column', y='missing_pct',
#                 title="Missing % by Column",
#                 color='missing_pct',
#                 color_continuous_scale=[[0,'#1e3a5f'],[1,'#5ba4e8']])
#             fig2.update_layout(height=320, **PLOTLY_LAYOUT)
#             st.plotly_chart(fig2, use_container_width=True)
#         else:
#             st.success("✓ Zero missing values detected.")

#     with tab4:
#         if len(numeric_cols) >= 2:
#             c1, c2 = st.columns(2)
#             x_col = c1.selectbox("X-axis", numeric_cols, key="sc_x")
#             y_col = c2.selectbox("Y-axis", numeric_cols, index=min(1, len(numeric_cols)-1), key="sc_y")
#             plot_data = df[[x_col, y_col]].dropna()
#             if len(plot_data):
#                 fig = px.scatter(plot_data, x=x_col, y=y_col,
#                     opacity=0.5, color_discrete_sequence=['#5ba4e8'])
#                 x_vals, y_vals = plot_data[x_col].values, plot_data[y_col].values
#                 m, b = np.polyfit(x_vals, y_vals, 1)
#                 x_line = np.linspace(x_vals.min(), x_vals.max(), 200)
#                 fig.add_trace(go.Scatter(x=x_line, y=m * x_line + b,
#                     mode='lines', line=dict(color='#38bdf8', width=2, dash='dot'),
#                     name='Linear trend'))
#                 fig.update_layout(height=480, **PLOTLY_LAYOUT)
#                 st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.info("Need ≥ 2 numeric columns for scatter explorer.")


# # ===================== INSIGHTS DISPLAY =====================

# def display_insights(insights: list):
#     icon_map = {'critical': '🔴', 'warning': '🟡', 'info': '🔵', 'success': '🟢'}
#     order = [('high', 'Critical Issues'), ('medium', 'Recommendations'), ('low', 'Observations')]
#     for priority, label in order:
#         group = [i for i in insights if i.get('priority') == priority]
#         if not group: continue
#         st.markdown(f'<div class="insight-group-label">{label}</div>', unsafe_allow_html=True)
#         for ins in group:
#             icon = icon_map.get(ins['type'], '◉')
#             cls = f"insight-{ins['type']}"
#             st.markdown(f"""
#             <div class="insight-block {cls}">
#                 <div class="insight-icon">{icon}</div>
#                 <div class="insight-body">
#                     <div class="insight-tag">{ins['title']}</div>
#                     <div class="insight-msg">{ins['message']}</div>
#                 </div>
#             </div>""", unsafe_allow_html=True)


# # ===================== SESSION STATE =====================

# _defaults = dict(
#     file_id=None, cleaner=None, data_cleaned=False,
#     insights=[], active_view='overview',
#     ml_results=None, anomaly_results=None,
# )
# for k, v in _defaults.items():
#     if k not in st.session_state:
#         st.session_state[k] = v


# # ══════════════════════════════════════════════════════════════
# # SIDEBAR
# # ══════════════════════════════════════════════════════════════

# with st.sidebar:
#     # Brand
#     st.markdown("""
#     <div class="sb-brand">
#         <div class="sb-brand-icon">⬡</div>
#         <div>
#             <div class="sb-brand-name">DataForge</div>
#             <div class="sb-brand-version">Professional Edition</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Upload
#     st.markdown('<div class="sb-upload-zone">', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader(
#         "Upload Dataset",
#         type=["csv"],
#         help="Accepts any well-formed CSV file",
#         label_visibility="visible"
#     )
#     st.markdown('</div>', unsafe_allow_html=True)

#     data_loaded = st.session_state.cleaner is not None

#     # ── Navigation ──
#     st.markdown('<span class="sb-nav-label">Navigation</span>', unsafe_allow_html=True)

#     nav_items = [
#         ("overview",     "📊", "Overview"),
#         ("insights",     "🧠", "AI Insights"),
#         ("visualize",    "📈", "Visualizations"),
#         ("clean",        "🧹", "Data Cleaning"),
#         ("ml",           "🤖", "ML Models"),
#         ("compare",      "🔄", "Before / After"),
#     ]

#     st.markdown('<div class="sb-nav-group">', unsafe_allow_html=True)
#     for key, icon, label in nav_items:
#         is_disabled = not data_loaded and key != "overview"
#         suffix = " ✓" if (key == "clean" and st.session_state.data_cleaned) else ""
#         if st.button(f"{icon}  {label}{suffix}", key=f"nav_{key}",
#                      disabled=is_disabled):
#             st.session_state.active_view = key
#             st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

#     # ── Download ──
#     if st.session_state.data_cleaned:
#         st.markdown('<span class="sb-nav-label">Export</span>', unsafe_allow_html=True)
#         st.download_button(
#             label="⬇  Download Cleaned CSV",
#             data=st.session_state.cleaner.export_cleaned_csv(),
#             file_name=f"dataforge_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
#             mime="text/csv",
#             use_container_width=True,
#             key="dl_sidebar"
#         )

#     # ── Status footer ──
#     if data_loaded:
#         orig = st.session_state.cleaner.get_original_df()
#         q = calculate_quality_score(orig)
#         q_color = "dot-green" if q >= 80 else ("dot-yellow" if q >= 60 else "dot-blue")
#         cleaned_dot = "dot-green" if st.session_state.data_cleaned else "dot-gray"
#         st.markdown(f"""
#         <div class="sb-status">
#             <div class="sb-status-row">
#                 <span>Quality Score</span>
#                 <span><span class="sb-status-dot {q_color}"></span>&nbsp;{q:.0f}/100</span>
#             </div>
#             <div class="sb-status-row">
#                 <span>Rows</span>
#                 <span>{len(orig):,}</span>
#             </div>
#             <div class="sb-status-row">
#                 <span>Cleaned</span>
#                 <span><span class="sb-status-dot {cleaned_dot}"></span>&nbsp;{'Yes' if st.session_state.data_cleaned else 'No'}</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════
# # FILE CHANGE DETECTION
# # ══════════════════════════════════════════════════════════════

# if uploaded_file is not None:
#     file_id = (uploaded_file.name, uploaded_file.size)
#     if file_id != st.session_state.file_id:
#         for k, v in _defaults.items():
#             st.session_state[k] = v
#         st.session_state.file_id = file_id
#         raw = ensure_unique_columns(pd.read_csv(uploaded_file))
#         st.session_state.cleaner = AdvancedDataCleaner(raw)
#         st.session_state.insights = AIInsightsEngine(raw).generate_all_insights()
#         st.session_state.active_view = 'overview'
#         st.rerun()


# # ══════════════════════════════════════════════════════════════
# # MAIN CONTENT
# # ══════════════════════════════════════════════════════════════

# cleaner = st.session_state.cleaner
# view = st.session_state.active_view

# # ── Helper: top bar ──
# def render_topbar(title: str, subtitle: str = "DataForge"):
#     now = datetime.now().strftime("%b %d, %Y · %H:%M")
#     st.markdown(f"""
#     <div class="topbar">
#         <div>
#             <div class="topbar-breadcrumb">{subtitle}</div>
#             <div class="topbar-title">{title}</div>
#         </div>
#         <div class="topbar-right">
#             <div class="topbar-chip">{'DATA LOADED' if cleaner else 'AWAITING DATA'}</div>
#             <div class="topbar-time">{now}</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# # ══════════════════════ WELCOME / NO DATA ══════════════════════
# if cleaner is None:
#     render_topbar("Welcome to DataForge")
#     st.markdown("""
#     <div class="welcome-screen">
#         <div class="welcome-glyph">⬡</div>
#         <div class="welcome-heading">Intelligent <span>Data Analysis</span><br>for Professionals</div>
#         <div class="welcome-sub">
#             Upload a CSV in the sidebar to unlock AI insights, automated cleaning,
#             interactive visualizations, and machine learning — all in one workspace.
#         </div>
#         <div class="welcome-hint">← Use the sidebar to upload your dataset</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="divider-label">Feature Overview</div>', unsafe_allow_html=True)
#     st.markdown("""
#     <div class="feat-grid">
#         <div class="feat-item">
#             <div class="feat-item-icon">🧹</div>
#             <div class="feat-item-name">Smart Cleaning</div>
#             <div class="feat-item-desc">Remove duplicates, impute missing values, normalize text</div>
#         </div>
#         <div class="feat-item">
#             <div class="feat-item-icon">🔍</div>
#             <div class="feat-item-name">Fuzzy Deduplication</div>
#             <div class="feat-item-desc">Detect near-duplicate text entries with fuzzy matching</div>
#         </div>
#         <div class="feat-item">
#             <div class="feat-item-icon">📈</div>
#             <div class="feat-item-name">Visualizations</div>
#             <div class="feat-item-desc">Distributions, correlations, violin plots, scatter explorer</div>
#         </div>
#         <div class="feat-item">
#             <div class="feat-item-icon">🤖</div>
#             <div class="feat-item-name">AutoML</div>
#             <div class="feat-item-desc">One-click Random Forest for classification or regression</div>
#         </div>
#         <div class="feat-item">
#             <div class="feat-item-icon">🕵️</div>
#             <div class="feat-item-name">Anomaly Detection</div>
#             <div class="feat-item-desc">Isolation Forest for multivariate outlier discovery</div>
#         </div>
#         <div class="feat-item">
#             <div class="feat-item-icon">🧠</div>
#             <div class="feat-item-name">AI Insights</div>
#             <div class="feat-item-desc">Automated quality report with prioritized recommendations</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # ══════════════════════ DATA LOADED ══════════════════════
# else:
#     orig = cleaner.get_original_df()
#     working = cleaner.get_cleaned_df() if st.session_state.data_cleaned else orig
#     quality = calculate_quality_score(orig)

#     # ─────────────── OVERVIEW ───────────────
#     if view == 'overview':
#         render_topbar("Overview", f"← {uploaded_file.name if uploaded_file else 'Dataset'}")

#         # KPI row
#         q_cls = "kpi-score-good" if quality >= 80 else ("kpi-score-warn" if quality >= 60 else "kpi-score-bad")
#         missing_total = int(orig.isnull().sum().sum())
#         dup_count = int(orig.duplicated().sum())
#         numeric_n = len(orig.select_dtypes(include=[np.number]).columns)

#         st.markdown(f"""
#         <div class="kpi-row">
#             <div class="kpi-card">
#                 <div class="kpi-label"><span class="kpi-label-dot"></span> Quality Score</div>
#                 <div class="kpi-value {q_cls}">{quality:.0f}<span class="kpi-unit">/100</span></div>
#                 <div class="kpi-sub">{'▲ Healthy' if quality >= 80 else '▼ Needs attention'}</div>
#             </div>
#             <div class="kpi-card">
#                 <div class="kpi-label"><span class="kpi-label-dot"></span> Total Rows</div>
#                 <div class="kpi-value">{len(orig):,}</div>
#                 <div class="kpi-sub">{len(orig) - dup_count:,} unique</div>
#             </div>
#             <div class="kpi-card">
#                 <div class="kpi-label"><span class="kpi-label-dot"></span> Columns</div>
#                 <div class="kpi-value">{orig.shape[1]}</div>
#                 <div class="kpi-sub">{numeric_n} numeric · {orig.shape[1] - numeric_n} categorical</div>
#             </div>
#             <div class="kpi-card">
#                 <div class="kpi-label"><span class="kpi-label-dot"></span> Missing Cells</div>
#                 <div class="kpi-value">{missing_total:,}</div>
#                 <div class="kpi-sub">{missing_total / (len(orig) * orig.shape[1]) * 100:.1f}% of dataset</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#         # Data preview
#         st.markdown("""
#         <div class="panel">
#             <div class="panel-header">
#                 <div class="panel-title">
#                     <div class="panel-icon">🗂</div>
#                     <div class="panel-name">Data Preview</div>
#                 </div>
#                 <div class="panel-badge">First 100 rows</div>
#             </div>
#         """, unsafe_allow_html=True)
#         st.dataframe(working.head(100), use_container_width=True, height=380)
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Column summary
#         with st.expander("📋  Column Schema & Statistics"):
#             col_info = pd.DataFrame({
#                 'Column': orig.columns,
#                 'Type': orig.dtypes.astype(str).values,
#                 'Non-Null': orig.count().values,
#                 'Null %': (orig.isnull().mean() * 100).round(1).values,
#                 'Unique': orig.nunique().values,
#             })
#             st.dataframe(col_info, use_container_width=True)

#     # ─────────────── AI INSIGHTS ───────────────
#     elif view == 'insights':
#         render_topbar("AI Insights", "Quality Analysis")
#         st.markdown("""
#         <div class="panel">
#             <div class="panel-header">
#                 <div class="panel-title">
#                     <div class="panel-icon">🧠</div>
#                     <div class="panel-name">Automated Quality Report</div>
#                 </div>
#                 <div class="panel-badge">AI-Generated</div>
#             </div>
#         """, unsafe_allow_html=True)
#         display_insights(st.session_state.insights)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # ─────────────── VISUALIZATIONS ───────────────
#     elif view == 'visualize':
#         render_topbar("Visualizations", "Data Exploration")
#         st.markdown("""
#         <div class="panel">
#             <div class="panel-header">
#                 <div class="panel-title">
#                     <div class="panel-icon">📈</div>
#                     <div class="panel-name">Interactive Charts</div>
#                 </div>
#                 <div class="panel-badge">Plotly</div>
#             </div>
#         """, unsafe_allow_html=True)
#         create_visualizations(working)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # ─────────────── DATA CLEANING ───────────────
#     elif view == 'clean':
#         render_topbar("Data Cleaning", "Preprocessing")
#         st.markdown("""
#         <div class="panel">
#             <div class="panel-header">
#                 <div class="panel-title">
#                     <div class="panel-icon">🧹</div>
#                     <div class="panel-name">Cleaning Operations</div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#         c1, c2 = st.columns(2)
#         with c1:
#             st.markdown("**Standard Clean**")
#             st.caption("Removes exact duplicate rows, imputes missing values with median/mode, and normalizes whitespace in text columns.")
#             if st.button("🧹  Run Standard Clean", key="btn_clean_v", use_container_width=True):
#                 with st.spinner("Cleaning…"):
#                     report = cleaner.full_clean(handle_fuzzy=False)
#                     st.session_state.data_cleaned = True
#                 removed = report.get('total_removed', 0)
#                 st.success(f"Done. Removed {removed:,} duplicate rows.")

#         with c2:
#             st.markdown("**Fuzzy Deduplication**")
#             st.caption("Detects near-duplicate text entries across categorical columns using string similarity (threshold: 85%).")
#             obj_cols = orig.select_dtypes(include='object').columns.tolist()
#             if obj_cols:
#                 if st.button("🔍  Run Fuzzy Clean", key="btn_fuzzy_v", use_container_width=True):
#                     with st.spinner("Fuzzy-matching…"):
#                         report = cleaner.full_clean(handle_fuzzy=True, fuzzy_threshold=85,
#                             columns_for_duplicates=obj_cols[:3])
#                         st.session_state.data_cleaned = True
#                     removed = report.get('total_removed', 0)
#                     st.success(f"Done. Removed {removed:,} rows.")
#             else:
#                 st.info("No text columns found for fuzzy matching.")

#         st.markdown("</div>", unsafe_allow_html=True)

#         if st.session_state.data_cleaned:
#             cleaned = cleaner.get_cleaned_df()
#             st.markdown('<div class="divider-label">Cleaned Dataset Preview</div>', unsafe_allow_html=True)
#             st.dataframe(cleaned.head(100), use_container_width=True, height=340)

#             col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
#             with col_dl2:
#                 st.download_button(
#                     label="⬇  Download Cleaned CSV",
#                     data=cleaner.export_cleaned_csv(),
#                     file_name=f"dataforge_cleaned_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
#                     mime="text/csv",
#                     use_container_width=True,
#                     key="dl_clean_page"
#                 )

#     # ─────────────── ML MODELS ───────────────
#     elif view == 'ml':
#         render_topbar("Machine Learning", "AutoML")
#         ml_df = ensure_unique_columns(working)
#         ml_mgr = MLModelManager(ml_df)

#         st.markdown("""
#         <div class="panel">
#             <div class="panel-header">
#                 <div class="panel-title">
#                     <div class="panel-icon">🤖</div>
#                     <div class="panel-name">Model Training</div>
#                 </div>
#                 <div class="panel-badge">Random Forest</div>
#             </div>
#         """, unsafe_allow_html=True)

#         target = st.selectbox("Target column for prediction", ml_df.columns, key="ml_target")
#         mc1, mc2 = st.columns(2)

#         with mc1:
#             if st.button("🚀  Train Model", key="btn_train", use_container_width=True):
#                 with st.spinner("Training…"):
#                     score, metrics, importance = ml_mgr.train_model(target)
#                 if score is None:
#                     st.error("Not enough feature columns.")
#                 else:
#                     label = "Accuracy" if 'accuracy' in metrics else "R² Score"
#                     val = metrics.get('accuracy', metrics.get('r2_score', 0))
#                     st.success(f"{label}: **{val:.3f}**")
#                     if 'rmse' in metrics:
#                         st.caption(f"RMSE: {metrics['rmse']:.4f}")
#                     st.markdown("**Feature Importance**")
#                     fig = px.bar(importance.head(10), x='importance', y='feature',
#                         orientation='h', color='importance',
#                         color_continuous_scale=[[0,'#1e3a5f'],[1,'#5ba4e8']])
#                     fig.update_layout(height=340, showlegend=False, yaxis_title='',
#                         **PLOTLY_LAYOUT)
#                     st.plotly_chart(fig, use_container_width=True)

#         with mc2:
#             if st.button("🕵️  Detect Anomalies", key="btn_anomaly", use_container_width=True):
#                 with st.spinner("Running Isolation Forest…"):
#                     anomalies = ml_mgr.detect_anomalies()
#                 if anomalies is None:
#                     st.error("Need ≥ 2 numeric columns.")
#                 elif len(anomalies) == 0:
#                     st.success("No anomalies found.")
#                 else:
#                     pct = len(anomalies) / len(ml_df) * 100
#                     st.warning(f"**{len(anomalies)}** anomalous rows ({pct:.1f}%)")
#                     with st.expander("View anomalous rows"):
#                         st.dataframe(ml_df.iloc[anomalies[:20]], use_container_width=True)

#         st.markdown("</div>", unsafe_allow_html=True)

#     # ─────────────── BEFORE / AFTER ───────────────
#     elif view == 'compare':
#         render_topbar("Before / After", "Comparison")
#         if not st.session_state.data_cleaned:
#             st.info("Run data cleaning first to see the before/after comparison.")
#         else:
#             cleaned = cleaner.get_cleaned_df()
#             st.markdown("""
#             <div class="panel">
#                 <div class="panel-header">
#                     <div class="panel-title">
#                         <div class="panel-icon">🔄</div>
#                         <div class="panel-name">Dataset Comparison</div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)

#             left, right = st.columns(2)
#             with left:
#                 st.markdown('<div class="cmp-header"><span class="cmp-dot-before"></span> Original</div>',
#                     unsafe_allow_html=True)
#                 a, b, c = st.columns(3)
#                 a.metric("Rows", f"{len(orig):,}")
#                 b.metric("Nulls", f"{orig.isnull().sum().sum():,}")
#                 c.metric("Dupes", f"{orig.duplicated().sum():,}")
#                 st.dataframe(orig, use_container_width=True, height=380)

#             with right:
#                 st.markdown('<div class="cmp-header"><span class="cmp-dot-after"></span> Cleaned</div>',
#                     unsafe_allow_html=True)
#                 a, b, c = st.columns(3)
#                 a.metric("Rows", f"{len(cleaned):,}", delta=f"{len(cleaned)-len(orig):,}")
#                 b.metric("Nulls", f"{cleaned.isnull().sum().sum():,}",
#                     delta=f"{cleaned.isnull().sum().sum() - orig.isnull().sum().sum():,}")
#                 c.metric("Dupes", f"{cleaned.duplicated().sum():,}",
#                     delta=f"{cleaned.duplicated().sum() - orig.duplicated().sum():,}")
#                 st.dataframe(cleaned, use_container_width=True, height=380)

#             st.markdown("</div>", unsafe_allow_html=True)

# # ── Footer ──
# st.markdown("""
# <div class="forge-footer">
#     ⬡ DataForge · Professional Data Analysis Suite · Smart Cleaning · AutoML · AI Insights
# </div>
# """, unsafe_allow_html=True)
#runnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, r2_score
from sklearn.impute import SimpleImputer
from fuzzywuzzy import fuzz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from io import StringIO
from datetime import datetime

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="DataForge — Data Analysis Suite",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== DESIGN SYSTEM =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300&display=swap');

:root {
    /* Core palette — deep slate with indigo accent */
    --bg:              #080c14;
    --bg-grid:         rgba(99,118,160,0.04);
    --surface-0:       #0c1220;
    --surface-1:       #111827;
    --surface-2:       #161e2e;
    --surface-3:       #1d2740;

    --border-subtle:   rgba(148,163,184,0.07);
    --border-default:  rgba(148,163,184,0.12);
    --border-strong:   rgba(148,163,184,0.22);
    --border-accent:   rgba(99,132,255,0.35);

    --accent:          #6384ff;
    --accent-light:    #818cf8;
    --accent-glow:     rgba(99,132,255,0.18);
    --accent-dim:      rgba(99,132,255,0.10);

    --emerald:         #34d399;
    --emerald-soft:    rgba(52,211,153,0.10);
    --amber:           #fbbf24;
    --amber-soft:      rgba(251,191,36,0.10);
    --rose:            #fb7185;
    --rose-soft:       rgba(251,113,133,0.10);
    --sky:             #38bdf8;
    --sky-soft:        rgba(56,189,248,0.10);

    --text-primary:    #e2e8f0;
    --text-secondary:  #94a3b8;
    --text-tertiary:   #475569;
    --text-disabled:   #2d3748;

    --font-sans:       'Plus Jakarta Sans', system-ui, sans-serif;
    --font-mono:       'DM Mono', 'Fira Code', monospace;
    --font-serif:      'Instrument Serif', Georgia, serif;

    --radius-sm:       6px;
    --radius-md:       10px;
    --radius-lg:       14px;
    --radius-xl:       20px;
    --radius-full:     9999px;

    --shadow-sm:       0 1px 3px rgba(0,0,0,0.4);
    --shadow-md:       0 4px 16px rgba(0,0,0,0.35);
    --shadow-lg:       0 12px 40px rgba(0,0,0,0.45);
    --shadow-accent:   0 0 40px rgba(99,132,255,0.15);
}

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: var(--font-sans);
    background-color: var(--bg) !important;
    color: var(--text-primary);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Grid background */
.main {
    background-image:
        linear-gradient(var(--bg-grid) 1px, transparent 1px),
        linear-gradient(90deg, var(--bg-grid) 1px, transparent 1px);
    background-size: 40px 40px;
    background-attachment: fixed;
}

.main .block-container {
    padding: 0 2.5rem 5rem 2.5rem;
    max-width: 1440px;
}

/* ── Custom Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--surface-0); }
::-webkit-scrollbar-thumb {
    background: var(--surface-3);
    border-radius: var(--radius-full);
}
::-webkit-scrollbar-thumb:hover { background: var(--border-strong); }

/* ══════════════════════════════════════════
   SIDEBAR — Refined command panel
══════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background: var(--surface-0) !important;
    border-right: 1px solid var(--border-default) !important;
    width: 272px !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }
section[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* Brand mark */
.sb-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 24px 20px 20px;
    border-bottom: 1px solid var(--border-subtle);
}
.sb-logo-wrap {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #6384ff 0%, #818cf8 100%);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    box-shadow: 0 0 16px rgba(99,132,255,0.4);
    flex-shrink: 0;
}
.sb-brand-text {}
.sb-brand-name {
    font-family: var(--font-sans) !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    letter-spacing: -0.3px;
    line-height: 1;
    margin-bottom: 2px;
}
.sb-brand-tagline {
    font-family: var(--font-mono) !important;
    font-size: 0.6rem !important;
    color: var(--text-tertiary) !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* Upload section */
.sb-section {
    padding: 16px 14px 12px;
    border-bottom: 1px solid var(--border-subtle);
}
.sb-section-label {
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-tertiary) !important;
    font-family: var(--font-mono) !important;
    margin-bottom: 10px;
    padding-left: 2px;
    display: block;
}

/* Upload zone styling */
[data-testid="stFileUploader"] {
    background: var(--surface-1) !important;
    border: 1.5px dashed var(--border-default) !important;
    border-radius: var(--radius-lg) !important;
    transition: all 0.2s ease !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--border-accent) !important;
    background: var(--accent-dim) !important;
}
[data-testid="stFileUploader"] label {
    font-family: var(--font-sans) !important;
    font-size: 0.78rem !important;
    color: var(--text-secondary) !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
    border: none !important;
}

/* Nav */
.sb-nav { padding: 10px 10px; }
.stButton > button {
    width: 100% !important;
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-secondary) !important;
    font-family: var(--font-sans) !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.58rem 0.85rem !important;
    text-align: left !important;
    justify-content: flex-start !important;
    transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.01em !important;
    margin-bottom: 2px !important;
}
.stButton > button:hover {
    background: var(--surface-2) !important;
    border-color: var(--border-default) !important;
    color: var(--text-primary) !important;
    transform: translateX(2px) !important;
}

/* Active nav item */
[data-active="true"] .stButton > button {
    background: var(--accent-dim) !important;
    border-color: var(--border-accent) !important;
    color: var(--accent) !important;
}

/* Sidebar footer */
.sb-footer {
    border-top: 1px solid var(--border-subtle);
    padding: 14px 16px;
    margin-top: auto;
}
.sb-stat-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 0;
    font-size: 0.72rem;
}
.sb-stat-key {
    color: var(--text-tertiary);
    font-family: var(--font-mono);
}
.sb-stat-val {
    font-family: var(--font-mono);
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 5px;
}
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 2px 7px;
    border-radius: var(--radius-full);
    font-size: 0.6rem;
    font-family: var(--font-mono);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.pill-good    { background: var(--emerald-soft); color: var(--emerald); border: 1px solid rgba(52,211,153,0.2); }
.pill-warn    { background: var(--amber-soft);   color: var(--amber);   border: 1px solid rgba(251,191,36,0.2); }
.pill-bad     { background: var(--rose-soft);    color: var(--rose);    border: 1px solid rgba(251,113,133,0.2); }
.pill-neutral { background: var(--surface-2);    color: var(--text-tertiary); border: 1px solid var(--border-subtle); }

/* ══════════════════════════════════════════
   TOPBAR / PAGE HEADER
══════════════════════════════════════════ */
.page-header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    padding: 28px 0 20px;
    border-bottom: 1px solid var(--border-subtle);
    margin-bottom: 28px;
}
.page-header-left {}
.page-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 6px;
}
.page-title {
    font-family: var(--font-sans);
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.5px;
    line-height: 1.2;
}
.page-header-right {
    display: flex;
    align-items: center;
    gap: 8px;
    padding-bottom: 3px;
}
.header-badge {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: var(--radius-full);
}
.badge-loaded {
    background: var(--emerald-soft);
    color: var(--emerald);
    border: 1px solid rgba(52,211,153,0.25);
}
.badge-idle {
    background: var(--surface-2);
    color: var(--text-tertiary);
    border: 1px solid var(--border-subtle);
}
.header-time {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text-tertiary);
}

/* ══════════════════════════════════════════
   KPI METRICS ROW
══════════════════════════════════════════ */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 28px;
}
.kpi-card {
    background: var(--surface-1);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 20px 22px 18px;
    position: relative;
    overflow: hidden;
    transition: all 0.22s ease;
    cursor: default;
}
.kpi-card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(135deg, rgba(255,255,255,0.02) 0%, transparent 60%);
    pointer-events: none;
}
.kpi-card:hover {
    border-color: var(--border-default);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}
.kpi-accent-bar {
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    border-radius: 0 0 0 var(--radius-lg);
}
.bar-blue   { background: linear-gradient(180deg, var(--accent), transparent); }
.bar-green  { background: linear-gradient(180deg, var(--emerald), transparent); }
.bar-amber  { background: linear-gradient(180deg, var(--amber), transparent); }
.bar-rose   { background: linear-gradient(180deg, var(--rose), transparent); }

.kpi-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 14px;
}
.kpi-label {
    font-family: var(--font-sans);
    font-size: 0.7rem;
    font-weight: 500;
    color: var(--text-tertiary);
    letter-spacing: 0.02em;
    text-transform: uppercase;
}
.kpi-icon {
    width: 26px; height: 26px;
    border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    background: var(--surface-2);
    border: 1px solid var(--border-subtle);
}
.kpi-value {
    font-family: var(--font-sans);
    font-size: 2rem;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -1.5px;
    line-height: 1;
    margin-bottom: 6px;
}
.kpi-value.v-good  { color: var(--emerald); }
.kpi-value.v-warn  { color: var(--amber); }
.kpi-value.v-bad   { color: var(--rose); }
.kpi-sub {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text-tertiary);
    letter-spacing: 0.04em;
}

/* ══════════════════════════════════════════
   PANELS / CARDS
══════════════════════════════════════════ */
.card {
    background: var(--surface-1);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    overflow: hidden;
    margin-bottom: 20px;
}
.card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 20px;
    border-bottom: 1px solid var(--border-subtle);
    background: var(--surface-0);
}
.card-title-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
}
.card-icon {
    width: 28px; height: 28px;
    background: var(--accent-dim);
    border: 1px solid var(--border-accent);
    border-radius: var(--radius-sm);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.78rem;
    flex-shrink: 0;
}
.card-title {
    font-family: var(--font-sans);
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-primary);
    letter-spacing: -0.1px;
}
.card-subtitle {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--text-tertiary);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 1px;
}
.card-meta {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--text-tertiary);
    background: var(--surface-2);
    border: 1px solid var(--border-subtle);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.card-body { padding: 20px; }

/* ══════════════════════════════════════════
   INSIGHTS
══════════════════════════════════════════ */
.insight-group-hd {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--text-tertiary);
    margin: 22px 0 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.insight-group-hd::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border-subtle);
}
.insight-item {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    padding: 13px 15px;
    border-radius: var(--radius-md);
    margin-bottom: 6px;
    border: 1px solid;
    transition: all 0.15s ease;
}
.insight-item:hover { transform: translateX(3px); }
.ins-critical { background: var(--rose-soft);    border-color: rgba(251,113,133,0.2); }
.ins-warning  { background: var(--amber-soft);   border-color: rgba(251,191,36,0.2); }
.ins-info     { background: var(--accent-dim);   border-color: rgba(99,132,255,0.2); }
.ins-success  { background: var(--emerald-soft); border-color: rgba(52,211,153,0.2); }

.insight-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    margin-top: 5px;
    flex-shrink: 0;
}
.dot-rose    { background: var(--rose);    box-shadow: 0 0 6px var(--rose); }
.dot-amber   { background: var(--amber);   box-shadow: 0 0 6px var(--amber); }
.dot-accent  { background: var(--accent);  box-shadow: 0 0 6px var(--accent); }
.dot-emerald { background: var(--emerald); box-shadow: 0 0 6px var(--emerald); }

.insight-tag {
    font-family: var(--font-sans);
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 2px;
}
.insight-msg {
    font-family: var(--font-sans);
    font-size: 0.76rem;
    color: var(--text-secondary);
    line-height: 1.55;
}

/* ══════════════════════════════════════════
   TABS
══════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface-0) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-md) !important;
    padding: 4px !important;
    gap: 2px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-sm) !important;
    font-family: var(--font-sans) !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    color: var(--text-tertiary) !important;
    padding: 0.45rem 1rem !important;
    transition: all 0.18s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-secondary) !important;
    background: var(--surface-2) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--accent-dim) !important;
    color: var(--accent-light) !important;
    border: 1px solid var(--border-accent) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding: 20px 0 0 !important; }

/* ══════════════════════════════════════════
   FORM ELEMENTS
══════════════════════════════════════════ */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-sans) !important;
    font-size: 0.82rem !important;
    transition: border-color 0.15s ease !important;
}
.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover {
    border-color: var(--border-accent) !important;
}

/* Download/Action Buttons */
.stDownloadButton > button {
    background: linear-gradient(135deg, #6384ff, #818cf8) !important;
    color: #fff !important;
    border: none !important;
    font-family: var(--font-sans) !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    border-radius: var(--radius-md) !important;
    padding: 0.65rem 1.5rem !important;
    letter-spacing: 0.01em !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(99,132,255,0.3) !important;
}
.stDownloadButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(99,132,255,0.45) !important;
}

/* Primary action buttons inside content */
.action-btn-wrap .stButton > button {
    background: linear-gradient(135deg, #6384ff, #818cf8) !important;
    color: #fff !important;
    border: none !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    border-radius: var(--radius-md) !important;
    padding: 0.65rem 1.2rem !important;
    box-shadow: 0 4px 14px rgba(99,132,255,0.25) !important;
    transition: all 0.2s ease !important;
}
.action-btn-wrap .stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(99,132,255,0.4) !important;
}

/* ══════════════════════════════════════════
   DATAFRAME
══════════════════════════════════════════ */
.stDataFrame {
    border-radius: var(--radius-lg) !important;
    overflow: hidden !important;
    border: 1px solid var(--border-subtle) !important;
}
[data-testid="stDataFrameResizable"] {
    background: var(--surface-1) !important;
}

/* ══════════════════════════════════════════
   ALERTS / MESSAGES
══════════════════════════════════════════ */
.stAlert {
    border-radius: var(--radius-md) !important;
    border: 1px solid var(--border-default) !important;
    background: var(--surface-2) !important;
    font-family: var(--font-sans) !important;
    font-size: 0.8rem !important;
}
.stSuccess { border-color: rgba(52,211,153,0.3) !important; background: var(--emerald-soft) !important; }
.stInfo    { border-color: rgba(99,132,255,0.3) !important; background: var(--accent-dim) !important; }
.stWarning { border-color: rgba(251,191,36,0.3) !important; background: var(--amber-soft) !important; }
.stError   { border-color: rgba(251,113,133,0.3) !important; background: var(--rose-soft) !important; }

/* Progress bar */
.stProgress > div > div {
    background: linear-gradient(90deg, var(--accent), var(--accent-light)) !important;
    border-radius: var(--radius-full) !important;
}

/* Spinner */
.stSpinner > div {
    border-color: var(--accent) transparent transparent !important;
}

/* Expander */
details {
    background: var(--surface-1) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-md) !important;
}
details summary {
    font-family: var(--font-sans) !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: var(--text-secondary) !important;
    padding: 12px 16px !important;
}

hr {
    border: none !important;
    border-top: 1px solid var(--border-subtle) !important;
    margin: 24px 0 !important;
}

/* Metrics */
[data-testid="stMetricValue"] {
    font-family: var(--font-sans) !important;
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    color: var(--text-primary) !important;
    letter-spacing: -0.5px !important;
}
[data-testid="stMetricLabel"] {
    font-family: var(--font-sans) !important;
    font-size: 0.7rem !important;
    color: var(--text-tertiary) !important;
    font-weight: 500 !important;
    letter-spacing: 0.03em !important;
}
[data-testid="stMetricDelta"] {
    font-family: var(--font-mono) !important;
    font-size: 0.7rem !important;
}

/* ══════════════════════════════════════════
   WELCOME / HERO SCREEN
══════════════════════════════════════════ */
.hero-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 62vh;
    text-align: center;
    gap: 0;
    padding: 40px 20px;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent-dim);
    border: 1px solid var(--border-accent);
    color: var(--accent-light);
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: var(--radius-full);
    margin-bottom: 22px;
}
.hero-badge-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 6px var(--accent);
    animation: blink 2s ease-in-out infinite;
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
}
.hero-title {
    font-family: var(--font-sans);
    font-size: 3.2rem;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -2px;
    line-height: 1.08;
    margin-bottom: 16px;
}
.hero-title em {
    font-style: normal;
    background: linear-gradient(135deg, #6384ff, #818cf8, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-family: var(--font-sans);
    font-size: 0.95rem;
    color: var(--text-secondary);
    max-width: 440px;
    line-height: 1.75;
    margin-bottom: 28px;
    font-weight: 400;
}
.hero-upload-hint {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    color: var(--text-tertiary);
    background: var(--surface-1);
    border: 1px dashed var(--border-default);
    border-radius: var(--radius-md);
    padding: 12px 24px;
    letter-spacing: 0.08em;
    margin-bottom: 48px;
}
.hero-upload-hint span { color: var(--accent-light); }

/* Feature cards grid */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    max-width: 720px;
    width: 100%;
}
.feature-card {
    background: var(--surface-1);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 18px;
    text-align: left;
    transition: all 0.22s ease;
    cursor: default;
}
.feature-card:hover {
    border-color: var(--border-accent);
    background: var(--surface-2);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}
.fc-emoji { font-size: 1.3rem; margin-bottom: 10px; display: block; }
.fc-name {
    font-family: var(--font-sans);
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}
.fc-desc {
    font-family: var(--font-sans);
    font-size: 0.72rem;
    color: var(--text-tertiary);
    line-height: 1.55;
}

/* ══════════════════════════════════════════
   COMPARISON VIEW
══════════════════════════════════════════ */
.cmp-col-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.cmp-indicator {
    width: 8px; height: 8px; border-radius: 2px;
}
.cmp-before { background: var(--text-tertiary); }
.cmp-after  { background: var(--emerald); box-shadow: 0 0 6px var(--emerald); }

/* ══════════════════════════════════════════
   DIVIDER WITH LABEL
══════════════════════════════════════════ */
.section-divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 26px 0 18px;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-tertiary);
}
.section-divider::before,
.section-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border-subtle);
}

/* ══════════════════════════════════════════
   CLEAN OPERATION CARDS
══════════════════════════════════════════ */
.op-card {
    background: var(--surface-1);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 20px;
    height: 100%;
    transition: border-color 0.2s;
}
.op-card:hover { border-color: var(--border-default); }
.op-card-icon { font-size: 1.5rem; margin-bottom: 12px; }
.op-card-title {
    font-family: var(--font-sans);
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 6px;
}
.op-card-desc {
    font-family: var(--font-sans);
    font-size: 0.75rem;
    color: var(--text-tertiary);
    line-height: 1.6;
    margin-bottom: 16px;
}

/* Footer */
.app-footer {
    text-align: center;
    padding: 32px 0 20px;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--text-tertiary);
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ===================== HELPER FUNCTIONS =====================

def ensure_unique_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    seen: dict = {}
    new_cols = []
    for col in df.columns:
        if col not in seen:
            seen[col] = 0
            new_cols.append(col)
        else:
            seen[col] += 1
            new_cols.append(f"{col}_{seen[col]}")
    df.columns = new_cols
    return df


# ===================== AI INSIGHTS ENGINE =====================

class AIInsightsEngine:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_all_insights(self) -> list:
        insights = []
        df = self.df
        rows, cols = df.shape

        insights.append({'type': 'info', 'title': 'Dataset Overview',
            'message': f"{rows:,} rows × {cols} columns loaded successfully.", 'priority': 'low'})

        mem_mb = df.memory_usage(deep=True).sum() / 1024 ** 2
        insights.append({'type': 'info', 'title': 'Memory Footprint',
            'message': f"Dataset occupies {mem_mb:.2f} MB in memory.", 'priority': 'low'})

        missing_pct = df.isnull().mean() * 100
        critical_cols = missing_pct[missing_pct > 30]
        moderate_cols = missing_pct[(missing_pct > 10) & (missing_pct <= 30)]

        for col, pct in critical_cols.items():
            insights.append({'type': 'critical', 'title': f'Critical Missing — {col}',
                'message': f"{pct:.1f}% values null. Consider dropping or imputing this column.",
                'priority': 'high'})

        if not moderate_cols.empty:
            cols_list = ", ".join(moderate_cols.index[:4])
            insights.append({'type': 'warning', 'title': 'Moderate Missing Values',
                'message': f"{len(moderate_cols)} columns with 10–30% nulls: {cols_list}.",
                'priority': 'medium'})

        total_missing = df.isnull().sum().sum()
        if total_missing > 0:
            overall_pct = total_missing / (rows * cols) * 100
            insights.append({'type': 'info', 'title': 'Data Completeness',
                'message': f"{100 - overall_pct:.1f}% complete — {total_missing:,} missing cells.",
                'priority': 'medium'})
        else:
            insights.append({'type': 'success', 'title': 'Fully Complete Data',
                'message': "Zero missing values — excellent data integrity!", 'priority': 'low'})

        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outlier_info = []
        for col in numeric_cols[:8]:
            series = df[col].dropna()
            if len(series) < 4: continue
            q1, q3 = series.quantile(0.25), series.quantile(0.75)
            iqr = q3 - q1
            if iqr == 0: continue
            n_out = int(((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum())
            if n_out > 0:
                outlier_info.append((col, n_out))
        if outlier_info:
            worst = sorted(outlier_info, key=lambda x: x[1], reverse=True)[0]
            insights.append({'type': 'warning', 'title': 'Outliers Detected',
                'message': f"'{worst[0]}' has {worst[1]} outliers (IQR). {len(outlier_info)} col(s) affected.",
                'priority': 'medium'})

        dup_count = int(df.duplicated().sum())
        if dup_count == 0:
            insights.append({'type': 'success', 'title': 'No Duplicate Rows',
                'message': "All rows are unique — great data hygiene!", 'priority': 'low'})
        else:
            dup_pct = dup_count / rows * 100
            severity = 'critical' if dup_pct > 5 else 'warning'
            insights.append({'type': severity, 'title': f'Duplicate Rows ({dup_pct:.1f}%)',
                'message': f"{dup_count:,} duplicate rows found. Remove before analysis.",
                'priority': 'high' if dup_pct > 5 else 'medium'})

        cat_cols = df.select_dtypes(include='object').columns
        insights.append({'type': 'info', 'title': 'Column Types',
            'message': f"{len(numeric_cols)} numeric, {len(cat_cols)} categorical columns.",
            'priority': 'low'})

        if rows > 100 and len(numeric_cols) >= 2:
            insights.append({'type': 'success', 'title': 'ML-Ready Dataset',
                'message': f"{rows:,} rows and {len(numeric_cols)} numeric features ready for ML.",
                'priority': 'low'})

        return insights


# ===================== DATA CLEANER =====================

class AdvancedDataCleaner:
    def __init__(self, df: pd.DataFrame):
        self._original = ensure_unique_columns(df.copy())
        self._cleaned = self._original.copy()
        self.report: dict = {}

    def find_fuzzy_duplicates(self, columns: list, threshold: int = 85) -> list:
        df = self._cleaned
        key = df[columns].astype(str).agg(' || '.join, axis=1) if len(columns) > 1 else df[columns[0]].astype(str)
        matches = []
        limit = min(500, len(df))
        for i in range(limit):
            for j in range(i + 1, min(i + 30, limit)):
                score = fuzz.ratio(key.iloc[i], key.iloc[j])
                if score >= threshold:
                    matches.append({'row1': i, 'row2': j, 'similarity': score})
        return matches

    def remove_duplicates_smart(self, exact=True, fuzzy=False, fuzzy_threshold=85, columns_to_check=None):
        to_drop: set = set()
        subset = columns_to_check if columns_to_check else None
        if exact:
            dup_mask = self._cleaned.duplicated(subset=subset, keep='first')
            to_drop.update(self._cleaned.index[dup_mask].tolist())
            self.report['exact_removed'] = int(dup_mask.sum())
        if fuzzy and columns_to_check:
            fuzzy_cols = [c for c in columns_to_check if c in self._cleaned.columns]
            if fuzzy_cols:
                matches = self.find_fuzzy_duplicates(fuzzy_cols, fuzzy_threshold)
                for m in matches:
                    to_drop.add(m['row2'])
                self.report['fuzzy_removed'] = len(matches)
        if to_drop:
            self._cleaned = self._cleaned.drop(index=list(to_drop)).reset_index(drop=True)
        self.report['total_removed'] = len(to_drop)

    def full_clean(self, handle_fuzzy=False, fuzzy_threshold=85, columns_for_duplicates=None):
        self._cleaned = self._original.copy()
        self.report = {}
        self.remove_duplicates_smart(exact=True, fuzzy=handle_fuzzy,
            fuzzy_threshold=fuzzy_threshold, columns_to_check=columns_for_duplicates)
        for col in self._cleaned.select_dtypes(include='object').columns:
            self._cleaned[col] = self._cleaned[col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
        for col in self._cleaned.columns:
            null_count = self._cleaned[col].isnull().sum()
            if null_count == 0: continue
            if pd.api.types.is_numeric_dtype(self._cleaned[col]):
                self._cleaned[col] = self._cleaned[col].fillna(self._cleaned[col].median())
            else:
                mode_vals = self._cleaned[col].mode()
                fill_val = mode_vals.iloc[0] if not mode_vals.empty else "Unknown"
                self._cleaned[col] = self._cleaned[col].fillna(fill_val)
        return self.report

    def get_original_df(self) -> pd.DataFrame: return self._original.copy()
    def get_cleaned_df(self) -> pd.DataFrame: return self._cleaned.copy()
    def export_cleaned_csv(self) -> str:
        buf = StringIO(); self._cleaned.to_csv(buf, index=False); return buf.getvalue()


# ===================== ML MODEL MANAGER =====================

class MLModelManager:
    def __init__(self, df: pd.DataFrame):
        self.df = ensure_unique_columns(df)
        self.model = None
        self.feature_importance = None
        self._scaler = StandardScaler()

    def _prepare_X(self, df, cols):
        X = df[cols].copy()
        for c in X.select_dtypes(include='object').columns:
            X[c] = LabelEncoder().fit_transform(X[c].astype(str))
        X = pd.DataFrame(SimpleImputer(strategy='median').fit_transform(X), columns=cols)
        return self._scaler.fit_transform(X)

    def train_model(self, target_col: str):
        feature_cols = [c for c in self.df.columns if c != target_col]
        if not feature_cols: return None, None, None
        X = self._prepare_X(self.df, feature_cols)
        y_raw = self.df[target_col].copy()
        if y_raw.dtype == 'object' or y_raw.nunique() <= 10:
            y = LabelEncoder().fit_transform(y_raw.astype(str))
            model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
            problem = 'classification'
        else:
            y = SimpleImputer(strategy='median').fit_transform(y_raw.values.reshape(-1, 1)).ravel()
            model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
            problem = 'regression'
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_te)
        if problem == 'classification':
            score = accuracy_score(y_te, y_pred); metrics = {'accuracy': score}
        else:
            score = r2_score(y_te, y_pred)
            metrics = {'r2_score': score, 'rmse': float(np.sqrt(np.mean((y_te - y_pred) ** 2)))}
        self.feature_importance = pd.DataFrame({
            'feature': feature_cols, 'importance': model.feature_importances_
        }).sort_values('importance', ascending=False).reset_index(drop=True)
        self.model = model
        return score, metrics, self.feature_importance

    def detect_anomalies(self, contamination=0.1):
        num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if len(num_cols) < 2: return None
        X = self._prepare_X(self.df, num_cols)
        iso = IsolationForest(contamination=contamination, random_state=42, n_jobs=-1)
        preds = iso.fit_predict(X)
        return np.where(preds == -1)[0]


# ===================== QUALITY SCORE =====================

def calculate_quality_score(df: pd.DataFrame) -> float:
    score = 100.0
    n = len(df)
    if n == 0: return 0.0
    missing_pct = df.isnull().sum().sum() / (n * len(df.columns)) * 100
    score -= missing_pct * 0.5
    dup_pct = df.duplicated().sum() / n * 100
    score -= dup_pct
    for col in df.select_dtypes(include=[np.number]).columns[:3]:
        series = df[col].dropna()
        if len(series) < 4: continue
        q1, q3 = series.quantile(0.25), series.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0: continue
        out_pct = ((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum() / n * 100
        score -= out_pct * 0.2
    return max(0.0, min(100.0, score))


# ===================== PLOTLY THEME =====================

PLOTLY_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(17,24,39,0.6)',
    font=dict(family='Plus Jakarta Sans, system-ui, sans-serif', color='#475569', size=10),
    margin=dict(l=16, r=16, t=40, b=16),
    xaxis=dict(
        gridcolor='rgba(148,163,184,0.05)',
        linecolor='rgba(148,163,184,0.08)',
        tickfont=dict(size=9, color='#475569'),
    ),
    yaxis=dict(
        gridcolor='rgba(148,163,184,0.05)',
        linecolor='rgba(148,163,184,0.08)',
        tickfont=dict(size=9, color='#475569'),
    ),
    hoverlabel=dict(
        bgcolor='#1d2740',
        bordercolor='rgba(148,163,184,0.15)',
        font=dict(family='Plus Jakarta Sans', size=11, color='#e2e8f0'),
    ),
)

COLOR_SEQ = ['#6384ff', '#34d399', '#fbbf24', '#fb7185', '#38bdf8', '#a78bfa']


# ===================== VISUALIZATIONS =====================

def create_visualizations(df: pd.DataFrame):
    df = ensure_unique_columns(df)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    tab1, tab2, tab3, tab4 = st.tabs(
        ["  Distribution  ", "  Correlation  ", "  Outliers & Nulls  ", "  Scatter Explorer  "]
    )

    with tab1:
        if numeric_cols:
            col = st.selectbox("Column", numeric_cols, key="dist_col", label_visibility="collapsed")
            data = df[col].dropna()
            if len(data):
                fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Distribution', 'Box Plot'),
                    horizontal_spacing=0.06)
                fig.add_trace(go.Histogram(
                    x=data, nbinsx=45,
                    marker=dict(
                        color='rgba(99,132,255,0.75)',
                        line=dict(color='rgba(99,132,255,0.3)', width=0.5)
                    )), row=1, col=1)
                fig.add_trace(go.Box(
                    x=data, boxmean='sd',
                    marker=dict(color='#6384ff', size=4, opacity=0.6),
                    line=dict(color='#6384ff', width=1.5),
                    fillcolor='rgba(99,132,255,0.1)',
                    whiskerwidth=0.6), row=1, col=2)
                fig.update_layout(height=400, showlegend=False,
                    title_text=col, title_font=dict(size=11, color='#94a3b8'),
                    **PLOTLY_LAYOUT)
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns available.")

    with tab2:
        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr()
            fig = px.imshow(corr,
                text_auto=".2f",
                aspect="auto",
                color_continuous_scale=[
                    [0, '#0c1220'],
                    [0.25, '#1e3a5f'],
                    [0.5, '#1d2740'],
                    [0.75, '#2d4a7a'],
                    [1, '#6384ff']
                ],
                color_continuous_midpoint=0)
            fig.update_traces(textfont=dict(size=9, color='rgba(226,232,240,0.7)'))
            fig.update_layout(height=520, **PLOTLY_LAYOUT)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need ≥ 2 numeric columns for correlation matrix.")

    with tab3:
        if numeric_cols:
            col = st.selectbox("Column", numeric_cols, key="violin_col", label_visibility="collapsed")
            data = df[col].dropna()
            if len(data):
                fig = go.Figure()
                fig.add_trace(go.Violin(
                    y=data,
                    box_visible=True,
                    meanline_visible=True,
                    fillcolor='rgba(99,132,255,0.1)',
                    line=dict(color='#6384ff', width=1.5),
                    meanline=dict(color='#34d399', width=2),
                    points='outliers',
                    marker=dict(color='#fb7185', size=4, opacity=0.7)
                ))
                fig.update_layout(title_text=col,
                    title_font=dict(size=11, color='#94a3b8'),
                    height=380, **PLOTLY_LAYOUT)
                st.plotly_chart(fig, use_container_width=True)

        null_sum = df.isnull().sum()
        if null_sum.sum() > 0:
            null_df = null_sum[null_sum > 0].reset_index()
            null_df.columns = ['column', 'missing_count']
            null_df['missing_pct'] = (null_df['missing_count'] / len(df) * 100).round(2)
            fig2 = px.bar(null_df, x='column', y='missing_pct',
                title="Missing Values by Column (%)",
                color='missing_pct',
                color_continuous_scale=[
                    [0, '#1e3a5f'],
                    [0.5, '#6384ff'],
                    [1, '#fb7185']
                ],
                text_auto='.1f')
            fig2.update_traces(marker_line_width=0, textfont_size=9)
            fig2.update_layout(
                height=320,
                title_font=dict(size=11, color='#94a3b8'),
                coloraxis_showscale=False,
                **PLOTLY_LAYOUT
            )
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.success("✓ Zero missing values detected across all columns.")

    with tab4:
        if len(numeric_cols) >= 2:
            c1, c2 = st.columns(2)
            x_col = c1.selectbox("X axis", numeric_cols, key="sc_x")
            y_col = c2.selectbox("Y axis", numeric_cols, index=min(1, len(numeric_cols)-1), key="sc_y")
            plot_data = df[[x_col, y_col]].dropna()
            if len(plot_data):
                fig = px.scatter(plot_data, x=x_col, y=y_col,
                    opacity=0.55,
                    color_discrete_sequence=['#6384ff'])
                x_vals, y_vals = plot_data[x_col].values, plot_data[y_col].values
                m, b = np.polyfit(x_vals, y_vals, 1)
                x_line = np.linspace(x_vals.min(), x_vals.max(), 200)
                fig.add_trace(go.Scatter(
                    x=x_line, y=m * x_line + b,
                    mode='lines',
                    line=dict(color='#34d399', width=2, dash='dot'),
                    name='Linear trend'))
                fig.update_traces(
                    marker=dict(size=6, line=dict(width=0.5, color='rgba(99,132,255,0.3)')),
                    selector=dict(mode='markers'))
                fig.update_layout(height=460, **PLOTLY_LAYOUT)
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need ≥ 2 numeric columns for scatter explorer.")


# ===================== INSIGHTS DISPLAY =====================

def display_insights(insights: list):
    dot_map = {
        'critical': ('dot-rose', 'ins-critical'),
        'warning':  ('dot-amber', 'ins-warning'),
        'info':     ('dot-accent', 'ins-info'),
        'success':  ('dot-emerald', 'ins-success'),
    }
    order = [('high', 'Critical Issues'), ('medium', 'Recommendations'), ('low', 'Observations')]
    for priority, label in order:
        group = [i for i in insights if i.get('priority') == priority]
        if not group: continue
        st.markdown(f'<div class="insight-group-hd">{label}</div>', unsafe_allow_html=True)
        for ins in group:
            dot_cls, item_cls = dot_map.get(ins['type'], ('dot-accent', 'ins-info'))
            st.markdown(f"""
            <div class="insight-item {item_cls}">
                <div class="insight-dot {dot_cls}"></div>
                <div>
                    <div class="insight-tag">{ins['title']}</div>
                    <div class="insight-msg">{ins['message']}</div>
                </div>
            </div>""", unsafe_allow_html=True)


# ===================== SESSION STATE =====================

_defaults = dict(
    file_id=None, cleaner=None, data_cleaned=False,
    insights=[], active_view='overview',
    ml_results=None, anomaly_results=None,
)
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-logo-wrap">◈</div>
        <div class="sb-brand-text">
            <div class="sb-brand-name">DataForge</div>
            <div class="sb-brand-tagline">Analysis Suite</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    st.markdown('<span class="sb-section-label">Dataset</span>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
        help="Upload any well-formed CSV file to begin",
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    data_loaded = st.session_state.cleaner is not None

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    st.markdown('<span class="sb-section-label">Navigation</span>', unsafe_allow_html=True)

    nav_items = [
        ("overview",  "📊", "Overview"),
        ("insights",  "🧠", "AI Insights"),
        ("visualize", "📈", "Visualizations"),
        ("clean",     "🧹", "Data Cleaning"),
        ("ml",        "🤖", "ML Models"),
        ("compare",   "🔄", "Before / After"),
    ]

    for key, icon, label in nav_items:
        is_disabled = not data_loaded and key != "overview"
        suffix = "  ✓" if (key == "clean" and st.session_state.data_cleaned) else ""
        if st.button(f"{icon}  {label}{suffix}", key=f"nav_{key}", disabled=is_disabled):
            st.session_state.active_view = key
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.data_cleaned:
        st.markdown('<div class="sb-section">', unsafe_allow_html=True)
        st.markdown('<span class="sb-section-label">Export</span>', unsafe_allow_html=True)
        st.download_button(
            label="⬇  Download Cleaned CSV",
            data=st.session_state.cleaner.export_cleaned_csv(),
            file_name=f"dataforge_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True,
            key="dl_sidebar"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    if data_loaded:
        orig = st.session_state.cleaner.get_original_df()
        q = calculate_quality_score(orig)
        if q >= 80:
            pill_cls, pill_txt = "pill-good", f"{q:.0f}/100"
        elif q >= 60:
            pill_cls, pill_txt = "pill-warn", f"{q:.0f}/100"
        else:
            pill_cls, pill_txt = "pill-bad", f"{q:.0f}/100"

        cleaned_pill = "pill-good" if st.session_state.data_cleaned else "pill-neutral"
        cleaned_txt  = "Done" if st.session_state.data_cleaned else "Pending"

        st.markdown(f"""
        <div class="sb-footer">
            <div class="sb-stat-row">
                <span class="sb-stat-key">Quality</span>
                <span class="status-pill {pill_cls}">{pill_txt}</span>
            </div>
            <div class="sb-stat-row">
                <span class="sb-stat-key">Rows</span>
                <span class="sb-stat-val">{len(orig):,}</span>
            </div>
            <div class="sb-stat-row">
                <span class="sb-stat-key">Columns</span>
                <span class="sb-stat-val">{orig.shape[1]}</span>
            </div>
            <div class="sb-stat-row">
                <span class="sb-stat-key">Cleaned</span>
                <span class="status-pill {cleaned_pill}">{cleaned_txt}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# FILE CHANGE DETECTION
# ══════════════════════════════════════════════════════════════

if uploaded_file is not None:
    file_id = (uploaded_file.name, uploaded_file.size)
    if file_id != st.session_state.file_id:
        for k, v in _defaults.items():
            st.session_state[k] = v
        st.session_state.file_id = file_id
        raw = ensure_unique_columns(pd.read_csv(uploaded_file))
        st.session_state.cleaner = AdvancedDataCleaner(raw)
        st.session_state.insights = AIInsightsEngine(raw).generate_all_insights()
        st.session_state.active_view = 'overview'
        st.rerun()


# ══════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════

cleaner = st.session_state.cleaner
view = st.session_state.active_view

def render_page_header(title: str, eyebrow: str = "DataForge"):
    now = datetime.now().strftime("%b %d, %Y · %H:%M")
    badge_cls = "badge-loaded" if cleaner else "badge-idle"
    badge_txt = "Data Loaded" if cleaner else "Awaiting Upload"
    st.markdown(f"""
    <div class="page-header">
        <div class="page-header-left">
            <div class="page-eyebrow">{eyebrow}</div>
            <div class="page-title">{title}</div>
        </div>
        <div class="page-header-right">
            <div class="header-badge {badge_cls}">{badge_txt}</div>
            <div class="header-time">{now}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════ WELCOME SCREEN ══════════════════════
if cleaner is None:
    render_page_header("Welcome")
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">
            <div class="hero-badge-dot"></div>
            Professional Edition · v2.0
        </div>
        <div class="hero-title">
            Intelligent Data<br><em>Analysis Suite</em>
        </div>
        <div class="hero-sub">
            Upload a CSV to unlock AI-powered insights, automated cleaning, interactive
            visualizations, and one-click machine learning — all in one workspace.
        </div>
        <div class="hero-upload-hint">
            ← <span>Upload your CSV file</span> using the sidebar to get started
        </div>
        <div class="feature-grid">
            <div class="feature-card">
                <span class="fc-emoji">🧹</span>
                <div class="fc-name">Smart Cleaning</div>
                <div class="fc-desc">Remove duplicates, impute missing values, normalize whitespace</div>
            </div>
            <div class="feature-card">
                <span class="fc-emoji">🔍</span>
                <div class="fc-name">Fuzzy Deduplication</div>
                <div class="fc-desc">Detect near-duplicate entries with string similarity matching</div>
            </div>
            <div class="feature-card">
                <span class="fc-emoji">📈</span>
                <div class="fc-name">Visualizations</div>
                <div class="fc-desc">Distributions, correlations, violin plots, scatter explorer</div>
            </div>
            <div class="feature-card">
                <span class="fc-emoji">🤖</span>
                <div class="fc-name">AutoML</div>
                <div class="fc-desc">One-click Random Forest for classification or regression</div>
            </div>
            <div class="feature-card">
                <span class="fc-emoji">🕵️</span>
                <div class="fc-name">Anomaly Detection</div>
                <div class="fc-desc">Isolation Forest for multivariate outlier discovery</div>
            </div>
            <div class="feature-card">
                <span class="fc-emoji">🧠</span>
                <div class="fc-name">AI Insights</div>
                <div class="fc-desc">Automated quality report with prioritized recommendations</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════ DATA LOADED ══════════════════════
else:
    orig    = cleaner.get_original_df()
    working = cleaner.get_cleaned_df() if st.session_state.data_cleaned else orig
    quality = calculate_quality_score(orig)

    # ─────────────── OVERVIEW ───────────────
    if view == 'overview':
        fname = uploaded_file.name if uploaded_file else "Dataset"
        render_page_header("Overview", fname)

        q_cls = "v-good" if quality >= 80 else ("v-warn" if quality >= 60 else "v-bad")
        missing_total = int(orig.isnull().sum().sum())
        dup_count     = int(orig.duplicated().sum())
        numeric_n     = len(orig.select_dtypes(include=[np.number]).columns)
        q_label = "Healthy" if quality >= 80 else ("Fair" if quality >= 60 else "Needs Work")

        st.markdown(f"""
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-accent-bar bar-blue"></div>
                <div class="kpi-header">
                    <div class="kpi-label">Quality Score</div>
                    <div class="kpi-icon">◎</div>
                </div>
                <div class="kpi-value {q_cls}">{quality:.0f}<span style="font-size:1rem;color:var(--text-tertiary);font-weight:500">/100</span></div>
                <div class="kpi-sub">▲ {q_label}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-accent-bar bar-green"></div>
                <div class="kpi-header">
                    <div class="kpi-label">Total Rows</div>
                    <div class="kpi-icon">≡</div>
                </div>
                <div class="kpi-value">{len(orig):,}</div>
                <div class="kpi-sub">{len(orig) - dup_count:,} unique rows</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-accent-bar bar-amber"></div>
                <div class="kpi-header">
                    <div class="kpi-label">Columns</div>
                    <div class="kpi-icon">⊞</div>
                </div>
                <div class="kpi-value">{orig.shape[1]}</div>
                <div class="kpi-sub">{numeric_n} numeric · {orig.shape[1] - numeric_n} categorical</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-accent-bar bar-rose"></div>
                <div class="kpi-header">
                    <div class="kpi-label">Missing Cells</div>
                    <div class="kpi-icon">⊘</div>
                </div>
                <div class="kpi-value {'v-good' if missing_total == 0 else 'v-bad'}">{missing_total:,}</div>
                <div class="kpi-sub">{missing_total / (len(orig) * orig.shape[1]) * 100:.1f}% of dataset</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Data preview card
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-title-wrap">
                    <div class="card-icon">🗂</div>
                    <div>
                        <div class="card-title">Data Preview</div>
                        <div class="card-subtitle">First 100 rows</div>
                    </div>
                </div>
                <div class="card-meta">Raw / Working</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="padding:16px">', unsafe_allow_html=True)
        st.dataframe(working.head(100), use_container_width=True, height=380)
        st.markdown('</div></div>', unsafe_allow_html=True)

        with st.expander("📋  Column Schema & Statistics"):
            col_info = pd.DataFrame({
                'Column': orig.columns,
                'Type': orig.dtypes.astype(str).values,
                'Non-Null': orig.count().values,
                'Null %': (orig.isnull().mean() * 100).round(1).values,
                'Unique': orig.nunique().values,
            })
            st.dataframe(col_info, use_container_width=True)

    # ─────────────── AI INSIGHTS ───────────────
    elif view == 'insights':
        render_page_header("AI Insights", "Quality Analysis")
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-title-wrap">
                    <div class="card-icon">🧠</div>
                    <div>
                        <div class="card-title">Automated Quality Report</div>
                        <div class="card-subtitle">AI-Generated · Real-time</div>
                    </div>
                </div>
                <div class="card-meta">AI-Generated</div>
            </div>
            <div class="card-body">
        """, unsafe_allow_html=True)
        display_insights(st.session_state.insights)
        st.markdown('</div></div>', unsafe_allow_html=True)

    # ─────────────── VISUALIZATIONS ───────────────
    elif view == 'visualize':
        render_page_header("Visualizations", "Data Exploration")
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-title-wrap">
                    <div class="card-icon">📈</div>
                    <div>
                        <div class="card-title">Interactive Charts</div>
                        <div class="card-subtitle">Plotly · Interactive</div>
                    </div>
                </div>
                <div class="card-meta">Plotly</div>
            </div>
            <div class="card-body">
        """, unsafe_allow_html=True)
        create_visualizations(working)
        st.markdown('</div></div>', unsafe_allow_html=True)

    # ─────────────── DATA CLEANING ───────────────
    elif view == 'clean':
        render_page_header("Data Cleaning", "Preprocessing Pipeline")

        c1, c2 = st.columns(2, gap="medium")

        with c1:
            st.markdown("""
            <div class="op-card">
                <div class="op-card-icon">🧹</div>
                <div class="op-card-title">Standard Clean</div>
                <div class="op-card-desc">
                    Removes exact duplicate rows, imputes missing numeric values with
                    median, fills categorical nulls with mode, and normalizes
                    whitespace in text columns.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="action-btn-wrap" style="margin-top:12px">', unsafe_allow_html=True)
            if st.button("🧹  Run Standard Clean", key="btn_clean_v", use_container_width=True):
                with st.spinner("Cleaning dataset…"):
                    report = cleaner.full_clean(handle_fuzzy=False)
                    st.session_state.data_cleaned = True
                removed = report.get('total_removed', 0)
                st.success(f"✓ Done — removed {removed:,} duplicate rows.")
            st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="op-card">
                <div class="op-card-icon">🔍</div>
                <div class="op-card-title">Fuzzy Deduplication</div>
                <div class="op-card-desc">
                    Detects near-duplicate text entries across categorical columns
                    using fuzzy string similarity matching with an 85% similarity
                    threshold.
                </div>
            </div>
            """, unsafe_allow_html=True)
            obj_cols = orig.select_dtypes(include='object').columns.tolist()
            st.markdown('<div class="action-btn-wrap" style="margin-top:12px">', unsafe_allow_html=True)
            if obj_cols:
                if st.button("🔍  Run Fuzzy Clean", key="btn_fuzzy_v", use_container_width=True):
                    with st.spinner("Running fuzzy matching…"):
                        report = cleaner.full_clean(handle_fuzzy=True, fuzzy_threshold=85,
                            columns_for_duplicates=obj_cols[:3])
                        st.session_state.data_cleaned = True
                    removed = report.get('total_removed', 0)
                    st.success(f"✓ Done — removed {removed:,} rows.")
            else:
                st.info("No text columns found for fuzzy matching.")
            st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.data_cleaned:
            cleaned = cleaner.get_cleaned_df()
            st.markdown('<div class="section-divider">Cleaned Dataset Preview</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <div class="card-title-wrap">
                        <div class="card-icon">✓</div>
                        <div>
                            <div class="card-title">Cleaned Dataset</div>
                            <div class="card-subtitle">Ready for analysis</div>
                        </div>
                    </div>
                    <div class="card-meta">Cleaned</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<div style="padding:16px">', unsafe_allow_html=True)
            st.dataframe(cleaned.head(100), use_container_width=True, height=340)
            st.markdown('</div></div>', unsafe_allow_html=True)

            col_dl1, col_dl2, col_dl3 = st.columns([1.5, 2, 1.5])
            with col_dl2:
                st.download_button(
                    label="⬇  Download Cleaned CSV",
                    data=cleaner.export_cleaned_csv(),
                    file_name=f"dataforge_cleaned_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                    mime="text/csv",
                    use_container_width=True,
                    key="dl_clean_page"
                )

    # ─────────────── ML MODELS ───────────────
    elif view == 'ml':
        render_page_header("Machine Learning", "AutoML · Random Forest")
        ml_df  = ensure_unique_columns(working)
        ml_mgr = MLModelManager(ml_df)

        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-title-wrap">
                    <div class="card-icon">🤖</div>
                    <div>
                        <div class="card-title">Model Training</div>
                        <div class="card-subtitle">Random Forest · AutoML</div>
                    </div>
                </div>
                <div class="card-meta">sklearn</div>
            </div>
            <div class="card-body">
        """, unsafe_allow_html=True)

        target = st.selectbox("Target column for prediction", ml_df.columns, key="ml_target")
        st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
        mc1, mc2 = st.columns(2, gap="large")

        with mc1:
            st.markdown("**Supervised Learning**")
            st.caption("Automatically selects classification or regression based on the target column.")
            st.markdown('<div class="action-btn-wrap">', unsafe_allow_html=True)
            if st.button("🚀  Train Model", key="btn_train", use_container_width=True):
                with st.spinner("Training Random Forest…"):
                    score, metrics, importance = ml_mgr.train_model(target)
                if score is None:
                    st.error("Not enough feature columns to train.")
                else:
                    label = "Accuracy" if 'accuracy' in metrics else "R² Score"
                    val   = metrics.get('accuracy', metrics.get('r2_score', 0))
                    col_a, col_b = st.columns(2)
                    col_a.metric(label, f"{val:.3f}")
                    if 'rmse' in metrics:
                        col_b.metric("RMSE", f"{metrics['rmse']:.4f}")
                    st.markdown('<div class="section-divider">Feature Importance</div>', unsafe_allow_html=True)
                    fig = px.bar(
                        importance.head(10),
                        x='importance', y='feature',
                        orientation='h',
                        color='importance',
                        color_continuous_scale=[[0,'#1d2740'],[0.5,'#6384ff'],[1,'#818cf8']],
                        text_auto='.3f',
                    )
                    fig.update_traces(textfont_size=9, marker_line_width=0)
                    fig.update_layout(
                        height=340, showlegend=False,
                        yaxis_title='', xaxis_title='Importance Score',
                        coloraxis_showscale=False,
                        **PLOTLY_LAYOUT
                    )
                    st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with mc2:
            st.markdown("**Anomaly Detection**")
            st.caption("Uses Isolation Forest to find multivariate outliers across all numeric features.")
            st.markdown('<div class="action-btn-wrap">', unsafe_allow_html=True)
            if st.button("🕵️  Detect Anomalies", key="btn_anomaly", use_container_width=True):
                with st.spinner("Running Isolation Forest…"):
                    anomalies = ml_mgr.detect_anomalies()
                if anomalies is None:
                    st.error("Need ≥ 2 numeric columns for anomaly detection.")
                elif len(anomalies) == 0:
                    st.success("✓ No anomalies detected.")
                else:
                    pct = len(anomalies) / len(ml_df) * 100
                    st.warning(f"**{len(anomalies)}** anomalous rows found ({pct:.1f}% of data)")
                    with st.expander(f"View {min(20, len(anomalies))} anomalous rows"):
                        st.dataframe(ml_df.iloc[anomalies[:20]], use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div></div>', unsafe_allow_html=True)

    # ─────────────── BEFORE / AFTER ───────────────
    elif view == 'compare':
        render_page_header("Before / After", "Data Comparison")

        if not st.session_state.data_cleaned:
            st.info("Run data cleaning first to unlock the before/after comparison view.")
        else:
            cleaned = cleaner.get_cleaned_df()
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <div class="card-title-wrap">
                        <div class="card-icon">🔄</div>
                        <div>
                            <div class="card-title">Dataset Comparison</div>
                            <div class="card-subtitle">Original vs Cleaned</div>
                        </div>
                    </div>
                    <div class="card-meta">Side-by-Side</div>
                </div>
                <div class="card-body">
            """, unsafe_allow_html=True)

            left, right = st.columns(2, gap="large")

            with left:
                st.markdown("""
                <div class="cmp-col-header">
                    <div class="cmp-indicator cmp-before"></div>
                    Original Dataset
                </div>
                """, unsafe_allow_html=True)
                a, b, c = st.columns(3)
                a.metric("Rows",  f"{len(orig):,}")
                b.metric("Nulls", f"{orig.isnull().sum().sum():,}")
                c.metric("Dupes", f"{orig.duplicated().sum():,}")
                st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
                st.dataframe(orig, use_container_width=True, height=380)

            with right:
                st.markdown("""
                <div class="cmp-col-header">
                    <div class="cmp-indicator cmp-after"></div>
                    Cleaned Dataset
                </div>
                """, unsafe_allow_html=True)
                a, b, c = st.columns(3)
                a.metric("Rows",  f"{len(cleaned):,}",
                    delta=f"{len(cleaned)-len(orig):,}")
                b.metric("Nulls", f"{cleaned.isnull().sum().sum():,}",
                    delta=f"{cleaned.isnull().sum().sum() - orig.isnull().sum().sum():,}")
                c.metric("Dupes", f"{cleaned.duplicated().sum():,}",
                    delta=f"{cleaned.duplicated().sum() - orig.duplicated().sum():,}")
                st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
                st.dataframe(cleaned, use_container_width=True, height=380)

            st.markdown('</div></div>', unsafe_allow_html=True)
            


# ── Footer ──
st.markdown("""
<style>
.app-footer {
    text-align: center;
    padding: 20px 10px;
    font-size: 14px;
    color: #888;
}

.app-footer .credit {
    margin-top: 6px;
    font-size: 13px;
    opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="app-footer">
    ◈ DataForge · Professional Data Analysis Suite · AI Insights · AutoML · Smart Cleaning
    <div class="credit">Built by Farheen ❤️</div>
</div>
""", unsafe_allow_html=True)