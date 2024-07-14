import json

class ConfigProvider:
    """
    A utility class for loading configuration data from JSON files.
    """

    @staticmethod
    def load_config_json(file):
        """
        Load and parse a JSON configuration file.

        Args:
            file (str): The path to the JSON configuration file.

        Returns:
            dict: The parsed configuration data as a dictionary.

        Raises:
            FileNotFoundError: If the specified file is not found.
        """
        try:
            with open(file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"file {file} not found")
            raise