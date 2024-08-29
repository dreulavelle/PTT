# Changelog

## [1.2.3](https://github.com/dreulavelle/PTT/compare/v1.2.2...v1.2.3) (2024-08-29)


### Bug Fixes

* spanish titles with seasons werent parsing as seasons. added spanish lang infer as well for this. ([f890cf3](https://github.com/dreulavelle/PTT/commit/f890cf34b8e7cc48abd35749dc8c4475903f31fc))

## [1.2.2](https://github.com/dreulavelle/PTT/compare/v1.2.1...v1.2.2) (2024-08-27)


### Bug Fixes

* fixed remux and shang-chi title returning as chinese ([6088ce3](https://github.com/dreulavelle/PTT/commit/6088ce394887ddada9b5e8560e658ec3962f9794))

## [1.2.1](https://github.com/dreulavelle/PTT/compare/v1.2.0...v1.2.1) (2024-08-26)


### Bug Fixes

* added translate langs to parse_title as well ([0324964](https://github.com/dreulavelle/PTT/commit/032496493cfbb4c92de0c5532784b70aff96c4ac))

## [1.2.0](https://github.com/dreulavelle/PTT/compare/v1.1.0...v1.2.0) (2024-08-26)


### Features

* improvements to audio parsing. added difference between DTS Lossy vs DTS Lossless! ([8a96a0b](https://github.com/dreulavelle/PTT/commit/8a96a0bdd05bb53e4177c422b23f0ffb98dae73d))

## [1.1.0](https://github.com/dreulavelle/PTT/compare/v1.0.0...v1.1.0) (2024-08-25)


### Features

* isort/black applied. added language translation for full langs. ([c82a068](https://github.com/dreulavelle/PTT/commit/c82a0685bb826996723b3ed3772a67312bc8f2ec))

## 1.0.0 (2024-08-25)


### ⚠ BREAKING CHANGES

* release 1.0.0

### Features

* add audio channels handler ([203a15f](https://github.com/dreulavelle/PTT/commit/203a15fc26af37a18af6b6f8dfdbcd9ee030fd1b))
* add edition test ([2392ce3](https://github.com/dreulavelle/PTT/commit/2392ce3616171e69caa0a9651ca6f45d122e54b6))
* add edition test ([fe70088](https://github.com/dreulavelle/PTT/commit/fe70088485ae9dfcbce717895e27b6f9115fbc9a))
* add episode test. ([eb7c0b8](https://github.com/dreulavelle/PTT/commit/eb7c0b8655b21f5dc294f3e16eabe1644770e2b5))
* add improved language support for language chars! all tests passing. ([67d83c3](https://github.com/dreulavelle/PTT/commit/67d83c3f0d35f0c846224717b7daa4a0b649603e))
* add network test ([215ae9d](https://github.com/dreulavelle/PTT/commit/215ae9d7abb9e8c7663bc97ec7b2109890c2a637))
* add ppv support ([643ef01](https://github.com/dreulavelle/PTT/commit/643ef015d7524ddb3026a301df762911db5d57da))
* add readme ([97e9639](https://github.com/dreulavelle/PTT/commit/97e9639c5b43c7d7c83f1687c0f9ff28e02d5f6d))
* add trash tests. add another test to main. ([46d1361](https://github.com/dreulavelle/PTT/commit/46d1361be2a141273714793c7aeebfe51bd7acb1))
* added site, size, networks and other fixes ([2f641dd](https://github.com/dreulavelle/PTT/commit/2f641dde2158aa29efffdaf3c7011bf8d3611064))
* basic title matching working now! ([5096ea8](https://github.com/dreulavelle/PTT/commit/5096ea890aa1f91be92eb8219d5943465eaefd51))
* update season and episode tests. ([d04e8c9](https://github.com/dreulavelle/PTT/commit/d04e8c99e73e9a2c79e5e689627dbf8e8a785ad0))
* wip ([55882fb](https://github.com/dreulavelle/PTT/commit/55882fb8906b71e8993925f712de63dbcaf88d9e))


### Bug Fixes

* add 2 more handlers to trash. add tests for them. ([3d08534](https://github.com/dreulavelle/PTT/commit/3d0853422c16736ced889468dc2ba2f75843f048))
* add more handlers to upscaled. add another test. ([6574ebd](https://github.com/dreulavelle/PTT/commit/6574ebd6db8d2fbb8667e961a9d57ca9fb641d23))
* added clean audio for hindi stuff ([3faaca4](https://github.com/dreulavelle/PTT/commit/3faaca4012760f5eb6872e9dc010cdba7e13fa67))
* fixed 2 failing tests ([157c972](https://github.com/dreulavelle/PTT/commit/157c9725947365dbf93c76769b95fad5a36da8a8))
* fixed 3D and country code tests. added more tests. ([c06223a](https://github.com/dreulavelle/PTT/commit/c06223a96e285c534578eea931fe04c376f09351))
* improved subbed/dubbed attributes. removed from languages. fixed tests. ([d1d2ee2](https://github.com/dreulavelle/PTT/commit/d1d2ee23095bd08947b059997680d136819a6a00))
* **langs:** standardized languages to ISO 639-1. all tests passing. ([30cac1f](https://github.com/dreulavelle/PTT/commit/30cac1fdef4b3323fc87c705c2dc2a96fda8a8a5))
* minor tweaks ([64216da](https://github.com/dreulavelle/PTT/commit/64216da6fc28c2051f047a92bcdc222e29758696))
* move Remastered to edition attribute ([2239a33](https://github.com/dreulavelle/PTT/commit/2239a333161282d4aa33a57fe7a3a429b9a76a72))
* remove print statement ([bf3f256](https://github.com/dreulavelle/PTT/commit/bf3f2568847bd67f678037ef5b906d16471be1b8))
* separate x/h of 264/265 from codecs ([bd2d2df](https://github.com/dreulavelle/PTT/commit/bd2d2dfd42b7df79c5d18ea9bdd6a0bfb5b4c9bd))
* small tweaks ([38a9c60](https://github.com/dreulavelle/PTT/commit/38a9c6073253fc27bb6023a2a20cc4354806cd22))
* standardize more separation for codecs. ([375a640](https://github.com/dreulavelle/PTT/commit/375a6406a2270607694707f04e57e9193e0db013))
* tests all passing. added trash handler. ([4e813e5](https://github.com/dreulavelle/PTT/commit/4e813e54e59ff1fee80628169990e115203388d9))
* **tests:** cleaned up tests and started normalizing handlers ([ef15224](https://github.com/dreulavelle/PTT/commit/ef15224643d812249039cdeb52734be4869c18a5))
* tidied up networks and site handlers. added more tests. ([d26309f](https://github.com/dreulavelle/PTT/commit/d26309f2d28ed15c6aec695383f81da7d518d0dd))
* tidy codecs. various other tweaks. added pdtv quality. ([1ef43ad](https://github.com/dreulavelle/PTT/commit/1ef43ada545fab1d2eccdf24312696127f3fd7ab))
* tidy up functions. ([6a804e9](https://github.com/dreulavelle/PTT/commit/6a804e9edb305887dbd0602836fafa3ecffd8c3a))
* tidy up functions. ([aa9e25e](https://github.com/dreulavelle/PTT/commit/aa9e25e80aa5c66460a3444b89fb0ef1bbcad7f9))
* update french language. tweak test ([fa4c2fa](https://github.com/dreulavelle/PTT/commit/fa4c2fabfc47d7624e20e59f45099622050efe2e))
* update tests. multiple tweaks. ([807287e](https://github.com/dreulavelle/PTT/commit/807287e43d91835ce21a170ab03438d6d6be9ee3))


### Miscellaneous Chores

* release 1.0.0 ([136215b](https://github.com/dreulavelle/PTT/commit/136215b333ee5bc2109e003c15dbc8b1bdd8710e))
