Name:		pixelize
Summary:	A program to build larger pictures from hundreds of smaller images 
Version:	1.0.0
Release:	12
Source0:	ftp://lashwhip.com/pub/%{name}-%{version}.tar.gz
Patch0:		pixelize-1.0.0-flags.patch
URL:		https://lashwhip.com/pixelize.html
Group:		Graphics
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
%autosetup -p1

%build
CFLAGS="%{optflags}" DFLAGS="%{ldflags}" CC="%{__cc}" %make_build

%install
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

%files
%defattr(-,root,root) 
%doc README LICENSE  
%{_bindir}/make_db
%{_bindir}/pixelize
%{_datadir}/applications/pixelize.desktop
