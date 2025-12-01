from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def draw(self):
        pass


class SimpleWindow(Window):
    def draw(self):
        print("Drawing a simple window")


class WindowDecorator(Window):
    def __init__(self, window: Window):
        self._window = window

    def draw(self):
        self._window.draw()


class BorderDecorator(WindowDecorator):
    def draw(self):
        super().draw()
        self._add_border()

    def _add_border(self):
        print("Adding a border")


class ScrollbarDecorator(WindowDecorator):
    def draw(self):
        super().draw()
        self._add_scrollbar()

    def _add_scrollbar(self):
        print("Adding scrollbars")


if __name__ == "__main__":
    simple = SimpleWindow()
    print("Simple window:")
    simple.draw()

    print("\nWindow with scrollbars:")
    window_with_scrollbars = ScrollbarDecorator(simple)
    window_with_scrollbars.draw()

    print("\nWindow with border and scrollbars:")
    fancy_window = BorderDecorator(ScrollbarDecorator(simple))
    fancy_window.draw()
