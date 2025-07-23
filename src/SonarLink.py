class SonarLink:
    def __init__(self, sonar_url, git_repo_base_url, associated_trigram):
        self.associated_trigram = associated_trigram
        self.git_repo_base_url = git_repo_base_url
        self.git_repo_full_url = ""
        self.sonar_url = sonar_url

    def __str__(self):
        return self.associated_trigram + " - " + self.sonar_url + " - " + self.git_repo_base_url