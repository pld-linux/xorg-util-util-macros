#
# Conditional build:
%bcond_with	manx	# "x" suffix for manpage files
# NOTE: FHS 2.3 says that X man pages must have .[1-8]x extensions;
# but has been dropped in Xorg upstream and requires sed fixes to generate proper .so refs
# (to point to man[1-8] dirs, not man[1-8]x)
#
Summary:	Autoconf macros for xorg
Summary(pl.UTF-8):	Makra autoconfa dla xorg
Name:		xorg-util-util-macros
Version:	1.19.2
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	https://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
# Source0-md5:	58edef899364f78fbde9479ded20211e
Patch0:		%{name}-x.patch
Patch1:		%{name}-nosilent.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.62
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
%{?with_manx:%patch0 -R -p1}
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
%{_datadir}/util-macros
%{_aclocaldir}/xorg-macros.m4
%{_npkgconfigdir}/xorg-macros.pc
