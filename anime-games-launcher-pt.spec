%define install_dir %{_libdir}/anime-games-launcher
%define icon_dir %{_datadir}/icons/hicolor/512x512/apps
%define apps_dir %{_datadir}/applications
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
Source0: https://github.com/retrozinndev/%{srcname}/releases/download/v%{version}/%{srcname}-copr-bin.zip
BuildArch: noarch

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: git
Requires: libcurl
Requires: libadwaita
Requires: gtk4
Requires: glibc
Requires: wget

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
Suggests: mangohud
Suggests: gamescope
Suggests: gamemode

%description
Retrozinndev's fork of Anime Games Launcher. Anime Games Launcher is an universal launcher for anime games.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
# get binary from latest release
wget https://github.com/retrozinndev/%{srcname}/releases/download/v%{version}/%{srcname}
# rename bin to default name
mv anime-games-launcher-pt anime-games-launcher


%install
# copy binary
mkdir -p %{buildroot}%{install_dir}
cp -f %{name} %{buildroot}%{install_dir}
# copy icon
mkdir -p %{buildroot}%{icon_dir}
cp -f assets/icon.png %{buildroot}%{icon_dir}
# copy desktop file
mkdir -p %{buildroot}%{apps_dir}
cp -f assets/%{name}.desktop %{buildroot}%{apps_dir}

%post
# create link of binary
ln -sf %{install_dir}/%{name} %{_bindir}/%{name}
# apply exec permision to binary
chmod +x %{install_dir}/%{name}

#-- LAUNCHER FILES ------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{install_dir}/*
%{icon_dir}/icon.png
%{apps_dir}/%{name}.desktop

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
