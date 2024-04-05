## 2019.06.18

06-18-2019 08:43 PDT

### Implementation Changes

- Specify --force-local to tar to handle Windows filenames ([#9](https://github.com/googleapis/docuploader/pull/9))
- Update metadata to match docpublisher's ([#7](https://github.com/googleapis/docuploader/pull/7))

### New Features

- Expose new metadata fields to docuploader create-metadata ([#8](https://github.com/googleapis/docuploader/pull/8))

## [0.6.6](https://github.com/googleapis/docuploader/compare/v0.6.5...v0.6.6) (2024-04-05)


### Documentation

* Add summary_overview template ([#192](https://github.com/googleapis/docuploader/issues/192)) ([3f35d13](https://github.com/googleapis/docuploader/commit/3f35d135e8a8acb3ced910fd55c83e9967f7c70b))

## [0.6.5](https://github.com/googleapis/docuploader/compare/v0.6.4...v0.6.5) (2023-02-27)


### Bug Fixes

* Add clarification on where docs.metadata should be ([#151](https://github.com/googleapis/docuploader/issues/151)) ([6435746](https://github.com/googleapis/docuploader/commit/6435746eed252f39a6af01b09238c33288dcf615))
* Prevent empty tarballs from being passed on ([#152](https://github.com/googleapis/docuploader/issues/152)) ([e50d78b](https://github.com/googleapis/docuploader/commit/e50d78bd07462b074d222277bcead5f6b9f2b66c))

## [0.6.4](https://github.com/googleapis/docuploader/compare/v0.6.3...v0.6.4) (2022-10-07)


### Bug Fixes

* **tar:** Add fallback tar without --force-local ([#139](https://github.com/googleapis/docuploader/issues/139)) ([06583af](https://github.com/googleapis/docuploader/commit/06583afcfc23ad305af433015b4e0b370b107928))

### [0.6.3](https://github.com/googleapis/docuploader/compare/v0.6.2...v0.6.3) (2022-04-15)


### Documentation

* update README with ADC credentials command ([#101](https://github.com/googleapis/docuploader/issues/101)) ([f515bbc](https://github.com/googleapis/docuploader/commit/f515bbc1add620f9e11c7d5f002d3eb743762a64))

### [0.6.2](https://github.com/googleapis/docuploader/compare/v0.6.1...v0.6.2) (2022-01-13)


### Bug Fixes

* update storage to v2 ([#95](https://github.com/googleapis/docuploader/issues/95)) ([8967690](https://github.com/googleapis/docuploader/commit/8967690247ab972803963007bde8d1410140778c))

### [0.6.1](https://www.github.com/googleapis/docuploader/compare/v0.6.0...v0.6.1) (2021-06-17)


### Documentation

* expand README ([#69](https://www.github.com/googleapis/docuploader/issues/69)) ([2e25300](https://www.github.com/googleapis/docuploader/commit/2e25300378e77caaa092a30dabb1e66ca726deb8))

## [0.6.0](https://www.github.com/googleapis/docuploader/compare/v0.5.0...v0.6.0) (2021-04-02)


### Features

* make credentials_file optional ([#64](https://www.github.com/googleapis/docuploader/issues/64)) ([a3e7c18](https://www.github.com/googleapis/docuploader/commit/a3e7c1850f684057de8bfbca8e64f19c0cfe816a))

## [0.5.0](https://www.github.com/googleapis/docuploader/compare/v0.4.1...v0.5.0) (2021-04-01)


### Features

* support Application Default Credentials ([#62](https://www.github.com/googleapis/docuploader/issues/62)) ([844b315](https://www.github.com/googleapis/docuploader/commit/844b3150b1ce143ab6fac3f8866bc08d59c9f1fd))

### [0.4.1](https://www.github.com/googleapis/docuploader/compare/v0.4.0...v0.4.1) (2021-02-03)


### Bug Fixes

* update destination_prefix to allow 'docfx-' ([#52](https://www.github.com/googleapis/docuploader/issues/52)) ([ef4532a](https://www.github.com/googleapis/docuploader/commit/ef4532a409926cb65ec5629df536e46a026feab2))

## [0.4.0](https://www.github.com/googleapis/docuploader/compare/v0.3.0...v0.4.0) (2021-01-26)


### Features

* add xref docs.metadata fields ([#46](https://www.github.com/googleapis/docuploader/issues/46)) ([c68c82e](https://www.github.com/googleapis/docuploader/commit/c68c82e09b50802237ae30990b959bddade1c517))
* adding docs.metadata.json support ([#48](https://www.github.com/googleapis/docuploader/issues/48)) ([935aa22](https://www.github.com/googleapis/docuploader/commit/935aa221c91ae58b8e404bc229ff7ea34698e302))

## [0.3.0](https://www.github.com/googleapis/docuploader/compare/v0.2.0...v0.3.0) (2021-01-08)


### Features

* adding timeout argument to be passable ([#43](https://www.github.com/googleapis/docuploader/issues/43)) ([5380c2f](https://www.github.com/googleapis/docuploader/commit/5380c2fc1da51c1b89c7b8251b575e84bde6a5f3))

## [0.2.0](https://www.github.com/googleapis/docuploader/compare/v0.1.0...v0.2.0) (2020-07-22)


### Features

* add tar.decompress ([#31](https://www.github.com/googleapis/docuploader/issues/31)) ([c22c803](https://www.github.com/googleapis/docuploader/commit/c22c803ad3d59076bf0d3ba78f25d99c7a6375f6))

## 0.1.0 (2020-07-14)


### Features

* **docuploader:** add destination-prefix option ([#26](https://www.github.com/googleapis/docuploader/issues/26)) ([68176ed](https://www.github.com/googleapis/docuploader/commit/68176ed98b80a16ab68e58003e61ceeeab68033f))

## 2019.05.30

05-30-2019 12:52 PDT

### Implementation Changes
- Check that required fields exist. ([#4](https://github.com/googleapis/docuploader/pull/4))

## 2019.03.05

03-05-2019 16:35 PST

Initial release.
