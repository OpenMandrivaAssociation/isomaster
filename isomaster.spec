%define name isomaster
%define version 0.8.1
%define release %mkrel 1

Summary: GTK+-based ISO image editor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
Patch0: isomaster-0.8.1-directories.patch
License: GPL
Group: Archiving/Cd burning
Url: http://littlesvr.ca/isomaster/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtk+2-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick

%description
ISO Master is an open-source, easy to use, graphical CD image editor. 
You can use this program to extract files from an ISO, add files to an
ISO, and create bootable ISOs - all in a graphical user interface. It 
can open both ISO and NRG files but can only save as ISO.

%prep
%setup -q
%patch0 -p0 -b .directories

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-System-Archiving-CDBurning" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -e 's/\/usr\/share\/%{name}\/icons\/isomaster.png/%{name}/' %buildroot%{_datadir}/applications/%{name}.desktop > %buildroot%{_datadir}/applications/%{name}.new && \
mv -f %buildroot%{_datadir}/applications/%{name}.new %buildroot%{_datadir}/applications/%{name}.desktop

mkdir -p %buildroot{%_liconsdir,%_miconsdir}
mkdir -p %buildroot%{_iconsdir}/hicolor
mkdir -p %buildroot%{_iconsdir}/hicolor/{48x48,32x32,24x24,22x22,16x16}
mkdir -p %buildroot%{_iconsdir}/hicolor/{48x48,32x32,24x24,22x22,16x16}/apps
convert -scale 48 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_liconsdir/%{name}.png
convert -scale 48 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/hicolor/48x48/apps/%{name}.png 
convert -scale 32 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/%{name}.png
convert -scale 32 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/hicolor/32x32/apps/%{name}.png
convert -scale 24 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/hicolor/24x24/apps/%{name}.png
convert -scale 22 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/hicolor/22x22/apps/%{name}.png
convert -scale 16 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_miconsdir/%{name}.png
convert -scale 16 $RPM_BUILD_ROOT/usr/share/isomaster/icons/isomaster.png %buildroot%_iconsdir/hicolor/16x16/apps/%{name}.png

%post
%update_icon_cache hicolor
%update_menus
%update_desktop_database
%postun
%clean_icon_cache hicolor
%clean_menus
%clean_desktop_database

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%dir %_datadir/%{name}
%dir %_datadir/%{name}/icons
%_datadir/%{name}/icons/*
%_iconsdir/hicolor/16x16/apps/%{name}.png
%_iconsdir/hicolor/22x22/apps/%{name}.png
%_iconsdir/hicolor/24x24/apps/%{name}.png
%_iconsdir/hicolor/32x32/apps/%{name}.png
%_iconsdir/hicolor/48x48/apps/%{name}.png
%_liconsdir/%{name}.png
%_iconsdir/%{name}.png
%_miconsdir/%{name}.png
%_mandir/man1/%{name}.1.bz2
