%define major 0
%define abi 0.0
%define devname %mklibname qxp -d

Name: libqxp
Version: 0.0.1
Release: 2
Source0: http://dev-www.libreoffice.org/src/libqxp/libqxp-%{version}.tar.xz
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

%prep
%setup -q
%apply_patches
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/qxp2*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%{_docdir}/%{name}
