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

%description
Anime Games Launcher is an universal launcher for anime games.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build

%install
# copy binary
sudo mkdir -p %{install_dir}
sudo cp -f %{name} %{install_dir}
# create link of binary
sudo ln -sf %{install_dir}/%{name} %{_bindir}/%{name}
# apply exec permision to binary
sudo chmod +x %{install_dir}/%{name}
# copy icon
sudo cp -f assets/icon.png %{icon_dir}
# copy desktop file
sudo cp -f assets/%{name}.desktop %{apps_dir}

%post
cd %{_buildrootdir}
cd ..
rm -rf *

#-- LAUNCHER FILES ------------------------------------------------------------#
cd /
%files
%config %{getenv:HOME}/.local/share/%{name}/config.json
%doc README.md
%license LICENSE
%{install_dir}
%{icon_dir}/icon.png
%{apps_dir}/%{name}.desktop
%{_bindir}/%{name}

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
