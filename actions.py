import json
import time
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

def perform_actions(actions):
    mouse = MouseController()
    keyboard = KeyboardController()

    for action in actions:
        action_type, *args = action

        if action_type == "click":
            x, y = args
            mouse.position = (x, y)
            mouse.click()

        elif action_type == "scroll":
            dx, dy = args
            mouse.scroll(dx, dy)

        elif action_type == "keys":
            keys = args[0]
            keyboard.type(keys)

        # Add additional conditions for other action types if needed

        time.sleep(1)  # Adjust the wait time between actions as needed

if __name__ == "__main__":
    with open("recorded_actions.json", "r") as file:
        recorded_actions = json.load(file)

    perform_actions(recorded_actions)
