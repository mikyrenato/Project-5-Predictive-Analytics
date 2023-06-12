import streamlit as st

from src.file_management import load_housing_price_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():


    df = load_housing_price_data()


    corr_var_list = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### House Sale Price Study")
    st.info(
        "My friend is interested in discovering how the house attributes "
        "correlate with the sale price.\n"
        "Therefore, my friend expects data visualizations of the "
        "correlated variables against the sale price to show that."
    )


    if st.checkbox("Inspect House Price Data:"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            "the first 10 rows are displayed below.")

        st.write(df.head(10))

    st.write("---")


    st.success(
        "* Correlation studies were conducted, using the Pearson and "
        "Spearman methods "
        "to better understand how the variables correlate to the "
        "sale price.\n"
        "* The most correlated variable are: \n"
        "  * **1stFlrSF, GarageArea, GrLivArea, OverallQual, "
        "TotalBsmtSF, YearBuilt**"
    )


    st.info(
        "### The correlations and plots interpretation converge.\n"
        "The following are the variables isolated in the"
        " correlation study:\n"
        "* 1stFlrSF: First Floor square feet.\n"
        "* GarageArea: Size of garage in square feet.\n"
        "* GrLivArea: Above grade (ground) living area square feet.\n"
        "* OverallQual: Rates the overall quality of the material "
        "and finish of the house when constructed / refurbished.\n"
        "* TotalBsmtSF: Total square feet of basement area.\n"
        "* YearBuilt: Original construction date (1872 to 2010).\n\n"
        "The plots show that the variables isolated in the "
        " correlation study, do indeed have a strong correlation and "
        " possibly strong predictive power for Sale Price for these houses.\n"
    )


    df_eda = df.filter(corr_var_list + ['SalePrice'])


    if st.checkbox("Variable correlation to Sale Price"):
        variable_correlation_to_sale_price(df_eda, corr_var_list)


def variable_correlation_to_sale_price(df_eda, corr_var_list):

    target_var = 'SalePrice'
    for col in corr_var_list:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


def plot_numerical(df, col, target_var):


    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(col, fontsize=20)
    st.pyplot(fig)
