
%define plugin	ttxtsubs
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define edition	rre
%define edlong	raastinrauta
%define rel	4

%define release %mkrel 10.%edition.%rel

Summary:	VDR plugin: Teletext subtitles
Name:		%name
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
