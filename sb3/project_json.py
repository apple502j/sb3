from .sprite import target_factory
from .monitor import Monitor
from .gclass import GenericData as G

class ProjectJSON(object):
    def __init__(self, json):
        self.targets = [target_factory(target) for target in json.get("targets", [])]
        self.monitors = [Monitor(obj) for obj in json.get("monitors", [])]
        self.extensions = json.get("extensions", [])
        self.meta = G(
            _repr="<Meta>",
            semantic_ver=json["meta"]["semver"],
            vm_ver=json["meta"]["vm"],
            user_agent=json["meta"]["agent"]
        )

    def __repr__(self):
        return "<ProjectJSON>"

def json_check(json):
    if json.get("targets", None):
        return ProjectJSON(json)
    return target_factory(json)
