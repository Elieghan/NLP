import pandas as pd
import numpy as np
import difflib
import streamlit as st
import re
import Levenshtein

DATA = "data_method.csv"


def similar(name):
    """
    Finds similar methods given an input method.
    :param name: name of the methode
    :return: similar methodes
    Author:  Elie Ghanassia
    """
    try:
        name = str(name)
    except:
        print("The name of the method can't be converted into string")

    df = pd.read_csv(DATA)
    res = difflib.get_close_matches(name, df['name'])
    result1 = [df[df['name'] == i].reset_index().iloc[0]['method'] for i in res]

    simi = []
    for i, v in df['method'].iteritems():
        sim = Levenshtein.ratio(name, v)
        simi.append(sim)
    ind = np.argmax(simi)
    res = df.iloc[ind]['method']
    result2 = [res]
    result = [result1, result2]

    return result


def transf(name):
    try:
        name = str(name)
    except:
        print("The name of the method can't be converted into string")

    name = name.replace('(', ' ').replace(')', ' ').replace(',', ' ')
    name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)

    return name


def main():
    """
    Calls similar function.
    Author:  Elie Ghanassia
    """
    st.set_page_config(page_title='Method Test Classifier', layout='wide', initial_sidebar_state='auto')
    st.sidebar.title('-- Method Classifier --')
    st.sidebar.write("Write the name of your method")
    st.sidebar.write("------------------------------")
    st.sidebar.write("Two methods will be used for this task:")
    st.sidebar.write("-> The first one is difflib")
    st.sidebar.write("-> The second one is Levenshtein")
    user_input = st.text_input("Name")
    user_input = transf(user_input)
    if st.button('Submit'):
        res = similar(user_input)
        st.write('Similar method with difflib:', res[0])
        st.write('Similar method with Levenshtein:', res[1])


if __name__ == '__main__':
    main()

