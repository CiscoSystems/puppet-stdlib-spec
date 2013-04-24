Name:		puppet-stdlib	
Version:	0.1
Release:	1cisco%{?dist}
Summary:	Puppet stdlib module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-stdlib.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This module provides a "standard library" of resources for developing Puppet Modules.

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{name}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{name}/

%files
%dir %{_usr}/share/puppet/modules/%{name}/
%{_usr}/share/puppet/modules/%{name}/*


%defattr(-,root,root,-)
%doc README.markdown README_DEVELOPER.markdown RELEASE_PROCESS.markdown LICENSE CHANGELOG

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 24 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

