# Anime Games Launcher PT
An [Anime Games Launcher](https://github.com/an-anime-team) fork by [retrozinndev](https://github.com/retrozinndev). Original repo by [An Anime Team](https://github.com/an-anime-team)


[![Copr build status](https://copr.fedorainfracloud.org/coprs/retrozinndev/anime-games-launcher/package/anime-games-launcher/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/retrozinndev/anime-games-launcher/package/anime-games-launcher/)
[![Compile release build](https://github.com/retrozinndev/anime-games-launcher-pt/actions/workflows/compile_release_build.yml/badge.svg)](https://github.com/retrozinndev/anime-games-launcher-pt/actions/workflows/compile_release_build.yml)


## How it looks
| Main window | Game details |
| :-: | :-: |
| <picture><source media="(prefers-color-scheme: dark)" srcset="repository/main-dark.png"><img src="repository/main-light.png"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="repository/details-dark.png"><img src="repository/details-light.png"></picture> |

<p align="center">
    <a href="https://discord.gg/ck37X6UWBp">Discord</a>(An Anime Team) ·
    <a href="https://matrix.to/#/#an-anime-game:envs.net">Matrix</a>(An Anime Team)
</p>

<p align="center">
    <b>PROOF OF CONCEPT - NOT FOR EVERYDAY USE</b></br>
    Retrozinn Dev's fork of the Universal linux launcher for anime games.
</p>

<br>

## 📚️ Docs
- [Launcher Integrations](repository/integrations);
- [Fedora Copr Install](repository/guides/FEDORA_COPR.md);
- [Changelog](CHANGELOG.md)

## ♥️ Useful links

| Link | Description |
| - | - |
| [macOS launcher](https://github.com/3Shain/yet-another-anime-game-launcher) | Another launcher with special macOS-compatible components |
| [Releases page](https://github.com/an-anime-team/anime-games-launcher/releases) | Launcher releases list |
| [Components repo](https://github.com/an-anime-team/components) | Repository with default wine and dxvk versions used in the launcher |
| [Integrations repo](https://github.com/an-anime-team/game-integrations) | Repository with default games integrations used in the launcher |

## 💻 Development

| Folder | Description |
| - | - |
| `src` | Source code |
| `assets` | App assets |
| `target/release` | Release build directory |

### 📥️ Clone repo

```sh
git clone https://github.com/an-anime-team/anime-games-launcher
```

## 🔨 Build app

```sh
cargo build --release
```

### 🎮️ Run app

```sh
cargo run
```
