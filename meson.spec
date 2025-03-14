Summary:	High productivity build system
Summary(pl.UTF-8):	System budowania o dużej produktywności
Name:		meson
Version:	1.6.1
Release:	6
License:	Apache v2.0
Group:		Development/Tools
#Source0Download: https://github.com/mesonbuild/meson/releases/
Source0:	https://github.com/mesonbuild/meson/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	397e29700c71f69d70fd2b5898620177
Patch0:		%{name}-gtkdocdir.patch
Patch1:		rust-proc-macro-filter-out-target.patch
Patch2:		allow-arm-on-arm64.patch
Patch3:		rpm-macros-pld.patch
URL:		https://mesonbuild.com/
BuildRequires:	ninja >= 1.8.2
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-devel-tools >= 1:3.7
Requires:	python3-libs >= 1:3.7
Requires:	python3-modules >= 1:3.7
Requires:	python3-setuptools
Conflicts:	ninja < 1.8.2
BuildArch:	noarch
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

%package polkit
Summary:	PolKit integration - handle projects installation via Meson
Summary(pl.UTF-8):	Integracja z PolKitem - obsługa instalowania projektów przy użyciu Mesona
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	polkit

%description polkit
PolKit integration - handle projects installation via Meson.

%description polkit -l pl.UTF-8
Integracja z PolKitem - obsługa instalowania projektów przy użyciu
Mesona.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -R
%patch -P3 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	meson.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_rpmmacrodir}

cp -p data/macros.meson $RPM_BUILD_ROOT%{_rpmmacrodir}

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/meson
%{_mandir}/man1/meson.1*
%{py3_sitescriptdir}/meson-%{version}-py*.egg-info
%{py3_sitescriptdir}/mesonbuild
%{_rpmmacrodir}/macros.meson

%files polkit
%defattr(644,root,root,755)
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
