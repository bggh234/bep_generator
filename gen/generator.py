from pack import Pack


class Generator:
    def __init__(self, path: str, pack: Pack) -> None:
        self.path = path
        self.pack = pack


    def gen(self, pack: Pack) -> None:
        pass


    def gen_manifest(self) -> None:
        with open(f"{self.path}/manifest.json", "a") as file:
            file.write(self.pack.gen_manifest())
            file.close()