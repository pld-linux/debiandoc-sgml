%include	/usr/lib/rpm/macros.perl
Summary:	SGML-based documentation formatting package
Summary(pl):	Bazuj±cy na SGML pakiet do formatowania dokumentacji
Name:		debiandoc-sgml
Version:	1.1.83
Release:	1
License:	GPL 2
Group:		Applications/Publishing/SGML
Source0:	ftp://ftp.debian.org/debian/pool/main/d/debiandoc-sgml/%{name}_%{version}.tar.gz
# Source0-md5:	abc5ea35af3fbce2968517be9eeb1d74
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML-based documentation formatting package.

%description -l pl
Bazuj±cy na SGML pakiet do formatowania dokumentacji.

%prep
%setup -q

%build
%{__make} \
	prefix=%{_prefix} \
	perl_dir=%{perl_vendorlib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	perl_dir=$RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/debiandoc2*
%{perl_vendorlib}/DebianDoc_SGML
%{_datadir}/%{name}
%{_datadir}/sgml/debiandoc
%{_mandir}/man?/*
