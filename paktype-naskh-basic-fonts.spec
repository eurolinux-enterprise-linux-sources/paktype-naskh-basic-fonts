%global fontname paktype-naskh-basic
%global fontconf 67-paktype-naskh-basic

Name:	%{fontname}-fonts
Version:     4.1
Release:     1%{?dist}
Summary:     Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
Group:		User Interface/X
License:     GPLv2 with exceptions
URL:		https://sourceforge.net/projects/paktype/
Source0:     http://downloads.sourceforge.net/paktype/Individual-Release/PakType-Naskh-Basic-%{version}.tar.gz
Source1:	%{fontconf}.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Requires:   fontpackages-filesystem

%description 
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Code
# get rid of the white space (' ')
mv PakType\ Naskh\ Basic.ttf PakTypeNaskhBasic.ttf
mv PakType\ Naskh\ Basic\ Features.pdf PakTypeNaskhBasicFeatures.pdf
mv PakType\ Naskh\ Basic\ License.txt  PakType_Naskh_Basic_License.txt

%{__sed} -i 's/\r//' PakType_Naskh_Basic_License.txt
chmod a-x PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf



%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeNaskhBasic.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

%_font_pkg -f %{fontconf}.conf PakTypeNaskhBasic.ttf

%doc PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf

%changelog
* Mon Apr 22 2013 Pravin Satpute <psatpute@redhat.com> - 4.1-1
- Upstream 4.1 Release

* Tue Feb 05 2013 Pravin Satpute <psatpute@redhat.com> - 4.0-2
- Upstream changed tarball

* Wed Nov 21 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-1
- Upstream 4.0 release. Now no language specific ttf

* Mon Sep 03 2012 Naveen Kumar <nkumar@redhat.com> - 3.1-1
- Upstream 3.1 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-8
- add ur-in, ur-pk & pa-pk locale-specific overrides rule in 67-paktype-naskh-basic.conf
- add ur-in, ur-pk & pa-pk locale-specific overrides rule in 67-paktype-naskh-basic-sa.conf
- resolves bug #586789

* Thu May 6 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-7
- remove binding="same" from all *.conf files

* Fri Mar 12 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-6
- Changes in summary and description

* Fri Mar 12 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-5
- changed the name of package from paktype-nashk-basic to paktype-naskh-basic

* Fri Mar 9 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-4
- removed redundant  BuildRequires from specfile
- removed unnecessary rm/rmdir's from specfile
- Sane updates in docs.

* Fri Mar 5 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-3
- removed all cd's
- changes w.r.t sed in prep section
- added .conf file for PakTypeNaskhBasic.ttf
- files section added for common
- removed space from 67-*-sindhi.conf

* Mon Feb 15 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-2
- Re-packing with updated License information.
- Changes in Spec file with new upstream source.
- Added conf files

* Mon Feb 15 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-1
- Initial packaging for version-3.0


