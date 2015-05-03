__author__ = "Paul Council, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Joe Kvedaras, Collin Day"]


class Registration:
    """
    purpose of this file is to register a player in a tournament

    Attributes:
        tournament: the tournament to register players to
    """

    def __init__(self, tournament):
        """
        Initialize Registration with a Tournament
        :param tournament: the tournament for registration
        :type tournament: TournamentService.TournamentService
        """
        self.tournament = tournament

    def register(self, player):
        """
        Register a player in the tournament
        :param player: the player to register to the current tournament
        :type player: Player.Player
        """
        self.tournament.register_player(player)
