pyMetakitDefinitionString [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=========================
~~[wheel (GHA via `nightly.link`)](https://nightly.link/prebuilder/pyMetakitDefinitionString/workflows/CI/master/pyMetakitDefinitionString-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/prebuilder/pyMetakitDefinitionString/workflows/CI/badge.svg)](https://github.com/prebuilder/pyMetakitDefinitionString/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/prebuilder/pyMetakitDefinitionString.svg)](https://libraries.io/github/prebuilder/pyMetakitDefinitionString)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Parses metakit definition string.

Usage
-----

```python
import pyMetakitDefinitionString

d = pyMetakitDefinitionString.parse("people[first:S,last:S,shoesize:I],text[line:S]")
print(d)
```

```
[
	view<name='people', bodyF=[scalar<name='first', typeF='S'>, scalar<name='last', typeF='S'>, scalar<name='shoesize', typeF='I'>]>,
	view<name='text', bodyF=[scalar<name='line', typeF='S'>]>
]
```

Interpretation of `typeF` is up to you since adding a enum will not spare you from having a look-up table. [See the docs.](https://codeberg.org/prebuilder/metakit/blob/master/doc/format.html#L155-L161)


Requirements
------------
* [UniGrammarRuntime](https://codeberg.org/UniGrammar/UniGrammarRuntime.py)
* Any of the backends for which parsers have been generated. [`parsimonious`](https://github.com/erikrose/parsimonious) is recommended, as it was benchmarked as the fastest one.
