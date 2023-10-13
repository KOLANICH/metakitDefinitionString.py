pyMetakitDefinitionString [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=========================
~~[wheel (GHA via `nightly.link`)](https://nightly.link/prebuilder/pyMetakitDefinitionString/workflows/CI/master/pyMetakitDefinitionString-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/prebuilder/pyMetakitDefinitionString/workflows/CI/badge.svg)](https://github.com/prebuilder/pyMetakitDefinitionString/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/prebuilder/pyMetakitDefinitionString.svg)](https://libraries.io/github/prebuilder/pyMetakitDefinitionString)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/prebuilder/pyMetakitDefinitionString, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

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
