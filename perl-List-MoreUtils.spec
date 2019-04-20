#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-MoreUtils
Version  : 0.428
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.428.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.428.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblist-moreutils-perl/liblist-moreutils-perl_0.416-1.debian.tar.xz
Summary  : Provide the stuff missing in List::Util
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 MIT
Requires: perl-List-MoreUtils-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::MoreUtils::XS)

%description
This scripts were submitted to #rt as examples of
memory leaks. All these memory leaks appear now to be fixed.
The name of the script corresponds to the #rt bug number.

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


%prep
%setup -q -n List-MoreUtils-0.428
cd ..
%setup -q -T -D -n List-MoreUtils-0.428 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/List-MoreUtils-0.428/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/deblicense_copyright
cp t/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils/t_LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/List/MoreUtils.pm
/usr/lib/perl5/vendor_perl/5.28.2/List/MoreUtils/Contributing.pod
/usr/lib/perl5/vendor_perl/5.28.2/List/MoreUtils/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::MoreUtils.3
/usr/share/man/man3/List::MoreUtils::Contributing.3
/usr/share/man/man3/List::MoreUtils::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-MoreUtils/LICENSE
/usr/share/package-licenses/perl-List-MoreUtils/deblicense_copyright
/usr/share/package-licenses/perl-List-MoreUtils/t_LICENSE
