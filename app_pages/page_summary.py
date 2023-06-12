import streamlit as st


def page_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        "**Project Dataset**\n"
        "* The dataset is sourced from [Kaggle]"
        "(https://www.kaggle.com/codeinstitute/housing-prices-data) "
        "being provided by Code Institute.\n"
        "* The dataset hosts 1.460 rows and represents housing "
        "records from Ames, Iowa. \n"
        "* The dataset typically contains a house profile, "
        "i.e., Floor Area, Basement, Garage, Kitchen, Lot, Porch, "
        "Wood Deck, Year Built "
        "and the respective sale price, for houses built between "
        "1872 and 2010.\n\n"
        "**SalePrice** represents the price a house was sold for and "
        "is our target variable.\n\n"
        "**Ames, Iowa**\n"
        "* Ames has a robust, stable economy, and a flourishing cultural "
        "environment with a population\n "
        "of 89,540 people. \n\n"
    )

    # "Business Requirements" section
    st.success(
        "The project has 2 business requirements:\n"
        "* 1 - My friend is interested in discovering how exactly house "
        "attributes correlate with the sale price.\n"
        "  * My friend expects data visualizations of the correlated "
        "variables against the sale price.\n"
        "* 2 - My friend is interested in predicting the house sales price "
        "for his refurbished houses, "
        "and any other house in Ames, Iowa, that he will consider to "
        "buy or sell in the future."
    )

    # Link to README file, so the users can have access to
    # full project documentation
    st.warning(
        "For additional information, please visit and **read** the "
        "[Project README file.]"
        "(https://github.com/mikyrenato/Project-5-Predictive-Analytics)"
    )

    st.info(
        "**Dataset Content Guidelines**\n\n"
        "|Variable|Meaning|Units|\n"
        "|:----|:----|:----|\n"
        "|1stFlrSF|First Floor square feet|(Min - Max > Sq. ft.) "
        "334 - 4692|\n"
        "|2ndFlrSF|Second floor square feet|(Min - Max > Sq. ft.) "
        "0 - 2065|\n"
        "|BedroomAbvGr|Bedrooms above grade (does NOT include "
        "basement bedrooms)|(Min - Max > Bedrooms) 0 - 8|\n"
        "|BsmtExposure|Refers to walkout or garden level walls|Gd: "
        "Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; "
        "No: No Exposure; None: No Basement|\n"
        "|BsmtFinType1|Rating of basement finished area|GLQ: Good "
        "Living Quarters; ALQ: Average Living Quarters; BLQ: Below "
        "Average Living Quarters; Rec: Average Rec Room; LwQ: Low "
        "Quality; Unf: Unfinished; None: No Basement|\n"
        "|BsmtFinSF1|Type 1 finished square feet|(Min - Max > Sq. ft.) "
        "0 - 5644|\n"
        "|BsmtUnfSF|Unfinished square feet of basement area|(Min - "
        "Max > Sq. ft.) 0 - 2336|\n"
        "|TotalBsmtSF|Total square feet of basement area|(Min - "
        "Max > Sq. ft.) 0 - 6110|\n"
        "|GarageArea|Size of garage in square feet|(Min - Max > "
        "Sq. ft.) 0 - 1418|\n"
        "|GarageFinish|Interior finish of the garage|Fin: Finished; "
        "RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        "|GarageYrBlt|Year garage was built|(Min - Max > Year) "
        "1900 - 2010|\n"
        "|GrLivArea|Above grade (ground) living area square feet|"
        "(Min - Max > Sq. ft.) 334 - 5642|\n"
        "|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: "
        "Typical/Average; Fa: Fair; Po: Poor|\n"
        "|LotArea| Lot size in square feet|(Min - Max > Sq. ft.) "
        "1300 - 215245|\n"
        "|LotFrontage| Linear feet of street connected to property|"
        "(Min - Max > Lin. ft.) 21 - 313|\n"
        "|MasVnrArea|Masonry veneer area in square feet|(Min - Max "
        "> Sq. ft.) 0 - 1600|\n"
        "|EnclosedPorch|Enclosed porch area in square feet|"
        "(Min - Max > Sq. ft.) 0 - 286|\n"
        "|OpenPorchSF|Open porch area in square feet|(Min - "
        "Max > Sq. ft.) 0 - 547|\n"
        "|OverallCond|Rates the overall condition of the house|"
        "10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; "
        "6: Above Average; 5: Average; 4: Below Average; 3: Fair; "
        "2: Poor; 1: Very Poor|\n"
        "|OverallQual|Rates the overall material and finish of the "
        "house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: "
        "Good; 6: Above Average; 5: Average; 4: Below Average; 3: "
        "Fair; 2: Poor; 1: Very Poor|\n"
        "|WoodDeckSF|Wood deck area in square feet|(Min - Max > "
        "Sq. ft.) 0 - 736|\n"
        "|YearBuilt|Original construction date|(Min - Max > Year) "
        "1872 - 2010|\n"
        "|YearRemodAdd|Remodel date (same as construction date "
        "if no remodeling or additions)|(Min - Max > Year) 1950 - 2010|\n"
        "|SalePrice|Sale Price|(Min - Max > Price in $) 34900 - 755000|\n"
    )


def main():
    st.set_page_config(page_title="Project Summary", layout="wide")
    page_summary_body()


if __name__ == "__main__":
    main()
