Summary:	High productivity build system
Name:		meson
Version:	0.40.1
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/mesonbuild/meson/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8475b19d5f5f3bd5c40f4bb1f31b93f3
URL:		http://mesonbuild.com/
BuildRequires:	ninja >= 1.5
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meson is a build system designed to optimize programmer productivity.
It aims to do this by providing simple, out-of-the-box support for
modern software development tools and practices, such as unit tests,
coverage reports, Valgrind, CCache and the like.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc authors.txt contributing.txt README.md
%attr(755,root,root) %{_bindir}/meson
%attr(755,root,root) %{_bindir}/mesonconf
%attr(755,root,root) %{_bindir}/mesonintrospect
%attr(755,root,root) %{_bindir}/mesontest
%attr(755,root,root) %{_bindir}/wraptool
%{_mandir}/man1/meson.1*
%{_mandir}/man1/mesonconf.1*
%{_mandir}/man1/mesonintrospect.1*
%{_mandir}/man1/mesontest.1*
%{_mandir}/man1/wraptool.1*
%{py3_sitescriptdir}/meson-*-py3*.egg-info
%{py3_sitescriptdir}/mesonbuild
