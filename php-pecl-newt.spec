%define		php_name	php%{?php_suffix}
%define		modname	newt
%define		status		stable
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{modname} - extension for RedHat Newt windowing library
Summary(pl.UTF-8):	%{modname} - rozszerzenie dla biblioteki Newt
Name:		%{php_name}-pecl-%{modname}
Version:	1.2.5
Release:	3
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	5f9bb7704ac15175e0dda63e38408728
Patch0:		php-pecl-%{modname}-tsrm.patch
URL:		http://pecl.php.net/package/newt/
BuildRequires:	%{php_name}-devel >= 4:5.0.0
BuildRequires:	newt-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires(triggerpostun):	sed >= 4.0
Requires:	%{_sysconfdir}/cli.d
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-NEWT - PHP language extension for RedHat Newt library, a
terminal-based window and widget library for writing applications with
user friendly interface. Once this extension is enabled in PHP it will
provide the use of Newt widgets, such as windows, buttons, checkboxes,
radiobuttons, labels, editboxes, scrolls, textareas, scales, etc. Use
of this extension if very similar to the original Newt API fo C
programming language.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
PHP-NEWT to rozszerzenie języka PHP dla biblioteki Newt - terminalowej
biblioteki okienek i widgetów do pisania aplikacji z przyjaznym dla
użytkownika interfejsem. Po włączeniu tego rozszerzenia PHP będzie
udostępniać widgety Newta, takie jak okienka, przyciski, pola wyboru,
etykiety, pola edycyjne, paski przewijania, pola tekstowe, skale itp.
Rozszerzenia tego używa się bardzo podobnie do oryginalnego API Newta
w języku C.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -q -c
mv %{modname}-%{version}/* .
%patch0 -p1

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{cli,conf}.d,%{extensionsdir},%{_examplesdir}}

install modules/%{modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/cli.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.0-6.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*%{modname}\.so/d' %{_sysconfdir}/php-cli.ini

%files
%defattr(644,root,root,755)
%doc CREDITS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/%{modname}.ini
%attr(755,root,root) %{extensionsdir}/%{modname}.so
%{_examplesdir}/%{name}-%{version}
