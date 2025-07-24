from src import ProductId
from src.CiId import CiId
from src.SonarLink import SonarLink
from src.config import read_config


class Product:
    def __init__(self, product_id: ProductId):
        self.ea_code = product_id.ea_code
        self.trigram = product_id.trigram
        self.name = product_id.name
        self.cis = []
        self.sonars = []
        self.conf = read_config()

    @property
    def faulty_product_str(self):
        return f"{self.trigram} - {self.name} - {self.ea_code} [{self.ea_code}]"

    def select_data_related_to_trigram(self, dataframe):
        return dataframe[dataframe[self.conf['header_trigram']] == self.trigram]

    def import_cis(self, ci_ids):
        relevant_ci_ids = self.select_data_related_to_trigram(ci_ids)
        for index, row in relevant_ci_ids.iterrows():
            self.cis.append(CiId(row[self.conf['header_ci']], row[self.conf['header_trigram']]))

    def import_sonars(self, sonar_links):
        relevant_sonar_links = self.select_data_related_to_trigram(sonar_links)
        for index, row in relevant_sonar_links.iterrows():
            self.sonars.append(SonarLink(row[self.conf['header_sonar']], row[self.conf['header_git']], row[self.conf['header_trigram']]))

    def __str__(self):
        return f"{self.trigram} - {self.name} [{self.ea_code}] - {len(self.cis)} CI(s) - {len(self.sonars)} Sonar projects(s)"

    def export_cis(self):
        cis_exportable = []
        for ci in self.cis:
            cis_exportable.append(ci.export())
        return cis_exportable

    def export_sonar_links(self):
        sonar_links_exportable = []
        for sonar_link in self.sonars:
            sonar_links_exportable.append(sonar_link.export())
        return sonar_links_exportable

    def export(self):
        return {
            "ea_code": self.ea_code,
            "trigram": self.trigram,
            "product_name": self.name,
            "cis": self.export_cis(),
            "sonarqubes": self.export_sonar_links()
        }