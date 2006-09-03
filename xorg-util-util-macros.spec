Summary:	Autoconf macros for xorg
Summary(pl):	Makra autoconfa dla xorg
Name:		xorg-util-util-macros
Version:	1.1.1
Release:	2
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
# Source0-md5:	8bf679b46bcf755cc4a136835f3e75d4
Patch0:		%{name}-x.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autoconf macros for xorg.

%description -l pl
Makra autoconfa dla xorg.

%prep
%setup -q -n util-macros-%{version}
%patch0 -R -p1

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
%doc COPYING ChangeLog
%{_aclocaldir}/xorgversion.m4
%{_aclocaldir}/xorg-macros.m4
