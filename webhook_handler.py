import pandas as pd

from flask import Flask, request, jsonify

BRAND_DATA = pd.read_csv('brand_data.csv')


def brand_data_dict():
    partner_data = {}
    for i in BRAND_DATA.index:
        current_col = {k: set(v.split(','))
                       for k, v in BRAND_DATA.loc[i].items()}
        partner_data[str(current_col['companyName'].pop())] = current_col
        del current_col['companyName']
    return partner_data
