#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[ ]:


# 1. Page Configuration
st.set_page_config(
    page_title="Titanic Data Analysis Dashboard",
    page_icon="🚢",
    layout="wide"
)


# In[4]:


# 2. Load Cleaned Dataset
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_titanic.csv')

df = load_data()


# In[5]:


# 3. Sidebar Filters
st.sidebar.header("Filter Options 🔍")

# Filter by Sex
selected_sex = st.sidebar.multiselect(
    "Select Gender:",
    options=df['Sex'].unique(),
    default=df['Sex'].unique()
)

# Filter by Pclass
selected_class = st.sidebar.multiselect(
    "Select Passenger Class:",
    options=sorted(df['Pclass'].unique()),
    default=sorted(df['Pclass'].unique())
)


# In[6]:


# Apply Filters
filtered_df = df[(df['Sex'].isin(selected_sex)) & (df['Pclass'].isin(selected_class))]


# In[7]:


# 4. Main Title
st.title("🚢 Titanic Survival Analysis Dashboard")
st.markdown("Interactive analysis built with **Python, Streamlit, and Plotly**.")


# In[8]:


# 5. Top KPIs Metrics
st.subheader("Key Performance Indicators (KPIs)")
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Passengers", len(filtered_df))
col2.metric("Total Survived", filtered_df['Survived'].sum())
col3.metric("Survival Rate", f"{filtered_df['Survived'].mean() * 100:.1f}%")
col4.metric("Avg Fare", f"${filtered_df['Fare'].mean():.2f}")
col5.metric("Avg Age", f"{filtered_df['Age'].mean():.1f} yrs")

st.divider()


# In[9]:


# 6. Interactive Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Survival Rate by Class & Sex")
    fig_class = px.histogram(
        filtered_df, 
        x="Pclass", 
        color="Survived", 
        barmode="group",
        labels={"Pclass": "Passenger Class", "count": "Passenger Count"},
        color_discrete_map={0: "#EF553B", 1: "#00CC96"}
    )
    st.plotly_chart(fig_class, use_container_width=True)

with col_right:
    st.subheader("Survival Rate by Age Group")
    fig_age = px.histogram(
        filtered_df, 
        x="AgeGroup", 
        color="Survived", 
        barmode="group",
        category_orders={"AgeGroup": ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']},
        color_discrete_map={0: "#EF553B", 1: "#00CC96"}
    )
    st.plotly_chart(fig_age, use_container_width=True)


# In[10]:


# 7. Additional Analysis Section
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("Family Status (Alone vs With Family)")
    fig_alone = px.histogram(
        filtered_df,
        x="IsAlone",
        color="Survived",
        barmode="group",
        labels={"IsAlone": "Is Alone (1=Yes, 0=No)"},
        color_discrete_map={0: "#EF553B", 1: "#00CC96"}
    )
    st.plotly_chart(fig_alone, use_container_width=True)

with col_right2:
    st.subheader("Fare Distribution by Class")
    fig_fare = px.box(
        filtered_df,
        x="Pclass",
        y="Fare",
        color="Pclass",
        points="all"
    )
    st.plotly_chart(fig_fare, use_container_width=True)


# In[11]:


# 8. Data Table
st.subheader("Cleaned Dataset View")
st.dataframe(filtered_df, use_container_width=True)

