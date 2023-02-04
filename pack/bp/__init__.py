from pack.bp.bmodule import BModule
from pack import Pack


class BehaviorPack(Pack):
    def __init__(
            self,
            format_version: int,
            uuid: str,
            name: str                        = "untitled",
            version: tuple[int, int, int]    = (0, 1, 0),
            mcversion: tuple[int, int, int]  = (1, 18, 0),
            discription: str                 = ""
            ) -> None:
        super().__init__(format_version, uuid, name, version, mcversion, discription)


    @staticmethod
    def with_default_module(
            format_version: int,
            uuid: str,
            name: str                        = "untitled",
            version: tuple[int, int, int]   = (0, 1, 0),
            mcversion: tuple[int, int, int] = (1, 18, 0),
            discription: str                 = ""
            ) -> "BehaviorPack":
        obj = BehaviorPack(format_version, uuid, name, version, mcversion, discription)
        obj.modules.append(BModule(uuid, name, "data", version, discription))
        return obj