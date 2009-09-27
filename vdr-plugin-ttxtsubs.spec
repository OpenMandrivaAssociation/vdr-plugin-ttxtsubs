
%define plugin	ttxtsubs
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	1

%define release %mkrel %rel

Summary:	VDR plugin: Teletext subtitles
Name:		%name
Version:	%version
Release:	%release
Group:		Video
License:	GPLv2+
URL:		http://projects.vdr-developer.org/wiki/plg-ttxtsubs
Source:		http://projects.vdr-developer.org/attachments/download/vdr-%plugin-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin implements displaying, recording and replaying teletext
based subtitles using the on screen display.

%prep
%setup -q -n %plugin-%version
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
