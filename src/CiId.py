import re


class CiId:
    def __init__(self, ci_string_id, associated_trigram):
        self.associated_trigram = associated_trigram
        self.name = ""
        self.id = ""
        self.parse_properties(ci_string_id)

    def __str__(self):
        return self.name + " [" + self.id + "]"

    def parse_properties(self, ci_string_id):
        regexp_pattern = r'^(.*)\s\[(.*)\]$'
        match = re.match(regexp_pattern, ci_string_id)

        if match:
            self.name = match.group(1)
            self.id = match.group(2)
        else:
            raise ValueError("Input string does not match the expected format.")

    @property
    def string_id(self):
        return self.name + " [" + self.id + "]"

    def export(self):
        return {
            "ci_name": self.name,
            "ci_id": self.id
        }
