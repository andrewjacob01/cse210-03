import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_player2_action import ControlPlayer2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    y = int(constants.MAX_Y/2)
    x = int(constants.MAX_X/2)

    # create the cast
    cast = Cast()

    position = Point(x,constants.CELL_SIZE*10)
    velocity = Point(constants.CELL_SIZE*1,0)
    player1 = Cycle(position,velocity)
    player1.set_color(constants.RED)
    cast.add_actor("player1", player1)
    
    position = Point(x,constants.CELL_SIZE*30)
    velocity = Point(-1 * constants.CELL_SIZE,0)
    player2 = Cycle(position,velocity)
    player2.set_color(constants.BLUE)
    cast.add_actor("player2", player2)
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlPlayer1Action(keyboard_service))
    script.add_action("input", ControlPlayer2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()