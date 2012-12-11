
%define plugin	ttxtsubs
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define edition	rre
%define edlong	raastinrauta
%define rel	5

%define release %mkrel 10.%edition.%rel

Summary:	VDR plugin: Teletext subtitles
Name:		%name
Epoch:		1
Version:	%version
Release:	%release
Group:		Video
License:	GPL+
URL:		ftp://ftp.nada.kth.se/pub/home/ragge/vdr/
Source:		ftp://ftp.nada.kth.se/pub/home/ragge/vdr/vdr-%plugin-%version.tar.bz2
# http://www.saunalahti.fi/~rahrenbe/vdr/patches/
Patch1:		vdr-ttxtsubs-0.0.5-%edlong-edition.diff
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin implements displaying, recording and replaying teletext
based subtitles using the on screen display.

This is the %edlong edition, currently maintained by Rolf
Ahrenberg.

%prep
%setup -q -n %plugin-%version
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README TROUBLESHOOTING HISTORY


%changelog
* Thu Mar 04 2010 Anssi Hannula <anssi@mandriva.org> 1:0.0.5-10.rre.5mdv2010.1
+ Revision: 514149
- revert back to 0.0.5 raastinrauta edition as 0.1.0 is incompatible
  with VDR 1.6 (fixes playback of recorded teletext subtitles; reported
  by Marko on mandriva-fi.org forum)

* Sun Sep 27 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2010.0
+ Revision: 450019
- new version by new upstream
- update URL and License
- drop Rolf Ahrenberg's raastinrauta-edition patch, applied upstream

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.rre.4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.rre.3mdv2009.1
+ Revision: 359378
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.rre.2mdv2009.0
+ Revision: 197990
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.rre.1mdv2009.0
+ Revision: 197736
- raastinrauta edition
- apply new license policy
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.6mdv2008.1
+ Revision: 145233
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.5mdv2008.1
+ Revision: 103225
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.4mdv2008.0
+ Revision: 50059
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.3mdv2008.0
+ Revision: 42142
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.2mdv2008.0
+ Revision: 22716
- rebuild for new vdr

* Fri Apr 20 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10.kne.1mdv
+ Revision: 16314
- kermanekka edition


* Sat Jan 20 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-9.pme.1mdv2007.0
+ Revision: 111095
- pippurimylly edition

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-9mdv2007.1
+ Revision: 90980
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-8mdv2007.1
+ Revision: 74095
- rebuild for new vdr
- Import vdr-plugin-ttxtsubs

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2007.0
- rebuild for new vdr

* Sun Jun 04 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2007.0
- initial Mandriva release

