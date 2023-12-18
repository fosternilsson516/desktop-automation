from pynput import mouse, keyboard
import json

class ClickRecorder:
    def __init__(self):
        self.recorded_actions = []
        self.current_keys = ""
        self.recording_started = False

        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_scroll
        )
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key)

    def on_click(self, x, y, button, pressed):
        if pressed:
            if not self.recording_started:
                self.recording_started = True
            else:
                self.recorded_actions.append(("click", x, y))
                self.save_data()

    def on_scroll(self, x, y, dx, dy):
        if self.recording_started:
            self.recorded_actions.append(("scroll", x, y, dx, dy))
            self.save_data()

    def on_key(self, key):
        if self.recording_started:
            try:
                char = key.char
                self.current_keys += char
            except AttributeError:
                pass  # Handle special keys, if needed

    def save_data(self):
        if self.current_keys:
            self.recorded_actions.append(("keys", self.current_keys))
            self.current_keys = ""

    def start_recording(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def stop_recording(self):
        self.mouse_listener.stop()
        self.mouse_listener.join()
        self.keyboard_listener.stop()
        self.keyboard_listener.join()

if __name__ == "__main__":
    recorder = ClickRecorder()
    recorder.start_recording()

    try:
        input("Recording started. Press Enter to stop recording...")
    except KeyboardInterrupt:
        pass  # Allow stopping recording using KeyboardInterrupt (Ctrl+C)

    recorder.stop_recording()

    # Save recorded actions to a JSON file
    with open("recorded_actions.json", "w") as file:
        json.dump(recorder.recorded_actions, file)

    print("Recording saved.")
