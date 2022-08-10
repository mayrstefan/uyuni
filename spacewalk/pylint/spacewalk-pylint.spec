#
# spec file for package spacewalk-pylint
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2008-2018 Red Hat, Inc.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           spacewalk-pylint
Version:        4.4.0
Release:        0
Summary:        Pylint configuration for spacewalk python packages
License:        GPL-2.0-only
Group:          Development/Debuggers

URL:            https://github.com/uyuni-project/uyuni
Source0:        https://github.com/spacewalkproject/spacewalk/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?suse_version} >= 1320
Requires:       pylint > 1.1
%else
%if 0%{?fedora} || 0%{?rhel} >= 7
%if 0%{?fedora} >= 26
Requires:       python2-pylint > 1.5
%else
Requires:       pylint > 1.5
%endif
%else
Requires:       pylint < 1.0
%endif
%endif
BuildRequires:  asciidoc
BuildRequires:  libxslt
%if 0%{?rhel} && 0%{?rhel} < 6
BuildRequires:  docbook-style-xsl
%endif

%description
Pylint configuration fine tuned to check coding style of spacewalk python
packages.

%prep
%setup -q

%build
a2x -d manpage -f manpage spacewalk-pylint.8.asciidoc

%install
install -d -m 755 %{buildroot}/%{_bindir}
install -p -m 755 spacewalk-pylint %{buildroot}/%{_bindir}/
install -d -m 755 %{buildroot}/%{_sysconfdir}
install -p -m 644 spacewalk-pylint.rc %{buildroot}/%{_sysconfdir}/
%if 0%{?rhel} && 0%{?rhel} < 7
# new checks in pylint 1.1
sed -i '/disable=/ s/,bad-whitespace,unpacking-non-sequence,superfluous-parens,cyclic-import//g;' \
        %{buildroot}%{_sysconfdir}/spacewalk-pylint.rc
# new checks in pylint 1.0
sed -i '/disable=/ s/,C1001,W0121,useless-else-on-loop//g;' \
        %{buildroot}%{_sysconfdir}/spacewalk-pylint.rc
%endif
%if 0%{?suse_version}
# new checks in pylint 1.2
sed -i '/disable=/ s/,bad-continuation//g;' \
        %{buildroot}%{_sysconfdir}/spacewalk-pylint.rc
%endif
mkdir -p %{buildroot}/%{_mandir}/man8
install -m 644 spacewalk-pylint.8 %{buildroot}/%{_mandir}/man8

%files
%defattr(-,root,root,-)
%{_bindir}/spacewalk-pylint
%config(noreplace)  %{_sysconfdir}/spacewalk-pylint.rc
%doc %{_mandir}/man8/spacewalk-pylint.8*
%{!?_licensedir:%global license %doc}
%license LICENSE

%changelog
