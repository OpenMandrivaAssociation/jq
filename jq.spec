%define lib_major	1
%define lib_name	%mklibname jq %{lib_major}
%define develname	%mklibname jq -d

Name:		jq
Version:	1.6
Release:	1
Summary:	Command-line JSON processor
Group:		System/Base
License:	MIT and ASL 2.0 and CC-BY and GPLv3
URL:		http://stedolan.github.io/jq/
Source0:	https://github.com/stedolan/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	pkgconfig(oniguruma)
BuildRequires:	valgrind


%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package -n %{lib_name}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{lib_name}
This package contains libraries used by %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/%{name}
%{_datadir}/man/man1/jq.1.*
%{_datadir}/doc/jq/AUTHORS
%{_datadir}/doc/jq/COPYING
%{_datadir}/doc/jq/README
%{_datadir}/doc/jq/README.md
%dir %{_datadir}/doc/jq

%files -n %{lib_name}
%{_libdir}/libjq.so.%{lib_major}
%{_libdir}/libjq.so.%{lib_major}.*

%files -n %{develname}
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so
