import zipfile
import json
from .project_json import json_check
from .excs import NotSB3Error

def open_sb3(filename, sprite=False):
    need = "project.json" if sprite else "project.json"
    with zipfile.ZipFile(filename) as sb3zip:
        names = sb3zip.namelist()
        if need not in names:
            raise NotSB3Error(
                "sprite3 must contain sprite.json"
                if sprite else
                "sb3 must contain project.json"
            )
        jsonfile = json.loads(sb3zip.read(need).decode("utf-8"))

        actual_names = (item for item in names if (
            item.count(".") == 1 and              # has one extension
            len(item.split(".")[0]) == 32 and     # has MD5 length
            item.split(".")[0].isalnum()        # has only alphabets and numbers
        )) # Maybe use regex?
        files = tuple(sb3zip.open(name) for name in actual_names)
    return json_check(jsonfile), files

open_sprite3 = lambda filename: open_sb3(filename, sprite=True)
