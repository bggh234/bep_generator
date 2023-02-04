import json
from metadata import MetaData
from module import Module
from typing import Self


class Pack:
    def __init__(
            self,
            format_version: int,
            uuid: str,
            name: str                       = "untitled",
            version: tuple[int, int, int]   = (0, 1, 0),
            mcversion: tuple[int, int, int] = (1, 18, 0),
            discription: str                = "",
            metadata: MetaData              = MetaData()
        ) -> None:
        self.format_version                  = format_version
        self.uuid: str                       = uuid
        self.name: str                       = name
        self.version: tuple[int, int, int]   = version
        self.mcversion: tuple[int, int, int] = mcversion
        self.discription: str                = discription
        self.metadata: MetaData              = metadata
        self.modules: list[Module]           = []
        self.dependencies: list[Self]        = []


    @staticmethod
    def with_default_module(
            format_version: int,
            uuid: str,
            name: str                       = "untitled",
            version: tuple[int, int, int]   = (0, 1, 0),
            mcversion: tuple[int, int, int] = (1, 18, 0),
            discription: str                = ""
    ) -> None :
        pass
        
    
    def add_module(self, module: Module) -> None:
        self.modules.append(module)


    def add_dependency(self, dependency: Self) -> None:
        self.dependencies.append(dependency)

    
    def gen_manifest(self):
        modules = []
        for module in self.modules:
            modules.append({
            "uuid":        module.uuid,
            "type":        module.type,
            "version":     module.version,
            "discription": module.discription
            })

        dependencies = []
        for dependency in self.dependencies:
            dependencies.append({
            "uuid":    dependency.uuid,
            "version": dependency.version
            })

        return json.dumps({
            "header": {
                "format_version":     self.format_version,
                "uuid":               self.uuid,
                "name":               self.name,
                "version":            self.version,
                "min_engine_version": self.mcversion
            },
            "modules": modules,
            "dependencies": dependencies,
            "metadata": {
                "authors": self.metadata.authors,
                "licence": self.metadata.licence,
                "url": self.metadata.url
            }
        })
