%{!?python:%define python python}
%{!?python_sitearch: %define python_sitearch %(%{python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:       pyOpenSSL
Version:    0.13.1
Release:    0
Summary:    Python wrapper module around the OpenSSL library

Group:      Development/Libraries
License:    ASL 2.0
URL:        https://launchpad.net/pyopenssl
Source0:    %{name}-%{version}.tar.gz

BuildRequires:	openssl-devel
BuildRequires:  %{python}-devel
Requires:	    %{python}


%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%prep
%setup -q -n %{name}-%{version}/%{name}

# Fix permissions for debuginfo package
%{__chmod} -x OpenSSL/ssl/connection.c

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/OpenSSL/
%{python_sitearch}/%{name}*.egg-info
%doc README
