from actor import Actor, Animator
from settings import Settings

class _GameInterface:
    def __init__(self):
        self._actors = {}
        self._remove_queue = []
        self._director = None
    
    def add_actor(self, name, x):
        if name not in self._actors:
            actor = Actor(x, Settings.sprite_elevation)
            animator = Animator("test/director")
            animator.set_animation("idle")
            self._actors[name] = {
                "actor": actor,
                "animator": animator,
                "puppet": False
            }

    def run(self):
        if len(self._remove_queue) < 1:
            return
        # Don't delete from actors if this actor is currently being puppeted by the director
        if not self._actors[self._remove_queue[0]]["puppet"]:
            del self._actors[self._remove_queue.pop(0)]
    
    def get_actors(self):
        return self._actors
    
    def set_director(self, director):
        self._director = director
    
    def enqueue_delete_actor(self, actor):
        self._remove_queue.append(actor)

    def enqueue_command(self, command):
        if self._director:
            self._director.enqueue_command(command)

GameInterface = _GameInterface()