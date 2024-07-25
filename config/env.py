from dotenv import dotenv_values

ENV = dotenv_values('./.env')


OPENAI_API_KEY = ENV['OPENAI_API_KEY']

DB_HOST = ENV["DB_HOST"]
DB_USER = ENV["DB_USER"]
DB_PASSWORD = ENV["DB_PASSWORD"]
DB_PORT = ENV["DB_PORT"]
DB_TABLE = ENV["DB_TABLE"]