%define plugin	ttxtsubs

Summary:	VDR plugin: Teletext subtitles
Name:		vdr-plugin-%plugin
Epoch:		1
Version:	0.3.0
Release:	1
Group:		Video
License:	GPLv2+
URL:		https://projects.vdr-developer.org/projects/plg-ttxtsubs
Source:		vdr-%plugin-%{version}.tar.gz
BuildRequires:	vdr-devel >= 1.7.6
Requires:	vdr-abi = %vdr_abi

%description
This plugin implements displaying, recording and replaying teletext
based subtitles using the on screen display.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README TROUBLESHOOTING HISTORY


