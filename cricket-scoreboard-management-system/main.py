import random

class T20Cup:
    allTeam=[]
    def entry_team(self,teamObj) -> None:
        self.allTeam.append(teamObj)

class Team(T20Cup):
    def __init__(self,name) -> None:
        self.teamName=name
        self.teamListOfObj=[]
        super().entry_team(self)
    def entry_player(self,player):
        self.teamListOfObj.append(player)
    def __repr__(self) -> str:
        return f"TeamName:{self.teamName}"

class Player(Team):
    def __init__(self,name,teamObj) -> None:
        self.playerName=name
        self.strike_rate=0
        self.ball_used=0
        self.run_bat=0
        self.fours=0
        self.sixes=0
        self.run_ball=0
        self.wicket_taken=0
        self.balls_bowled=0
        teamObj.entry_player(self)

class Innings:
    def __init__(self,team1,team2,battingTeam,bowlingTeam) -> None:
        self.teamOneObj=team1
        self.teamTwoObj=team2
        self.battingTeam=battingTeam
        self.bowlingTeam=bowlingTeam
        self.totalRun=0
        self.totalWickets=0
        self.totalOver=0
        self.currentBall=0
        self.currentBattingList=[battingTeam.teamListOfObj[0],battingTeam.teamListOfObj[1]]
        self.striker=battingTeam.teamListOfObj[0]
        self.currentBowler=None
        self.currentOverStatus=[]
        self.allOverStatus=[]

cup=T20Cup()
bangladesh=Team('bangladesh')
india=Team('India')
tamim=Player('tamim',bangladesh)
sakib=Player('Shakib',bangladesh)
mustafiz=Player('Mustafizur Rahman',bangladesh)
kholi=Player('Virat Kohli',india)
rohit=Player('Rohit Sharma',india)
bumra=Player('jasprit Bhumra',india)
# for obj in india.teamListOfObj:
#     print(obj.playerName)


while True:
    print("Select teams to be played: ")
    for i,val in enumerate(cup.allTeam):
        print(f'{i+1}. {val.teamName}')
    teamOneIndex,teamTwoIndex=map(int,input("Enter two team indexes: ").split(" "))
    teamOneIndex-=1
    teamTwoIndex-=1
    teamOneObj=cup.allTeam[teamOneIndex]
    teamTwoObj=cup.allTeam[teamTwoIndex]
    tossWin=random.choice([teamOneIndex,teamTwoIndex])
    print(f'{cup.allTeam[tossWin].teamName} have won the toss')
    if tossWin==teamOneIndex:
        tossLoss = teamTwoIndex
    else:
        tossLoss = teamOneIndex
    rand = random.choice([0,1])
    if rand == 0:
        # winner team choose bowling
        print(f'{cup.allTeam[tossWin]} choose bowling')
        battingTeamObj = cup.allTeam[tossLoss]
        bowlingTeamObj = cup.allTeam[tossWin]
    else:
        # winner team choose batting
        print(f'{cup.allTeam[tossWin].teamName} choose batting')
        battingTeamObj = cup.allTeam[tossWin]
        bowlingTeamObj = cup.allTeam[tossLoss]
    print(battingTeamObj)
    print(bowlingTeamObj)
    break