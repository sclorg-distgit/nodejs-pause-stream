%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# BR: for tests are not packaged yet
%global enable_tests 0

%global module_name pause-stream

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.0.11
Release:        6%{?dist}
Summary:        A ThroughStream that strictly buffers all readable events when paused

License:        MIT and ASL 2.0
URL:            http://github.com/dominictarr/pause-stream
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(stream-tester)
BuildRequires:  %{?scl_prefix}npm(stream-spec)
%endif

%description
This is a Stream that will strictly buffer when paused. Connect it to anything
you need buffered.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test/index.js && node test/pause-end.js
%endif

%files
%doc readme.markdown LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.11-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.11-5
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 0.0.11-4
- Enable find provides and requires macro

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 0.0.11-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.11-1
- Initial packaging
