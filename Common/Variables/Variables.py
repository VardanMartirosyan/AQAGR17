class ProjectVariables():
    productName = "AGV Helmet"
    productName2 = "Yamaha R6"
    mainURL = "https://www.google.com"

    def get_project_root(self):
        from pathlib import Path
        return str(Path(__file__).parent.parent.parent)
