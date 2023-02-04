class MetaData:
    def __init__(
            self,
            authors: list[str] = ["Unknown"],
            licence: str = "None",
            url: str = "None"
        ) -> None:
        self.authors: list[str] = authors
        self.licence: str       = licence
        self.url: str           = url
