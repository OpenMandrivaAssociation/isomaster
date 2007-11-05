%define name	isomaster
%define version	1.2
%define release	%mkrel 2

Summary:	GTK+-based ISO image editor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
Patch0:		isomaster-0.8.1-directories.patch
License:	GPLv2
Group:		Archiving/Cd burning
URL:		http://littlesvr.ca/isomaster/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick

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
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

perl -pi -e 's,/usr/share/%{name}/icons/isomaster.png,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert -scale 48 icons/isomaster.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png 
convert -scale 32 icons/isomaster.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 icons/isomaster.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%post
%update_icon_cache hicolor
%update_menus
%update_desktop_database
%postun
%clean_icon_cache hicolor
%clean_menus
%clean_desktop_database

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
