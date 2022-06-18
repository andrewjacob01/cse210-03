from game.scripting.action import Action

class MoveActorsAction(Action):

    def execute(self, cast, script):
        """ Overrides execute() of Action

        Iterates through the cast of actors and
        calls their move_next() method
  

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.

            # 1) get all the actors from the cast
            # 2) loop through the actors
            # 3) call the move_next() method on each actor
        """
        ensemble = cast.get_all_actors()

        for actor in ensemble:
            actor.move_next()
