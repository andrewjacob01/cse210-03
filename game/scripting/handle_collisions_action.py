import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the players collides
    with the food, or the players collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._message = Actor()
        self._x = int(constants.MAX_X / 2)
        self._y = int(constants.MAX_Y / 2)
        self._position = Point(self._x, self._y)

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the players collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        cycle1 = player1.get_segments()[0]
        cycle2 = player2.get_segments()[0]
        segments1 = player1.get_segments()[1:]
        segments2 = player2.get_segments()[1:]
        
        #game over for player1
        for segment1 in segments1:
            if cycle1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._message.set_text("Blue Won!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)

        for segment1 in segments2:
            if cycle1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._message.set_text("Blue Won!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)

        #game over for player2
        for segment2 in segments2:
            if cycle2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._message.set_text("Red Won!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)

        for segment2 in segments1:
            if cycle2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._message.set_text("Red Won!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the players white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1")
            player2 = cast.get_first_actor("player2")
            segments1 = player1.get_segments()
            segments2 = player2.get_segments()

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
            
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)