from steam.client import SteamClient
from steam.core.msg import MsgProto
from steam.enums.emsg import EMsg
from itertools import zip_longest
import time

def grouper(iterable, n): #https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time/5845141#5845141
	args = [iter(iterable)] * n
	return zip_longest(*args)

client = SteamClient()
client.cli_login()

def main():
	with open("run.txt", "r") as run:
		#todo: request_free_license
		for threetwo in grouper(run, 31): # get 31 appids
			clean = list(filter(None, threetwo))
			for game in clean:
				game = game.strip("\n")
				client.send(MsgProto(EMsg.ClientGamesPlayed), {'games_played': [{'game_id': game},]})
				print(game)
			#client.games_played(clean) #play
			#client.run_forever()
			break

main()