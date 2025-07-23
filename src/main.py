import pandas as pd


def extract_data_from_excel(file_path):
    faulty_product_table = pd.read_excel(file_path, sheet_name='Sheet1', index_col=0)
    faulty_ci_table = pd.read_excel(file_path, sheet_name='Sheet2', index_col=0)
    git_sonar_table = pd.read_excel(file_path, sheet_name='Sheet3', index_col=0)
    return faulty_product_table, faulty_ci_table, git_sonar_table


def print_extracted_data(faulty_product_table, faulty_ci_table, git_sonar_table):
    print(faulty_product_table.head())
    print(faulty_ci_table.head())
    print(git_sonar_table.head())


def main():

    file_path = '../data/mapping.xlsx'

    faulty_product_df, faulty_ci_df, git_sonar_df = extract_data_from_excel(file_path)
    print_extracted_data(faulty_product_df, faulty_ci_df, git_sonar_df)

    # object_list = create_objects_from_data(faulty_product_df, faulty_ci_df, git_sonar_df)

    # json_file = generate_json_from_object(object_list)

    # validate_json_against_schema(json_file, json_schema)

    # save_json_file(json_file)


if __name__ == "__main__":
    main()