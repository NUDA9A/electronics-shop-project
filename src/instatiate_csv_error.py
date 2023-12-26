class InstatiateCSVError(Exception):
    def __init__(self, file, *args, **kwargs):
        self.message = f"InstantiateCSVError: Файл {file} поврежден"