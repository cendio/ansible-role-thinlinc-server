# Change log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Changed

- Updated to 4.20.0
- Update SUSE usr merge workaround to match SLES 16 changes

### Removed

- Support for 32-bit server packages

### Removed

- Old web integration tlsetup answer

## [1.13] - 2025-07-09

### Changed

- Updated to 4.19.0
- Updated paths for HA and subclusters

## [1.12] - 2025-01-07

### Changed

 - Updated to 4.18.0
 - Updated tlsetup answers to match the 4.18.0 changes

## [1.11] - 2024-08-20

### Changed

 - Updated to 4.17.0
 - Simplified/refactored package installation tasks

### Added

 - Added configuration for Web Access & Web Administration ports
 - Added configuration for Web Access login page

### Removed

 - thinlinc_server_bundle and thinlinc_build parameters
 - vars/main.yaml configuration file (redundant)

## [1.10] - 2024-02-01

### Changed

 - Updated to 4.16.0
 - Fixed default value of thinlinc_agent_hostname

## [1.9] - 2023-08-25

### Changed

- Updated to 4.15.0
- Rewrite to fix style issues, fix some tasks to be a bit more 'ansible-y'
- Fixed file permissions warning
- Made role compatible with 'new' ansible_facts[...] notation of facts
- Made template correctly translate true/false to yes/no
- Remove requirement to use groups in inventory

## [1.8] - 2022-02-07

### Changed

- Updated to 4.14.0
- Added workaround for OpenSUSE Tumbleweed usr merge
- In case of package upgrade, force the use of old config files
- Use correct parameter name for thinlinc_server_bundle_file

## [1.7] - 2021-08-31

### Changed

- Updated to 4.13.0
- Updated tlsetup answers to match new Python 3 requirements
- Added .yamllint to catch syntax errors and style issues

## [1.6] - 2021-02-09

### Changed

- Updated to 4.12.1
- Package signature check disabled as ThinLinc packages are not signed
- Add handlers for the tlwebadm and tlwebaccess services

## [1.5] - 2020-06-29

### Changed

- Updated to ThinLinc 4.12.0

## [1.4] - 2019-12-19

### Changed

- Updated to ThinLinc 4.11.0

## [1.3] - 2019-08-27

### Changed

- Updated to ThinLinc 4.10.1
- Inventory names now use underscore (`_`) instead of dash (`-`),
  e.g. `thinlinc-agents`.

## [1.2] - 2019-04-05

### Changed

- Updated to ThinLinc 4.10.0

## [1.1] - 2018-12-13

### Added

- `thinlinc_agent_hostname`, a variable that allows you to customize
  /vsmagent/agent_hostname parameter on ThinLinc Agent servers.

## [1.0] - 2018-11-22

First release.

### Added

- An Ansible role to install the ThinLinc server software.

[unreleased]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.13...HEAD
[1.13]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.12...v1.13
[1.12]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.11...v1.12
[1.11]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.10...v1.11
[1.10]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.9...v1.10
[1.9]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.8...v1.9
[1.8]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.7...v1.8
[1.7]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.6...v1.7
[1.6]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.5...v1.6
[1.5]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.4...v1.5
[1.4]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.3...v1.4
[1.3]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.2...v1.3
[1.2]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.1...v1.2
[1.1]: https://github.com/cendio/ansible-role-thinlinc-server/compare/v1.0...v1.1
[1.0]: https://github.com/cendio/ansible-role-thinlinc-server/compare/...v1.0
