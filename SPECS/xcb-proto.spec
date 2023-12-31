%define debug_package %{nil}

Name:           xcb-proto
Version:        1.13
Release:        4%{?dist}
Summary:        XCB protocol descriptions

Group:          Development/Libraries
License:        MIT
URL:            https://xcb.freedesktop.org/
Source0:        https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:	python3-devel
Requires:       pkgconfig

%description
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves.  Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.

%prep
%setup -q

%build
# Bit of a hack to get the pc file in /usr/share, so we can be noarch.
%configure --libdir=%{_datadir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING NEWS README TODO doc/xml-xcb.txt
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%{python3_sitelib}/xcbgen

%changelog
* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.13-4
- Drop useless %%defattr

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13-3
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Adam Jackson <ajax@redhat.com> - 1.13-2
- Switch to python3

* Mon Mar 05 2018 Adam Jackson <ajax@redhat.com> - 1.13-1
- xcb-proto 1.13

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.12-5
- Add a build-time dependency on python2-devel

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 18 2016 Adam Jackson <ajax@redhat.com> - 1.12-1
- xcb-proto 1.12

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 Adam Jackson <ajax@redhat.com> 1.11-1
- xcb-proto 1.11

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Adam Jackson <ajax@redhat.com> 1.10-1
- xcb-proto 1.10

* Mon Dec 02 2013 Adam Jackson <ajax@redhat.com> 1.9-1
- xcb-proto 1.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
