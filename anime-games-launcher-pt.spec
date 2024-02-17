%global srcname anime-games-launcher

Name: %{srcname}
Version: 0.0.0
Release: 0%\{?dist}
License: GPLv3
Summary: Universal linux launcher for anime games
Url: https://github.com/retrozinndev/%{srcname}-pt
# Sources can be obtained by
# git clone https://github.com/retrozinndev/anime-games-launcher-pt
# cd anime-games-launcher-pt
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

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
%git clone https://github.com/retrozinndev/anime-games-launcher-pt
%mv %{srcname}-pt/ %{srcname}/
%cd %{srcname}
%cargo build --release

%install
%mkdir -p /usr/lib/%{srcname}
%cp target/release/%{srcname} /usr/lib/%{srcname}
%ln -s /usr/lib/%{srcname}/%{srcname} /usr/bin/anime-games-launcher

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/build

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
