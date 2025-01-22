from atproto import Client
import os, random, time

client = Client()
client.login(os.environ['USER_ACCOUNT'], os.environ["APP_PASSWORD"])

last_hour = 25

file_path = 'earthbound.txt'
if os.path.exists(file_path):
	with open(file_path, 'r') as file:
		earthbound_strings = file.read().split('\n')
else:
	print(f"Error: {file_path} does not exist.")
	earthbound_strings = []


while True:
	current_hour = int(time.strftime("%H"))
	if not current_hour == last_hour:
		random_string = random.choice(earthbound_strings)
		client.send_post(earthbound_strings[random.randint(0, len(earthbound_strings) - 1)])
		last_hour = current_hour
		time.sleep(60*60) # sleep for an hour
	time.sleep(600) # sleep for a minute