import unittest
from launch_console import move_player, describe_room


class TestQuestForge(unittest.TestCase):

    def test_player_can_move_north(self):
        location, message = move_player("village", "north")
        self.assertEqual(location, "forest")
        self.assertIn("forest", message.lower())

    def test_player_cannot_move_in_invalid_direction(self):
        location, message = move_player("village", "west")
        self.assertEqual(location, "village")
        self.assertEqual(message, "You cannot go that way.")

    def test_cave_is_reachable(self):
        location, _ = move_player("forest", "east")
        self.assertEqual(location, "cave")

