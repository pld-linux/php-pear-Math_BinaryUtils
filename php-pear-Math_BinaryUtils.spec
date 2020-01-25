%define		_status		alpha
%define		_pearname	Math_BinaryUtils
Summary:	%{_pearname} - Collection of helper methods for easy handling of binary data
Summary(pl.UTF-8):	%{_pearname} - Kolekcja przydatnych funkcji do obsługi danych binarnych
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	4
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f0532a5be8c4ff4569bc7c6442a92b83
URL:		http://pear.php.net/package/Math_BinaryUtils/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of helper methods for dealing with binary data (add,
subtract, converting functions, endianess functions etc.).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Kolekcja przydatnych funkcji do obsługi danych binarnych (dodawanie,
odejmowanie, funkcje konwersji i obsługi kolejności bajtów w słowie
itp.).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/*.php
