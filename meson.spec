Summary:	High productivity build system
Summary(pl.UTF-8):	System budowania o dużej produktywności
Name:		meson
Version:	0.46.1
Release:	6
License:	Apache v2.0
Group:		Development/Tools
#Source0Download: https://github.com/mesonbuild/meson/releases/
Source0:	https://github.com/mesonbuild/meson/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1698f6526574839de5dcdc45e3f7d582
Patch0:		%{name}-gtkdocdir.patch
URL:		http://mesonbuild.com/
BuildRequires:	ninja >= 1.5
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-devel-tools >= 1:3.5
Requires:	python3-libs >= 1:3.5
Requires:	python3-modules >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meson is a build system designed to optimize programmer productivity.
It aims to do this by providing simple, out-of-the-box support for
modern software development tools and practices, such as unit tests,
coverage reports, Valgrind, CCache and the like.

%description -l pl.UTF-8
Meson to system budowania zaprojektowany z myślą o optymalizacji
produktywności programisty. Celem jest dostarczenie prostej, od razu
działającej obsługi nowoczesnych narzędzi i praktyk programistycznych,
takich jak testy jednostkowe, raporty pokrycia, Valgrind, CCache itp.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	meson.py mesonconf.py mesonintrospect.py mesontest.py wraptool.py
%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
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
%{py3_sitescriptdir}/meson-%{version}-py*.egg-info
%{py3_sitescriptdir}/mesonbuild
