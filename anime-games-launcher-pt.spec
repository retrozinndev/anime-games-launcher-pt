%define install_dir /usr/lib/anime-games-launcher
%define icon_dir /usr/share/icons/hicolor/512x512/apps
%define apps_dir /usr/share/applications
%global srcname anime-games-launcher-pt

Name: anime-games-launcher
Version: 1.0.2.rc2
Release: 1%{?dist}
License: GPLv3
Summary: Universal Linux launcher for anime games
Url: https://github.com/retrozinndev/%{srcname}
# Sources can be obtained by
# git clone https://github.com/retrozinndev/anime-games-launcher-pt.git
# cd anime-games-launcher-pt
# tito build --tgz
Source0: https://github.com/retrozinndev/%{srcname}/archive/refs/tags/v%{version}.tar.gz
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
# copy binary and create link
mkdir -p %{install_dir}
cp -f target/release/%{name} %{install_dir}
ln -s %{install_dir}/%{name} /usr/bin/%{name}
# apply exec permision to binary
chmod +x %{install_dir}/%{name}
# copy icon
cp -f assets/images/icon.png %{icon_dir}
# copy desktop file
cp -f assets/%{name}.desktop %{apps_dir}

#-- FILES ---------------------------------------------------------------------#
%files
%{install_dir}/*
%{icon_dir}/icon.png
%{apps_dir}/%{name}.desktop
%doc README.md
%license LICENSE
%{_bindir}/%{name}

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
