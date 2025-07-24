import configparser


def read_config():
    config_file_path = './config.ini'

    config = configparser.ConfigParser()
    config.read(config_file_path)

    return {
        'input_file_path': config.get('General', 'input_file_path'),
        'json_output_path': config.get('General', 'json_output_path'),
        'products_sheet_name': config.get('General', 'products_sheet_name'),
        'cis_sheet_name': config.get('General', 'cis_sheet_name'),
        'sonars_sheet_name': config.get('General', 'sonars_sheet_name'),
        'header_product': config.get('General', 'header_product'),
        'header_trigram': config.get('General', 'header_trigram'),
        'header_ci': config.get('General', 'header_ci'),
        'header_git': config.get('General', 'header_git'),
        'header_sonar': config.get('General', 'header_sonar'),
        'schema_path': config.get('General', 'schema_path')
    }