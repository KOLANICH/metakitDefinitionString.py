__all__ = ("parse",)

from pathlib import Path
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/prebuilder/pyMetakitDefinitionString , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

from UniGrammarRuntime.ParserBundle import ParserBundle

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent
bundleDir = thisDir / "parserBundle"

bundle = ParserBundle(bundleDir)

grammar = bundle.grammars["metakit4_definition_string"]
wrapper = grammar.getWrapper()  # put backend name, by default it selects the fastest one


parse = wrapper
