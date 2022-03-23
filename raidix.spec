Name:	raidix
Version:	1.0
Release:	1%{?dist}
Summary:	line of code

License:	 GPLv3+
URL:	https://example.com/%{name}
Source0:	https://example.com/rel/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
just line of task.

%prep
%setup	 -T


%build
%{?_smp_mflags}


%install
%make_install


%files
%license	LICENSE



%changelog
* Wed Mar 23 2022 root
- 2nd try
