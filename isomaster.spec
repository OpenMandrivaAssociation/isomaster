Summary:	GTK+-based ISO image editor
Name:		isomaster
Version:	1.3.9
Release:	%mkrel 1
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
Patch0:		isomaster-0.8.1-directories.patch
License:	GPLv2
Group:		Archiving/Cd burning
URL:		http://littlesvr.ca/isomaster/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick

%description
ISO Master is an open-source, easy to use, graphical CD image editor. 
You can use this program to extract files from an ISO, add files to an
ISO, and create bootable ISOs - all in a graphical user interface. It 
can open both ISO and NRG files but can only save as ISO.

%prep
%setup -q -n %{name}-%{version}
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

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mv %{buildroot}%{_datadir}/doc/bkisofs/* %{buildroot}%{_datadir}/doc/%{name}/


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Thu May 24 2012 Eugene Budanov <eugene.budanov@rosalab.ru> 1.3.9-1-rosa.lts2012.0
- Update to new release 1.3.9
- cleaned spec

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.7-2mdv2011.0
+ Revision: 612420
- the mass rebuild of 2010.1 packages

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 1.3.7-1mdv2010.1
+ Revision: 487298
- Update to new version 1.3.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.3.5-1mdv2009.1
+ Revision: 324849
- update to new version 1.3.5

* Mon Dec 15 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.4-1mdv2009.1
+ Revision: 314446
- new release 1.3.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 02 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.3-1mdv2009.0
+ Revision: 230825
- new release 1.3.3

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Feb 05 2008 Funda Wang <fwang@mandriva.org> 1.3.1-1mdv2008.1
+ Revision: 162797
- update to new version 1.3.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.3-1mdv2008.1
+ Revision: 132467
- minor spec cleanups
- new release 1.3

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-2mdv2008.1
+ Revision: 106207
- rebuild for lzma permissions issue (#35309)

* Mon Oct 29 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-1mdv2008.1
+ Revision: 103130
- make macro usage more consistent
- new release 1.2

* Tue Aug 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.1-1mdv2008.0
+ Revision: 72431
- drop some unneeded icons and X-Mandriva menu category
- spec clean
- new release 1.1

* Sun Jun 10 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-1mdv2008.0
+ Revision: 37740
- new release 1.0

* Thu Apr 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 14914
- Import isomaster

