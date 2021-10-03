import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

csv_file = 'Number_of_CWD-positive_deer_identified_per_township__2015-2019_.csv'
df = pd.read_csv(csv_file)

data_clean = df

data_clean.replace('Uncoded & Errors', np.nan, inplace=True)
data_clean.replace('Unknown', np.nan, inplace=True)
data_clean.replace('U', np.nan, inplace=True)
data_clean.replace('None', np.nan, inplace=True)
data_clean.replace('<null>', np.nan, inplace=True)

st.title('Michigan CWD Dataset')
st.markdown("Taking the information we can gather from the CSV file. We can create a Streamlit app to look into our "
            "dataset, and visualize multiple plots. Showing how many tests were taken, how many were followed with "
            "positive results. What counties tested the most, and what counties had the most deer inflicted with CWD.")


st.sidebar.subheader('Explore Stats')
st.sidebar.markdown('Tick a box on the side panel to explore the dataset')
if st.sidebar.checkbox('Basic Info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look: ')
        st.write(data_clean.head())

    if st.sidebar.checkbox('Show raw data', False):
        st.subheader('Raw data')
        st.write(data_clean)

    if st.sidebar.checkbox('Show Columns'):
        st.subheader('Show columns list')
        all_columns = data_clean.columns.to_list()
        st.write(all_columns)

    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Description')
        st.write(data_clean.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.table(data_clean.isnull().sum())

st.sidebar.title('Creating Visualizations')
st.sidebar.subheader('Create and show visualizations.')
if st.sidebar.checkbox('Graphics'):
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If there's an error, adjust column name on side panel.")
        if st.checkbox('Plot the Count Plot'):
            column_count_plot = st.sidebar.selectbox('Choose a column to plot count.', data_clean.columns)
            hue_opt = st.sidebar.selectbox('Optional categorical variables (countplot hue)',
                                        data_clean.columns.insert(0, None))
            fig = sns.countplot(x=column_count_plot, data=data_clean, hue=hue_opt)
            fig.tick_params(axis='x', rotation=90)
            st.pyplot()

    if st.sidebar.checkbox('Histogram | Distplot'):
        st.subheader('Histogram | Distplot')
        st.info("If there's an error, adjust column name on side panel.")
        if st.checkbox('Dist plot'):
            column_dist_plot = st.sidebar.selectbox("Optional categorical variables (countplot hue)", data_clean.columns)
            fig = sns.displot(data_clean[column_dist_plot])
            st.pyplot()

    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If there's an error, adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column)", df.columns.insert(0, None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical)", data_clean.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)", data_clean.columns.insert(0, None))
        if st.checkbox('Plot Boxplot'):
            fig = sns.boxplot(x=column_box_plot_X,
                              y=column_box_plot_Y,
                              data=data_clean,
                              palette='Set3')
            fig.tick_params(axis='x', rotation=90)
            st.pyplot()