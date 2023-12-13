from perform_actions import perform_actions

def re_run_actions_with_data_list(recorded_actions, data_list):
    for data_item in data_list:
        # Append data_item to recorded_actions or modify the actions as needed
        modified_actions = recorded_actions + [(data_item)]

        print(f"Running actions with data: {data_item}")
        perform_actions(modified_actions)

if __name__ == "__main__":
    with open("recorded_actions.json", "r") as file:
        recorded_actions = json.load(file)

    data_list = ["item1", "item2", "item3"]  # Replace with your list of data items

    re_run_actions_with_data_list(recorded_actions, data_list)
