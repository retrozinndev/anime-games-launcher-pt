# Anime Games Launcher PT
An [Anime Games Launcher](https://github.com/an-anime-team) fork by [retrozinndev](https://github.com/retrozinndev). Original repo by [An Anime Team](https://github.com/an-anime-team)


[![Copr build status](https://copr.fedorainfracloud.org/coprs/retrozinndev/anime-games-launcher/package/anime-games-launcher/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/retrozinndev/anime-games-launcher/package/anime-games-launcher/)
[![Compile release build](https://github.com/retrozinndev/anime-games-launcher-pt/actions/workflows/compile_release_build.yml/badge.svg)](https://github.com/retrozinndev/anime-games-launcher-pt/actions/workflows/compile_release_build.yml)


## How it looks
| Main window | Game details |
| :-: | :-: |
| <picture><source media="(prefers-color-scheme: dark)" srcset="repository/main-dark.png"><img src="repository/main-light.png"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="repository/details-dark.png"><img src="repository/details-light.png"></picture> |

<p align="center">
    <a href="https://discord.gg/ck37X6UWBp">Discord</a> ·
    <a href="https://matrix.to/#/#an-anime-game:envs.net">Matrix</a>
</p>

<p align="center">
    <b>PROOF OF CONCEPT - NOT FOR EVERYDAY USE</b></br>
    Universal linux launcher for anime games
</p>

<br>

## Docs


## ♥️ Useful links

| Link | Description |
| - | - |
| [macOS launcher](https://github.com/3Shain/yet-another-anime-game-launcher) | Another launcher with special macOS-compatible components |
| [Releases page](https://github.com/an-anime-team/anime-games-launcher/releases) | Launcher releases list |
| [Changelog](CHANGELOG.md) | Launcher updates chronology |
| [Integration guide](repository/integrations) | Games integration standard |
| [Components repo](https://github.com/an-anime-team/components) | Repository with default wine and dxvk versions used in the launcher |
| [Integrations repo](https://github.com/an-anime-team/game-integrations) | Repository with default games integrations used in the launcher |

<br>

## 💻 Development

| Folder | Description |
| - | - |
| src | Rust source code |
| assets | App assets folder |
| target/release | Release build of the app |

### Clone repo

```sh
git clone https://github.com/an-anime-team/anime-games-launcher
```

### Run app

```sh
cargo run
```

## Build app

```sh
cargo build --release
```
