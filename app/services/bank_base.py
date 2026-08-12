class BankBase:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self):
        """Log in to the bank. Override in each bank's class."""
        raise NotImplementedError("Each bank must implement get_latest_statement()")

    def get_latest_statements(self):
        raise NotImplementedError("Each bank must implement get_latest_statement()")

    def download_statement(self, filename: str):
        raise NotImplementedError("Each bank must implement download_statement()")