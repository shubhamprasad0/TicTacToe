class Player:
    ''' This class defines the properties of a player of the game '''

    def __init__(self, name='player', marker='x'):
        ''' This is a constructor to initialize a player object.

        Arguments:

        name -- name of the player (default 'player')
        marker -- marker ('x' or 'o') to identify the player (default 'x')

        '''

        self.name = name
        self.moves = []
        self.marker = marker
