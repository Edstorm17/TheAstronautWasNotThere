import re

class Colors:
    """To change the color dict to new values, the autorised modifications are \n
        - add (add a new value to a dict);
        - remove (remove a value on the dic with specific value);
        - pop (remove a value from the dict by is position id and not it's value);
        - new (add a new key (a color in hex) into the dict);
        - fetch ( return the values of the colors dict
        """
    global colors
    def __init__(self, mod: str = "", values: str | re | int = "", key: str = ""):
        self.mod: str = mod
        if type(values) == int:
            self.index: int = int(values)
        self.value: str| re | list[str] = values
        self.key: str = key
        match self.mod:
            case "add":
                Colors.c_add(self)
            case "remove":
                Colors.c_remove(self)
            case "pop":
                Colors.c_pop(self)
            case "new":
                Colors.c_new(self)
            case "fetch":
                Colors.fetch(self)

    def c_add(self):
        """add a new value to the color dict """
        if isinstance(self.value, list):
            colors[self.key].extend(self.value)
        else:
            colors[self.key].append(self.value)
        return colors

    def c_remove(self):
        """remove the value in a color dict of key x"""
        colors[self.key].remove(self.value)
        return colors

    def c_pop(self):
        """remove at index the value in the color dict """
        colors[self.key].pop(self.index)
        return colors

    def c_new(self):
        """add a new color to the dict """
        if not self.key in colors.keys():
            colors[self.key] = []
        return colors

    def fetch(self):
        """pull the current color dict"""
        return colors



colors = {
    "#00FFFF": [r'(-?\d+)'],
    "#FFA500": [],
    "#00FF00": [r'\b(up)\b',r"\b(down)\b",r"\b(left)\b",r"\b(right)\b"],
}
