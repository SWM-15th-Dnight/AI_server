from dotenv import dotenv_values

ENV = dotenv_values('./.env')

OPENAI_API_KEY = ENV['OPENAI_API_KEY']

