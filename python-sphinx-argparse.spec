%global srcname sphinx-argparse
%global sum Sphinx extension that automatically documents argparse commands and options

Name:           python-%{srcname}
Version:        0.2.2
Release:        1%{?dist}
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/ribozz/%{srcname}/
Source0:        https://github.com/ribozz/%{srcname}/archive/%{version}.tar.gz

BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python3-devel python3-setuptools

%description
Sphinx extension that automatically documents argparse commands and options

%package -n python2-%{srcname}
Requires:       python2-sphinx
BuildRequires:  python2-sphinx
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Sphinx extension that automatically documents argparse commands and options


%package -n python3-%{srcname}
Requires:       python3-sphinx
BuildRequires:  python3-sphinx
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Sphinx extension that automatically documents argparse commands and options


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Fri May 11 2018 Brian C. Lane <bcl@redhat.com> - 0.2.2-1
- Update to new upstream release

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.15-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-6
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.15-3
- Rebuild for Python 3.6

* Tue Feb 02 2016 Brian C. Lane <bcl@redhat.com> 0.1.15-2
- Fix description typo
- Drop %%check section, upstream uses tox for testing.

* Mon Feb 01 2016 Brian C. Lane <bcl@redhat.com> 0.1.15-1
- Initial creation

