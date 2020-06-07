class Player:
    def __init__(self,name:str,result:int):
        self.name=name
        self.result=result

    def get_count(self):
        return len(self.result)

    def get_score(self):
        return sum(self.result)


data = input()
players_DB = []

while not data == 'report':
    player_name = data.split(' -> ')[0]
    results = data.split(' -> ')[1].split(', ')

    player = Player(player_name, list(map(int, results)))
    players_DB.append(player)

    data = input()

report=input()
while not report=="end":
    sorted_players=[]
    if report=="score descending":
        sorted_players = sorted(players_DB, key=lambda x: (-x.get_score(), x.name))
        for player in sorted_players:
            print(f"{player.name}: {player.get_score()}")
    elif report=="score ascending":
        sorted_players = sorted(players_DB, key=lambda x: (x.get_score(), x.name))
        for player in sorted_players:
            print(f"{player.name}: {player.get_score()}")
    elif report=="numberOfGames descending":
        sorted_players = sorted(players_DB, key=lambda x: (-x.get_count(), x.name))
        for player in sorted_players:
            print(f"{player.name}: {player.get_count()}")
    elif report=="numberOfGames ascending":
        sorted_players = sorted(players_DB, key=lambda x: (x.get_count(), x.name))
        for player in sorted_players:
            print(f"{player.name}: {player.get_count()}")

    report = input()