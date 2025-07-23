import re


class ProductId:
    def __init__(self, product_string_id):
        self.ea_code = ""
        self.name = ""
        self.trigram = ""
        self.parse_properties(product_string_id)


    def __str__(self):
        return self.trigram + " - " + self.name + " [" + self.ea_code + "]"

    def parse_properties(self, product_string_id):
        regexp_pattern = r'^(\w{3})\s-\s(.*)\s-\s(EA\d+)\s\[.*\]$'
        match = re.match(regexp_pattern, product_string_id)

        if match:
            self.trigram = match.group(1)
            self.name = match.group(2)
            self.ea_code = match.group(3)
        else:
            raise ValueError("Input string does not match the expected format.")

    @property
    def string_id(self):
        return self.trigram + " - " + self.name + " [" + self.ea_code + "]"
