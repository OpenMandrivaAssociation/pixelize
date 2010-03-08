%define	name	pixelize
%define	version	1.0.0
%define release	%mkrel 3		

Name:		%{name}
Summary:	A program to build larger pictures from hundreds of smaller images 
Version:	%{version}
Release:	%{release}	
Source0:	ftp://lashwhip.com/pub/%{name}-%{version}.tar.gz
URL:		http://lashwhip.com/pixelize.html
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPLv2
BuildRequires:	libgtk+2.0_0-devel
#BuildRequires:	gtk+2.0_0-devel 
BuildRequires:	gtk+2.0
BuildRequires:	libgtk+2.0_0
BuildArch:	i586

%description
Pixelize is a program that will use many scaled down images to try to duplicate, as closely as possible, another image. It works by splitting up the image you want rendered (or duplicated) into a grid of small rectangular areas. Each area is analyzed, and replaced with an image chosen from a large database of images. Pixelize tries to pick images that best match each area. It works best when it can choose images from a very large database of images. With about 1000 images, Pixelize can do a reasonable job. 

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install -m 755 pixelize %{buildroot}%{_bindir}
install -m 755 make_db	%{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc README LICENSE  
%{_bindir}/make_db
%{_bindir}/pixelize
