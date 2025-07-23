import re


class FaultyProduct:
    def __init__(self, product_string_id):
        self.ea_code, self.product_name, self.trigram = self.extract_ea_code(product_string_id)

    def __str__(self):
        return self.trigram + " - " + self.product_name + " [" + self.ea_code + " ]"

    def extract_ea_code(self, product_string_id):
        regexp_pattern = r'^(\w{3})\s-\s([^-]+)\s-\s(\w+)\s\[\1\]$'
        match = re.match(regexp_pattern, product_string_id)

        if match:
            trigram = match.group(1)
            name = match.group(2).strip()
            unique_id = match.group(3)
            return trigram, name, unique_id
        else:
            raise ValueError("Input string does not match the expected format.")

