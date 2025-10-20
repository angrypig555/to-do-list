from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Input

class application(App):
    KEYBINDS = [("q", "quit", "Quit the app")]
    CSS_PATH = "main.tcss"
    TITLE = "To-Do List"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Enter a new to-do item:", id="label")
        yield Input(placeholder="New to-do item...", id="todo_input")
        yield Button("Add Item", id="add_button")
        yield Static("Your To-Do List:", id="list_label")
        yield Static("", id="todo_list")
        yield Static("To-Do List V0.1, press Q to exit.", id="footer")
        yield Footer()


if __name__ == "__main__":
    app = application()
    app.run()