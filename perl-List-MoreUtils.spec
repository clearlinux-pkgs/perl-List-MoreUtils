#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-MoreUtils
Version  : 0.430
Release  : 50
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.430.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.430.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblist-moreutils-perl/liblist-moreutils-perl_0.416-1.debian.tar.xz
Summary  : 'Provide the stuff missing in List::Util'
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 MIT
Requires: perl-List-MoreUtils-license = %{version}-%{release}
Requires: perl-List-MoreUtils-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::MoreUtils::XS)

%description
# NAME
List::MoreUtils - Provide the stuff missing in List::Util
# SYNOPSIS
# import specific functions

%package dev
Summary: dev components for the perl-List-MoreUtils package.
Group: Development
Provides: perl-List-MoreUtils-devel = %{version}-%{release}
Requires: perl-List-MoreUtils = %{version}-%{release}

%description dev
dev components for the perl-List-MoreUtils package.


%package license
Summary: license components for the perl-List-MoreUtils package.
Group: Default

%description license
license components for the perl-List-MoreUtils package.


%package perl
Summary: perl components for the perl-List-MoreUtils package.
Group: Default
Requires: perl-List-MoreUtils = %{version}-%{release}

%description perl
perl components for the perl-List-MoreUtils package.


%prep
%setup -q -n List-MoreUtils-0.430
cd %{_builddir}
tar xf %{_sourcedir}/liblist-moreutils-perl_0.416-1.debian.tar.xz
cd %{_builddir}/List-MoreUtils-0.430
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/List-MoreUtils-0.430/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils
cp %{_builddir}/List-MoreUtils-0.430/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/List-MoreUtils-0.430/t/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/446678782aae2b15edd14ce41e923805e8e0345a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::MoreUtils.3
/usr/share/man/man3/List::MoreUtils::Contributing.3
/usr/share/man/man3/List::MoreUtils::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-MoreUtils/446678782aae2b15edd14ce41e923805e8e0345a
/usr/share/package-licenses/perl-List-MoreUtils/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
