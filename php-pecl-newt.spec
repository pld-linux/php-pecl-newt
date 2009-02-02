# TODO
# - current php segfaults when installed
%define		_modname	newt
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - extension for RedHat Newt windowing library
Summary(pl.UTF-8):	%{_modname} - rozszerzenie dla biblioteki Newt
Name:		php-pecl-%{_modname}
Version:	1.2.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	c57fa6a76c7da3bc53ba986b41c9e49a
URL:		http://pecl.php.net/package/newt/
BuildRequires:	newt-devel
BuildRequires:	php-devel >= 4:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires(triggerpostun):	sed >= 4.0
Requires:	%{_sysconfdir}/cli.d
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

%description -l pl.UTF-8
PHP-NEWT to rozszerzenie języka PHP dla biblioteki Newt - terminalowej
biblioteki okienek i widgetów do pisania aplikacji z przyjaznym dla
użytkownika interfejsem. Po włączeniu tego rozszerzenia PHP będzie
udostępniać widgety Newta, takie jak okienka, przyciski, pola wyboru,
etykiety, pola edycyjne, paski przewijania, pola tekstowe, skale itp.
Rozszerzenia tego używa się bardzo podobnie do oryginalnego API Newta
w języku C.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
mv %{_modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{cli,conf}.d,%{extensionsdir},%{_examplesdir}}

install modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/cli.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.0-6.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*%{_modname}\.so/d' %{_sysconfdir}/php-cli.ini

%files
%defattr(644,root,root,755)
%doc CREDITS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
%{_examplesdir}/%{name}-%{version}
