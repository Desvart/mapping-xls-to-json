import os

import pandas as pd
import json
from jsonschema import validate, ValidationError

from src.Product import Product
from src.ProductId import ProductId
from src.config import read_config


def extract_raw_data_from_excel(file_path, products_sheet_name, cis_sheet_name, sonars_sheet_name):
    print('Starting raw data extraction...')
    products_dataframe = pd.read_excel(file_path, sheet_name=products_sheet_name)
    cis_dataframe = pd.read_excel(file_path, sheet_name=cis_sheet_name)
    sonars_dataframe = pd.read_excel(file_path, sheet_name=sonars_sheet_name)
    print('Raw data extraction finished.')
    return products_dataframe, cis_dataframe, sonars_dataframe

def build_product_objects_from_raw_data(products_df, cis_df, sonars_df, header_product):
    print('Starting product object building...')
    products = []
    for index, row in products_df.iterrows():
        product_id = ProductId(row[header_product])
        product = Product(product_id)
        product.import_cis(cis_df)
        product.import_sonars(sonars_df)
        products.append(product)
    print('Product object building finished.')
    return products

def generate_dto_from_objects(products):
    print('Start creating DTO from objects...')
    product_dto = []
    for product in products:
        product_dto.append(product.export())
    print('DTO created successfully.')
    return product_dto

def load_schema(schema_path):
    with open(schema_path, 'r') as file:
        json_schema = json.load(file)
        file.close()
        print('JSON schema loaded...')
        return json_schema

def validate_dto_against_schema(dto, schema_path):
    print('Checking DTO validity toward schema...')
    json_schema = load_schema(schema_path)
    try:
        validate(instance=dto, schema=json_schema)
        print('DTO validation successful!')
    except ValidationError as e:
        print("Validation error:", e.message)

def create_file_if_missing(file_path):
    if not os.path.isfile(file_path):
        print('JSON file is missing...')
        file = open(file_path, "x")
        file.close()
        print('JSON file created.')

def save_dto_to_json_file(file_path, dto):
    create_file_if_missing(file_path)

    with open(file_path, 'w') as file:
        json.dump(dto, file, indent=4)
        file.close()

    print('JSON file updated.')

def main():
    conf = read_config()
    products_df, cis_df, sonars_df = extract_raw_data_from_excel(conf['input_file_path'], conf['products_sheet_name'],
                                                              conf['cis_sheet_name'], conf['sonars_sheet_name'])
    products = build_product_objects_from_raw_data(products_df, cis_df, sonars_df, conf['header_product'])
    products_dto = generate_dto_from_objects(products)
    validate_dto_against_schema(products_dto, conf['schema_path'])
    save_dto_to_json_file(conf['json_output_path'], products_dto)

if __name__ == "__main__":
    main()
