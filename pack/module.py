class Module:
    def __init__(
            self,
            uuid: str,
            name: str                     = "untitled",
            module_type: str              = "data",
            version: tuple[int, int, int] = (0, 1, 0),
            discription: str              = ""
        ) -> None:
        self.uuid: str                     = uuid
        self.type: str                     = module_type
        self.name: str                     = name
        self.version: tuple[int, int, int] = version
        self.discription: str              = discription