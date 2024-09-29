import main
class System:
    coordinate_origin = (main.performance.window_height() / 2) * -1
    def get_ready(self):
        global coordinate_origin
        self.goto(-180, coordinate_origin + 50)
        coordinate_origin += 50