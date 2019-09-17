from json import loads as json_loads
from .gclass import GenericData as G
from .gclass import _define

BlockDefinitation = _define("BlockDefinitation")

class Block(G):
    menu = None
    block = None
    number = 0
    color = ""
    text = ""
    broadcast_id = ""
    broadcast_name = ""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._iter_num = 0

    def __repr__(self):
        return f"<Block {self.id}>"
    def __iter__(self):

        return self
    def __next__(self):
        o = self
        for i in range(self._iter_num):
            if getattr(o, "next", None):
                o = o.next
            else:
                self._iter_num += 1
                raise StopIteration
        self._iter_num += 1
        return o
    def __eq__(self, other):
        return self.id == other.id


    @property
    def isolated(self):
        return getattr(self, "first_block", False) and not getattr(self, "next", None)

    @property
    def proc_define(self):
        if self._mutation:
            return BlockDefinitation(
                name=self.id,
                code=self._mutation["proccode"],
                arg_ids=json_loads(self._mutation["argumentids"]),
                arg_names=json_loads(self._mutation["argumentnames"]),
                arg_defaults=json_loads(self._mutation["argumentdefaults"]),
                without_refresh=self._mutation.get("warp", False)
            )
        return None

    @property
    def selectables(self):
        return self.inputs + self.fields


Input = _define("Input")
Field = _define("Field")

def arg_type(enum):
    return {
        1: "menu",
        2: "block",
        3: "note",
        8: "direction",
        9: "color",
        10: "text",
        11: "broadcast",
        12: "variable",
        13: "list"
    }.get(enum, "number")


class ScriptBuilder(object):
    def __init__(self, d):
        self.dict = d

    def __repr__(self):
        return "<ScriptBuilder>"

    def blocks(self):
        block_list = []
        for block_id in self.dict.keys():
            block = self.get_block(block_id)
            if "_menu" in block.opcode or block.opcode.endswith("menu"):
                continue
            block_list.append(block)
        return block_list

    def scripts(self):
        first_blocks = (block for block in self.blocks() if block.first_block)
        return [tuple(block) for block in first_blocks]

    def get_block(self, id, is_field=False, solve_before=True, solve_next=True, # pylint: disable=unused-argument
                  solve_field=True, solve_input=True):
        try:
            block = self.dict[id]
        except KeyError:
            return None
        return Block(
            id=id,
            opcode=block["opcode"],
            inputs=self.get_inputs(block) if solve_input else [],
            fields=self.get_fields(block) if solve_field else [],
            next=(block.get("next", None) and
                  solve_next and
                  self.get_block(block["next"], solve_before=False)),
            before=(block.get("parent", None) and
                    solve_before and
                    self.get_block(block["parent"], solve_next=False)),
            first_block=block.get("topLevel", False),
            shadow=block.get("shadow", None),
            x=block.get("x", 0),
            y=block.get("y", 0),
            _mutation=block.get("mutation", {}),
            _dict=block
        )

    def get_inputs(self, block):
        inputs = []
        for input_name, val in block["inputs"].items():
            atype = arg_type(val[-1][0] if isinstance(val[-1], list) else val[0])
            if len(val) == 3:
                block_inside = val[1]
            else:
                block_inside = None
            input = Input(name=input_name, type=atype, block_inside=block_inside)
            if atype == "menu":
                input.__dict__.update(
                    menu=self.get_fields(self.dict[val[-1]])[0]
                )
            elif atype == "block":
                input.__dict__.update(
                    block=self.get_block(val[-1],
                                         solve_input=False,
                                         solve_next=False,
                                         solve_before=False,
                                         solve_field=False)
                )
            elif atype == "text":
                input.__dict__.update(
                    text=val[-1][-1]
                )
            elif atype == "broadcast":
                input.__dict__.update(
                    broadcast_id=val[-1][-1],
                    broadcast_name=val[-1][-2]
                )
            elif atype in ("number", "direction"):
                input.__dict__.update(
                    number=int(val[-1][-1])
                )
            elif atype == "color":
                input.__dict__.update(
                    color=val[-1][-1]
                )

            inputs.append(input)
        return inputs

    def get_fields(self, block): # pylint: disable=no-self-use
        fields = []
        for fieldname, (value, extra) in block.get("fields", {}).items():
            fields.append(Field(
                name=fieldname,
                value=value,
                extra=extra
            ))
        return fields
