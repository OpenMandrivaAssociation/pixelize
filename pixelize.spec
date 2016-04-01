Name:		pixelize
Summary:	A program to build larger pictures from hundreds of smaller images 
Version:	1.0.0
Release:	11
Source0:	ftp://lashwhip.com/pub/%{name}-%{version}.tar.gz
Patch0:		pixelize-1.0.0-fix_overlinking.patch
URL:		http://lashwhip.com/pixelize.html
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPLv2+
BuildRequires:	gtk+2.0-devel

%description
Pixelize is a program that will use many scaled down images to
try to duplicate, as closely as possible, another image. It
works by splitting up the image you want rendered (or duplicated)
into a grid of small rectangular areas. Each area is analyzed,
and replaced with an image chosen from a large database of images.
Pixelize tries to pick images that best match each area. It works
best when it can choose images from a very large database of images.
With about 1000 images, Pixelize can do a reasonable job.

%prep
%setup -q
%patch0 -p0

%build
CFLAGS="%{optflags}" DFLAGS="%{ldflags} -lgdk-x11-2.0 -lgobject-2.0 -lm" %make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 pixelize %{buildroot}%{_bindir}
install -m 755 make_db	%{buildroot}%{_bindir}

#mdk menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Pixelize
Exec=%{_bindir}/%{name}
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;
MimeType=image/gif;image/jpeg;image/png;image/bmp;image/x-eps;image/x-ico;image/x-portable-bitmap;image/x-portable-pixmap;image/x-xbitmap;image/x-xpixmap;
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%doc README LICENSE  
%{_bindir}/make_db
%{_bindir}/pixelize
%{_datadir}/applications/pixelize.desktop


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2011.0
+ Revision: 614547
- the mass rebuild of 2010.1 packages

  + Jani Välimaa <wally@mandriva.org>
    - improve patch0

* Sun Mar 21 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-8mdv2010.1
+ Revision: 525993
- fix compiler flags and rediff patch

* Fri Mar 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.0-7mdv2010.1
+ Revision: 518302
- Add a desktop entry

* Tue Mar 09 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-6mdv2010.1
+ Revision: 517011
- bump release (previous release was lost in BS)
- add patch0 (fix overlinking)
- fix license
- fix build for x86_64
- fix description

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.0-4mdv2010.1
+ Revision: 515981
- add an exclusive arch to fix rebuild
- Add a BA
- Fix BR
- import pixelize


