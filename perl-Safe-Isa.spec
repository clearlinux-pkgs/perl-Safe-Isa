#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Safe-Isa
Version  : 1.000010
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Safe-Isa-1.000010.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Safe-Isa-1.000010.tar.gz
Summary  : 'Call isa, can, does and DOES safely on things that may not be objects'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Safe-Isa-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Safe::Isa - Call isa, can, does and DOES safely on things that may not
be objects

%package dev
Summary: dev components for the perl-Safe-Isa package.
Group: Development
Provides: perl-Safe-Isa-devel = %{version}-%{release}
Requires: perl-Safe-Isa = %{version}-%{release}

%description dev
dev components for the perl-Safe-Isa package.


%package perl
Summary: perl components for the perl-Safe-Isa package.
Group: Default
Requires: perl-Safe-Isa = %{version}-%{release}

%description perl
perl components for the perl-Safe-Isa package.


%prep
%setup -q -n Safe-Isa-1.000010
cd %{_builddir}/Safe-Isa-1.000010

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
/usr/share/man/man3/Safe::Isa.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
