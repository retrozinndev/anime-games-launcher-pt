%define install_dir %{_libdir}/anime-games-launcher
%define icon_dir %{_datadir}/icons/hicolor/512x512/apps
%define apps_dir %{_datadir}/applications
%define app_id moe.launcher.anime-games-launcher
%global srcname anime-games-launcher-pt

Name: anime-games-launcher
Version: 1.0.2.rc3
Release: 1%{?dist}
License: GPLv3
Summary: Universal Linux launcher for anime games
Url: https://github.com/retrozinndev/%{srcname}
# Sources can be obtained by
# git clone https://github.com/retrozinndev/%{srcname}.git
# cd %{srcname}
# tito build --tgz
Source0: https://github.com/retrozinndev/%{srcname}/archive/refs/tags/v%{version}.tar.gz
BuildArch: x86_64

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
BuildRequires: libadwaita-devel
BuildRequires: gtk4-devel
BuildRequires: glibc
BuildRequires: glib2
BuildRequires: glib2-devel
BuildRequires: p7zip
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: pango-devel
BuildRequires: rust-gdk4-devel

%description
Anime Games Launcher is an universal launcher for anime games.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
cargo build --release

%install
# copy binary
mkdir -p %{buildroot}%{install_dir}
cp -f target/release/%{name} %{buildroot}%{install_dir}
# copy icon
mkdir -p %{buildroot}%{icon_dir}
cp -f assets/images/%{app_id}.png %{buildroot}%{icon_dir}
# copy desktop file
mkdir -p %{buildroot}%{apps_dir}
cp -f assets/%{name}.desktop %{buildroot}%{apps_dir}

%post
# create link of binary
ln -sf %{install_dir}/%{name} %{_bindir}/%{name}
# apply exec permision to binary
chmod +x %{install_dir}/%{name}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{install_dir}/*
%{icon_dir}/moe.launcher.anime-games-launcher.png
%{apps_dir}/%{name}.desktop

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
