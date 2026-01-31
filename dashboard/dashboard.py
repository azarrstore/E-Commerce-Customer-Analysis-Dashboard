import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="E-Commerce Dashboard (RFM & Retention)",
    layout="wide"
)

sns.set(style="whitegrid")

# =========================
# Load Data
# =========================
@st.cache_data
def load_data():
    rfm = pd.read_csv("dashboard/rfm_data.csv")
    rev = pd.read_csv("dashboard/revenue_by_segment.csv")
    retention = pd.read_csv("dashboard/retention.csv")
    return rfm, rev, retention

rfm, rev, retention = load_data()

# =========================
# Header
# =========================
st.title("📊 E-Commerce Customer Analysis Dashboard")
st.caption("Ringkasan analisis pelanggan menggunakan RFM dan Cohort Retention (non-ML).")

# =========================
# Sidebar Filters
# =========================
st.sidebar.header("Filter")

segments = sorted(rfm["segment"].dropna().unique().tolist())
selected_segments = st.sidebar.multiselect(
    "Pilih segmen pelanggan",
    options=segments,
    default=segments
)

min_score, max_score = int(rfm["RFM_score"].min()), int(rfm["RFM_score"].max())
score_range = st.sidebar.slider(
    "Rentang RFM Score",
    min_value=min_score,
    max_value=max_score,
    value=(min_score, max_score)
)

filtered_rfm = rfm[
    (rfm["segment"].isin(selected_segments)) &
    (rfm["RFM_score"].between(score_range[0], score_range[1]))
].copy()

# =========================
# KPI Row
# =========================
col1, col2, col3, col4 = st.columns(4)

total_customers = filtered_rfm["customer_unique_id"].nunique()
avg_recency = filtered_rfm["recency"].mean()
avg_frequency = filtered_rfm["frequency"].mean()
total_monetary = filtered_rfm["monetary"].sum()

col1.metric("Total Pelanggan (filtered)", f"{total_customers:,}")
col2.metric("Rata-rata Recency (hari)", f"{avg_recency:,.1f}")
col3.metric("Rata-rata Frequency", f"{avg_frequency:,.2f}")
col4.metric("Total Monetary (RFM)", f"{total_monetary:,.2f}")

st.divider()

# =========================
# Layout: Segment Distribution + Revenue Contribution
# =========================
left, right = st.columns(2)

with left:
    st.subheader("Distribusi Segmen Pelanggan")
    seg_counts = filtered_rfm["segment"].value_counts().reindex(segments, fill_value=0)

    fig = plt.figure()
    seg_counts.plot(kind="bar")
    plt.title("Jumlah Pelanggan per Segmen")
    plt.xlabel("Segmen")
    plt.ylabel("Jumlah Pelanggan")
    plt.xticks(rotation=0)
    st.pyplot(fig)

with right:
    st.subheader("Kontribusi Pendapatan per Segmen")
    # rev: columns biasanya ["segment","payment_value"] dari reset_index
    # Jika nama kolom beda, sesuaikan di bawah.
    seg_col = rev.columns[0]
    val_col = rev.columns[1]

    fig = plt.figure()
    plt.bar(rev[seg_col].astype(str), rev[val_col])
    plt.title("Total Pendapatan per Segmen")
    plt.xlabel("Segmen")
    plt.ylabel("Total Pendapatan")
    st.pyplot(fig)

st.divider()

# =========================
# RFM Scatter (Frequency vs Monetary) colored by segment
# =========================
st.subheader("Pola Perilaku Pelanggan (Frequency vs Monetary)")
fig = plt.figure()
sns.scatterplot(
    data=filtered_rfm,
    x="frequency",
    y="monetary",
    hue="segment",
    alpha=0.7
)
plt.title("Scatter: Frequency vs Monetary")
plt.xlabel("Frequency")
plt.ylabel("Monetary")
st.pyplot(fig)

st.divider()

# =========================
# Retention Heatmap
# =========================
st.subheader("Cohort Retention Heatmap")

# retention: baris cohort, kolom cohort_index (1,2,3,...)
# Format CSV bisa: kolom pertama "index" / "cohort_month", sisanya angka.
retention_df = retention.copy()

# Pastikan kolom pertama jadi index cohort
cohort_col = retention_df.columns[0]
retention_df[cohort_col] = retention_df[cohort_col].astype(str)
retention_df = retention_df.set_index(cohort_col)

# Ubah semua kolom ke numeric (kalau ada string)
for c in retention_df.columns:
    retention_df[c] = pd.to_numeric(retention_df[c], errors="coerce")

fig = plt.figure(figsize=(12, 6))
sns.heatmap(retention_df, annot=False)
plt.title("Retention Rate (Cohort Analysis)")
plt.xlabel("Bulan ke-")
plt.ylabel("Cohort")
st.pyplot(fig)

# =========================
# Table Preview
# =========================
st.subheader("Preview Data RFM (Filtered)")
st.dataframe(filtered_rfm.head(50), use_container_width=True)

st.caption("Catatan: Dashboard ini menampilkan hasil olahan analisis dari notebook.")
