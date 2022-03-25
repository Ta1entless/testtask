Name:           task
Version:        1.0
Release:        1%{?dist}
Summary:        Code script

License:        GPLv3
Source:		https://example.com/releases/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
the new rpm pack.

%prep
%setup -q


%build
make %{?_smp_flags}


%install
%make_install


%files
%license LICENSE
%doc
%{_bindir}/task



%changelog
* Fri Mar 25 2022 root
- New way commiting task into binary rpm 
