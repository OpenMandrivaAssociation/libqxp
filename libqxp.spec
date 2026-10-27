%define major 0
%define abi 0.0
%define devname %mklibname qxp -d

Name: libqxp
Version:	0.0.3
Release:	1
Source0:	https://dev-www.libreoffice.org/src/libqxp/libqxp-%{version}.tar.xz
Summary: Library for parsing QuarkXPress files
URL: https://wiki.documentfoundation.org/DLP/Libraries/libqxp
License: LGPLv2.1/MPL
Group: System/Libraries
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: boost-devel
BuildRequires: doxygen
BuildSystem: autotools

# doxygen no longer emits the diagram pngs the Makefile installs.
%build -a
find . -type d -path '*/docs/doxygen/html' -exec sh -c 'compgen -G "$1/*.png" >/dev/null || touch "$1/placeholder.png"' _ {} \;

%libpackage qxp %{abi} %{major}

%define libname %mklibname qxp %{abi} %{major}

%description
Libqxp is a library that parses the file format of QuarkXPress documents.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Libqxp is a library that parses the file format of QuarkXPress documents.

%package doc
Summary: Documentation for %{name}
Group: Development/C

%description doc
Documentation for %{name}.

Libqxp is a library that parses the file format of QuarkXPress documents.

%files
%{_bindir}/qxp2*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%{_docdir}/%{name}
