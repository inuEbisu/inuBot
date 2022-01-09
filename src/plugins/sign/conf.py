from os import path

data_path_relative = 'assets/data.json'
data_path = path.abspath(path.join(path.dirname(__file__), data_path_relative))