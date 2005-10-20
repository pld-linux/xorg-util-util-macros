Summary:	Autoconf macros for xorg
Summary(pl):	Makra autoconfa dla xorg
Name:		xorg-util-util-macros
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/util/util-macros-%{version}.tar.bz2
# Source0-md5:	04a213cd8cbe2c5f4576a4eda73316c4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autoconf macros for xorg.

%description -l pl
Makra autoconfa dla xorg.

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
%{_aclocaldir}/xorg-macros.m4
