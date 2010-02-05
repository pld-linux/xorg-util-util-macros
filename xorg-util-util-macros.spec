Summary:	Autoconf macros for xorg
Summary(pl.UTF-8):	Makra autoconfa dla xorg
Name:		xorg-util-util-macros
Version:	1.6.0
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
# Source0-md5:	6a0ac8efb11ad9b867f2e08ef87ad4c4
Patch0:		%{name}-x.patch
Patch1:		%{name}-nosilent.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
Requires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of autoconf macros used by the configure.ac scripts in
other Xorg modular packages, and is needed to generate new versions of
their configure scripts with autoconf.

%description -l pl.UTF-8
Ten pakiet zawiera makra autoconfa używane przez skrypty configure.ac
w innych pakietach modularnego Xorg. Jest wymagany do generowania
nowych wersji skryptów configure przy użyciu autoconfa.

%prep
%setup -q -n util-macros-%{version}
%patch0 -R -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_aclocaldir}/xorg-macros.m4
%{_npkgconfigdir}/xorg-macros.pc
