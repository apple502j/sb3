from .gclass import GenericData as G

class Monitor(object):
    def __init__(self, json):
        self.id = json.get("id")
        self.mode = json.get("mode")
        self.opcode = json.get("opcode")
        self.params = G(_repr="<MonitorParams>", **json.get("params", {}))
        self.sprite_name = json.get("spriteName", None)
        self.value = json.get("value")
        self.width = json.get("width", 0)
        self.height = json.get("height", 0)
        self.x = json.get("x", 0)
        self.y = json.get("y", 0)
        self.visible = json.get("visible", True)
        self.slider_min = json.get("sliderMin", 0)
        self.slider_max = json.get("sliderMax", 0)
        self.slider_integer = json.get("isDiscrete", True)

    def __repr__(self):
        return f"<Monitor {self.id}>"

    def __eq__(self, other):
        return self.id == other.id
