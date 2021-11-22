Name:       python3-openssl
Version:    19.1.0
Release:    0
Summary:    Python wrapper module around the OpenSSL library
License:    ASL 2.0
URL:        https://github.com/pyca/pyopenssl.git
Source0:    %{name}-%{version}.tar.gz

# Support migration from old package name
Provides:       pyOpenSSL = %{version}-%{release}
Obsoletes:      pyOpenSSL
BuildRequires:	pkgconfig(openssl)
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%py3_build

%install
%py3_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{python3_sitelib}/OpenSSL/
%{python3_sitelib}/pyOpenSSL*.egg-info
%doc README.rst
