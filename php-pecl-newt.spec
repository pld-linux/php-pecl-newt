%define		_modname	newt
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - extension for RedHat Newt windowing library
Summary(pl):	%{_modname} - rozszerzenie dla biblioteki Newt
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	bb208abdcf759bd789822ef6ddaf77f2
URL:		http://pecl.php.net/package/newt/
BuildRequires:	newt-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.254
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Requires:	php-cli
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-NEWT - PHP language extension for RedHat Newt library, a
terminal-based window and widget library for writing applications with
user friendly interface. Once this extension is enabled in PHP it will
provide the use of Newt widgets, such as windows, buttons, checkboxes,
radiobuttons, labels, editboxes, scrolls, textareas, scales, etc. Use
of this extension if very similar to the original Newt API fo C
programming language.

In PECL status of this extension is: %{_status}.

%description -l pl
PHP-NEWT to rozszerzenie j�zyka PHP dla biblioteki Newt - terminalowej
biblioteki okienek i widget�w do pisania aplikacji z przyjaznym dla
u�ytkownika interfejsem. Po w��czeniu tego rozszerzenia PHP b�dzie
udost�pnia� widgety Newta, takie jak okienka, przyciski, pola wyboru,
etykiety, pola edycyjne, paski przewijania, pola tekstowe, skale itp.
Rozszerzenia tego u�ywa si� bardzo podobnie do oryginalnego API Newta
w j�zyku C.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cli.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cli.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,TODO}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
