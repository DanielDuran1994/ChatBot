import os

class Config(object):
	SECRET_KEY = 'my_secret_token'
	PAGE_ACCESS_TOKEN = 'EAAXpwZB7CwMEBALkKthiqzXLYxXgY5lCIKSqMznKU9N2WVxUTHeksOKwg7Cg37BldVMc5ZA96ZCoNyOZBByn4F3QCgIIfEWJLZAoomqFUweRxQmqWtXfRb7RZA44EM0X37I3ZBCg6yUbVCQUaZCXseW2UMZA2tZA2J1FmjuQfAvIAZBjQZDZD'

class DevelopmentConfig(Config):
	DEBUG = True