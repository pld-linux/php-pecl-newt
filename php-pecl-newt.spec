%define		_modname	newt
%define		_status		beta

Summary:	%{_modname} - Extension for RedHat Newt windowing library
Summary(pl):	%{_modname} - Rozszerzenie biblioteki Newt
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	7a5816b24032188545a31d51b2527800
Patch0:		%{name}-compile_fix.patch
Patch1:		%{name}-missing_ifdefs.patch
URL:		http://pecl.php.net/package/newt/
BuildRequires:	libtool
BuildRequires:	newt-devel
BuildRequires:	php-devel >= 4.3.0
Requires:	php-common >= 4.3.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
PHP-NEWT - PHP language extension for RedHat Newt library, a
terminal-based window and widget library for writing applications with
user friendly interface. Once this extension is enabled in PHP it will
provide the use of Newt widgets, such as windows, buttons, checkboxes,
radiobuttons, labels, editboxes, scrolls, textareas, scales, etc. Use
of this extension if very similar to the original Newt API fo C
programming language.

In PECL status of this extension is: %{_status}.

#%description -l pl
#
#To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
cd %{_modname}-%{version}
%patch0 -p1
%patch1 -p1

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,TODO}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
