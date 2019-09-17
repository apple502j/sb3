from abc import ABCMeta
from .excs import SB3ParsingError
from .gclass import _define
from .block import ScriptBuilder

Variable = _define("Variable")
List = _define("List")
Broadcast = _define("Broadcast")
Costume = _define("Costume")
Sound = _define("Sound")
Comment = _define("Comment")

class Target(metaclass=ABCMeta):
    def __init__(self, json):
        self.name = json.get("name")
        self._is_stage = json.get("isStage", False)
        self.costume_id = json.get("currentCostume")
        self.volume = json.get("volume")
        self.layer = json.get("layerOrder")
        self.block_info = ScriptBuilder(json.get("blocks", {}))
        self.variables = []
        for vid, l in json.get("variables", {}).items():
            self.variables.append(Variable(
                id=vid,
                name=l[0],
                value=l[1],
                cloud=(len(l) == 3)
            ))
        self.lists = []
        for vid, l in json.get("lists", {}).items():
            self.lists.append(List(
                id=vid,
                name=l[0],
                value=l[1]
            ))
        self.broadcasts = []
        for vid, l in json.get("broadcasts", {}).items():
            self.broadcasts.append(Broadcast(
                id=vid,
                name=l
            ))
        self.costumes = []
        for l in json.get("costumes", []):
            self.costumes.append(Costume(
                asset_id=l.get("assetId"),
                name=l.get("name"),
                filename=l.get("md5ext"),
                data_format=l.get("dataFormat"),
                center_x=l.get("rotationCenterX", 240),
                center_y=l.get("rotationCenterY", 180),
                resolution=l.get("bitmapResolution", None)
            ))
        self.sounds = []
        for l in json.get("sounds", []):
            self.sounds.append(Sound(
                asset_id=l.get("assetId"),
                name=l.get("name"),
                filename=l.get("md5ext"),
                data_format=l.get("dataFormat"),
                format=l.get("format", ""),
                rate=l.get("rate", 0),
                sample_count=l.get("sampleCount", 0)
            ))
        self.comments = []
        for key, l in json.get("comments", {}).items():
            self.comments.append(Comment(
                id=key,
                block=l.get("blockId", None),
                x=l.get("x"),
                y=l.get("y"),
                width=l.get("width"),
                height=l.get("height"),
                minimized=l.get("minimized"),
                text=l.get("text", ""),
                name=key
            ))

    def __repr__(self):
        return f"<{'Stage' if self._is_stage else 'Sprite'} {self.name}>"

class Stage(Target):
    def __init__(self, json):
        super().__init__(json)
        if not self._is_stage:
            raise SB3ParsingError("Sprite passed to Stage.__init__()")
        self.tempo = json.get("tempo", 0)
        self.video_transparency = json.get("videoTransparency", 0)
        self.video_state = json.get("videoState", "off")
        self.tts_language = json.get("textToSpeechLanguage", "")
        self.backdrops = self.costumes

class Sprite(Target):
    def __init__(self, json):
        super().__init__(json)
        if self._is_stage:
            raise SB3ParsingError("Stage passed to Sprite.__init__()")
        self.x = json.get("x", 0)
        self.y = json.get("y", 0)
        self.visible = json.get("visible", True)
        self.size = json.get("size", 100)
        self.direction = json.get("direction", 90)
        self.draggable = json.get("draggable", False)
        self.rotation = json.get("rotationStyle", "all around")

def target_factory(target_obj):
    try:
        return Sprite(target_obj)
    except SB3ParsingError:
        return Stage(target_obj)
