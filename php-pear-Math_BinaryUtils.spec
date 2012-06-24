%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	BinaryUtils
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Collection of helper methods for easy handling of binary data
Summary(pl):	%{_pearname} - Kolekcja przydatnych funkcji do obs�ugi danych binarnych
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f0532a5be8c4ff4569bc7c6442a92b83
URL:		http://pear.php.net/package/Math_BinaryUtils/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of helper methods for dealing with binary data (add,
subtract, converting functions, endianess functions etc.).

In PEAR status of this package is: %{_status}.

%description -l pl
Kolekcja przydatnych funkcji do obs�ugi danych binarnych (dodawanie,
odejmowanie, funkcje konwersji i obs�ugi kolejno�ci bajt�w w s�owie
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
%{php_pear_dir}/%{_class}/*.php
