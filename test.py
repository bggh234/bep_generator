import sys
sys.path.append("./pack")

from pack.bp import BehaviorPack
from gen.generator import Generator
p = BehaviorPack.with_default_module(2, "123412341234", "ABC")

Generator(".", p).gen_manifest()