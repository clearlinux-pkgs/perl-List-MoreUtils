#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-MoreUtils
Version  : 0.416
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/List-MoreUtils-0.416.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/List-MoreUtils-0.416.tar.gz
Summary  : 'Provide the stuff missing in List::Util'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-List-MoreUtils-lib
Requires: perl-List-MoreUtils-doc
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(XSLoader)

%description
# NAME
List::MoreUtils - Provide the stuff missing in List::Util
# SYNOPSIS
# import specific functions

%package doc
Summary: doc components for the perl-List-MoreUtils package.
Group: Documentation

%description doc
doc components for the perl-List-MoreUtils package.


%package lib
Summary: lib components for the perl-List-MoreUtils package.
Group: Libraries

%description lib
lib components for the perl-List-MoreUtils package.


%prep
%setup -q -n List-MoreUtils-0.416

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/List/MoreUtils.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/List/MoreUtils/Contributing.pod
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/List/MoreUtils/PP.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/List/MoreUtils/XS.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/auto/List/MoreUtils/MoreUtils.so
