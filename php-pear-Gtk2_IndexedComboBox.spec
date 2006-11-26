%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	IndexedComboBox
%define		_status		beta
%define		_pearname	Gtk2_IndexedComboBox

Summary:	%{_pearname} - Indexed Gtk2 combo box similar to the HTML select box
Summary(pl):	%{_pearname} - Indeksowane pole Gtk2 typu combo box podobne do pola wyboru HTML
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ed24417269fb575fd06a678ab8625249
URL:		http://pear.php.net/package/Gtk2_IndexedComboBox/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gtk2)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Indexed Gtk2 combo box similar to the HTML select box. Lets you not
only store values as the normal GtkComboBox, but associated key/value
pairs as well. The active key can be easily received with
get_active_key.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet ten dostarcza mo�liwo�� tworzenia indeksowanego pola Gtk2 typu
combo box podobnego do pola wyboru HTML. Pozwala nie tylko na
przechowywanie warto�ci w typowych GtkComboBox, ale tak�e powi�zania
klucz-warto��. Bie��cy klucz mo�na w �atwy spos�b pobra� przy u�yciu
get_active_key.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc install.log docs/Gtk2_IndexedComboBox/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/IndexedComboBox.php
%{php_pear_dir}/Gtk2/IndexedComboBox

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Gtk2_IndexedComboBox
