'''
This file and the contents have been taken from the
Churnometer walk through Project 2 and customized for
this project
'''
import streamlit as st


def page_project_hypothesis_body():

    st.success(
        "### Project Hypothesis and Validation\n\n"
        "I have found 4 hypothesis and their validation:\n\n"
        "**1. Hypothesis one.** \n"
        "* We consider the price of houses to be higher if the house has had "
        "a larger surface measured in sq. ft. \n"
        "* A correlation study can help in investigating if this is true.\n\n"
        "**2. Hypothesis Two.** \n"
        "* We consider that a houses with the same util surface measured "
        "in sq. ft., but built more recently has had a higher price than a "
        "older built house. \n"
        "* A correlation study can help in investigating if this is true.\n\n"
        "**3. Hypothesis Three.** \n"
        "* We consider the houses with the same util surface measured in "
        "sq. ft "
        "built in a recent year, but remodeled recently has had a higher "
        "price "
        "than a house built in the same year, but not recently refurbished.\n"
        "* A correlation study can help in investigating if this is true.\n\n"
        "**4. Hypothesis Four.** \n"
        "* We consider that a house with similar sq. ft., but with a higher "
        "quality of materials and condition scores might have had a "
        "higher sale price.\n"
        "* A correlation study can help in investigating if this is true."
    )
