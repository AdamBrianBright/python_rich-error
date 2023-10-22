# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## `1.0.0` [!badge variant="info" text="NEXT"]

Expected: unknown

## `0.3.0` [!badge variant="info" text="LATEST"]

Released: 2023-10-22

### Changed

- [x] Updated python to `3.12`
- [x] Updated dependencies

## `0.2.3

Released: 2021-11-27

### Fixed

- [x] Fixed `Unhashable Type RichErr` was causing rollbar troubles with reporting RichErr exceptions

## `0.2.2`

Released: 2021-10-17

### Added

- [x] Added `__str__` and `__repr__` methods for base error class

## `0.2.1`

Released: 2021-10-06

### Changed

- [x] Updated python to 3.10.0

## `0.2.0`

Released: 2021-10-02

### Added

- [x] Added `Pydantic` error support
- [x] Added bytes support for string arguments

### Changed

- [x] Removed trailing `Exception` from error name in `error.exception`

## `0.1.2`

Released: 2021-09-24

### Fixed

- [x] Fixed error conversion losing default code

## `0.1.1`

Released: 2021-09-18

### Changed

- [x] Base error now inherits `Exception` instead of `BaseException`

### Fixed

- [x] Fixed typing issues with `add_conversion` like methods

## `0.1.0`

Released: 2021-09-17

### Added

- [x] Project started