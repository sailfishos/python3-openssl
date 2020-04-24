Name:       pyOpenSSL
Version:    0.15.1
Release:    0
Summary:    Python wrapper module around the OpenSSL library
License:    ASL 2.0
URL:        https://github.com/pyca/pyopenssl.git
Source0:    %{name}-%{version}.tar.gz

BuildRequires:	openssl-devel
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%py2_build

%install
%py2_install

%files
%defattr(-,root,root,-)
%{python_sitearch}/OpenSSL/
%{python_sitearch}/%{name}*.egg-info
%doc README.rst
