import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Data Visualizer', layout='centered', page_icon='📊')

st.title('📊 Data Visualizer')


uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
   
    df = pd.read_csv(uploaded_file)

    
    st.write("Preview of the dataset")
    st.write(df.head())

    
    st.write("Null Values in the Dataset")
    null_values = df.isnull().sum()
    st.write(null_values[null_values > 0])
    st.write(df.describe())

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("Dataset preview:")
        st.write(df.head())

    with col2:
        
        x_axis = st.selectbox('Select the X-axis', options=columns + ["None"])
        y_axis = st.selectbox('Select the Y-axis', options=columns + ["None"])

        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot', 'Pie Chart']
        
        plot_type = st.selectbox('Select the type of plot', options=plot_list)
        
        # Additional columns for Pie Chart
        if plot_type == 'Pie Chart':
            other_axes = st.multiselect('Select additional columns for Pie Chart', options=columns, default=[])

    # Generate the plot based on user selection
    if st.button('Generate Plot'):
        fig, ax = plt.subplots(figsize=(6, 4))

        if plot_type == 'Line Plot':
            if x_axis != 'None' and y_axis != 'None':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            else:
                st.error("Please select both X and Y axis for Line Plot")
        elif plot_type == 'Bar Chart':
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Scatter Plot':
            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Distribution Plot':
            sns.histplot(df[x_axis], kde=True, ax=ax)
            y_axis = 'Density'
        elif plot_type == 'Count Plot':
            sns.countplot(x=df[x_axis], ax=ax)
            y_axis = 'Count'
        

        
        ax.tick_params(axis='x', labelsize=10)  
        ax.tick_params(axis='y', labelsize=10)  

            
        plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        
        st.pyplot(fig)
else:
    st.write("Please upload a CSV file to get started.")
