# $Rev: 3222 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	Autoconf macros for xorg
Summary(pl):	Makra autoconfa dla xorg
Name:		xorg-util-util-macros
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11/Development
######		Unknown group!
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/util/util-macros-%{version}.tar.bz2
# Source0-md5:	5647ac7ca141725cae6c7fc73fd76dbd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/util-macros-%{version}-root-%(id -u -n)

%description
Autoconf macros for xorg.

%description -l pl
Makra autoconfa dla xorg

%prep
%setup -q -n util-macros-%{version}


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
%{_aclocaldir}/xorgversion.m4
