%define installation_dir /usr/lib
%global srcname anime-games-launcher-pt

Name: anime-games-launcher
Version: 1.0.3.rc1
Release: 1%{dist}
License: GPLv3
Summary: Universal Linux launcher for anime games
Url: https://github.com/retrozinndev/%{srcname}
# Sources can be obtained by
# git clone https://github.com/retrozinndev/%{srcname}.git
# cd %{srcname}
# tito build --tgz
Source0: https://github.com/retrozinndev/%{srcname}/releases/%{version}.tar.gz

BuildArch: noarch

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: git
Requires: libcurl
Requires: libadwaita
Requires: gtk4
Requires: glibc

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
Suggests: mangohud
Suggests: gamescope
Suggests: gamemode

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: rust
BuildRequires: cargo
BuildRequires: git
BuildRequires: libcurl
BuildRequires: libadwaita
BuildRequires: gtk4
BuildRequires: glibc
BuildRequires: p7zip
BuildRequires: gcc
BuildRequires: gcc-c++

%description
Anime Games Launcher is an universal launcher for anime games.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
cargo build --release

%install
mkdir -p %{installation_dir}/%{name}
cp target/release/%{name} %{installation_dir}/%{name}
ln -s %{installation_dir}/%{name}/%{name} /usr/bin/%{name}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/build

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sat Feb 17 2024 João Dias <joaovodias@gmail.com>
- new package built with tito

* Sat Feb 17 2024 João Dias <joaovodias@gmail.com>
- Added new copr package built with tito

