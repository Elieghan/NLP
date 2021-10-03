import requests
import os
from urllib.parse import urlparse

URL = 'http://localhost:8501'


def main():
    """
    Calls similarity.py
    Author:  Elie Ghanassia
    """
    cwd = os.getcwd()
    der = 'streamlit run ' + cwd + '/similarity.py'
    os.system(der)
    urlparse(URL)


if __name__ == '__main__':
    main()

