import pandas as pd

from src.CiId import CiId
from src.ProductId import ProductId
from src.SonarLink import SonarLink


def extract_data_from_excel(file_path):
    faulty_product_table = pd.read_excel(file_path, sheet_name='Sheet1')
    faulty_ci_table = pd.read_excel(file_path, sheet_name='Sheet2')
    git_sonar_table = pd.read_excel(file_path, sheet_name='Sheet3')
    return faulty_product_table, faulty_ci_table, git_sonar_table


def print_extracted_data(faulty_product_table, faulty_ci_table, git_sonar_table):
    print(faulty_product_table.head())
    print(faulty_ci_table.head())
    print(git_sonar_table.head())


def main():

    file_path = '../data/mapping.xlsx'
    header_product_str_id = "Product String Identifier"
    header_trigram = "Trigram"
    header_ci_str_id = "CI"
    header_git_repo = "Git Repo"
    header_sonar_url = "SonarQube URL"

    product_str_id_df, ci_str_id_df, git_sonar_df = extract_data_from_excel(file_path)
    print_extracted_data(product_str_id_df, ci_str_id_df, git_sonar_df)
    print(f" ")

    product_str_id1 = product_str_id_df[header_product_str_id].iloc[0]
    product_id1 = ProductId(product_str_id1)
    print(product_id1)
    print(product_id1.string_id)
    print(f" ")


    for index, row in ci_str_id_df.iterrows():
        print(f"{index}: {row[header_trigram]}, {row[header_ci_str_id]}")
        print(f" ")
        associated_trigram = row[header_trigram]
        ci_str_id = row[header_ci_str_id]
        ci_id1 = CiId(ci_str_id, associated_trigram)
        print(ci_id1)
        print(ci_id1.string_id)
        print(ci_id1.associated_trigram)

    for index, row in git_sonar_df.iterrows():
        sonar_link1 = SonarLink(row[header_sonar_url], row[header_git_repo], row[header_trigram])
        print(sonar_link1)




    # object_list = create_objects_from_data(faulty_product_df, faulty_ci_df, git_sonar_df)

    # json_file = generate_json_from_object(object_list)

    # validate_json_against_schema(json_file, json_schema)

    # save_json_file(json_file)


if __name__ == "__main__":
    main()