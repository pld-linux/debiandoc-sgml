%include	/usr/lib/rpm/macros.perl
Summary:	SGML-based documentation formatting package
Summary(pl.UTF-8):	Bazujący na SGML pakiet do formatowania dokumentacji
Name:		debiandoc-sgml
Version:	1.2.31
Release:	1
License:	GPL v2+
Group:		Applications/Publishing/SGML
Source0:	http://ftp.debian.org/debian/pool/main/d/debiandoc-sgml/%{name}_%{version}.orig.tar.xz
# Source0-md5:	f89fdd5f2f9242549bbe8b405e1d9734
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.402
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	sgml-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML-based documentation formatting package.

%description -l pl.UTF-8
Bazujący na SGML pakiet do formatowania dokumentacji.

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
%doc README
%attr(755,root,root) %{_bindir}/debiandoc2*
%{perl_vendorlib}/DebianDoc_SGML
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/fixlatex
%attr(755,root,root) %{_datadir}/%{name}/saspconvert
%{_datadir}/sgml/debiandoc
%{_mandir}/man1/debiandoc-sgml.1*
%{_mandir}/man1/debiandoc2*.1*
