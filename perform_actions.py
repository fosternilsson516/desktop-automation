import json
import time
import pyautogui

def perform_actions(actions):

    for action in actions:
        action_type, *args = action

        if action_type == "click":
            x, y = args
            pyautogui.click(x, y)

        elif action_type == "scroll":
            dx, dy = args
            pyautogui.scroll(dx)

        elif action_type == "keys":
            keys = args[0]
            pyautogui.write(keys)

        # Add additional conditions for other action types if needed

        time.sleep(1)  # Adjust the wait time between actions as needed

def re_run_actions_with_data_list(recorded_actions, data_list):
    for click_location in recorded_actions:
        if click_location[0] == "click":
            x, y = click_location[1:]
            print(f"Clicking at coordinates: ({x}, {y})")
            perform_actions([(click_location)] + data_list)

if __name__ == "__main__":
    with open("recorded_actions.json", "r") as file:
        recorded_actions = json.load(file)

    data_list = ["hello"]  # Replace with your list of data items

    re_run_actions_with_data_list(recorded_actions, data_list)
