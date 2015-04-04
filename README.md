##Adaptable R.P.S.


>Provides a robust game framework for hosting competitions of games akin to Rock Paper Scissors. In such games, players move simultaneously and the rules of the game decide who wins. This framework will be able to recover from network issues and support player ai.


###Supported Game Types

**Rock, Paper, Scissors**
	- Standard Rock, Paper, Scissors Rules
**Rock, Paper, Scissors, Lizard, Spock** (WIP)
**Prisoner's Dilemma** (WIP)
**Tic Tac Toe** (WIP)

###Supported Tournament Types

**All Play All**
	- Every player plays against every other player and the player with the most wins is champion.
**Single Elimination** (WIP)
	- Every player is pitted against one other and the winner moves on. An automatic win is given to the 'odd' player.
**Double Elimination** (WIP)
	- Every player is pitted against one other player and moves on unless they have accumulated 
**Round Robin** (WIP)
	- For large player counts(>16). Divides the players into groups and runs All Play All on the individual groups. Top 3 players move forward. 