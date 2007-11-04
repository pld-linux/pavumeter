Summary:	PulseAudio Volume Meter
Summary(pl.UTF-8):	PulseAudio Volume Meter - pomiar głośności PulseAudio
Name:		pavumeter
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/pavumeter/%{name}-%{version}.tar.gz
# Source0-md5:	3a6b36cfefa8d6dd00084dafa50c934c
Patch0:		%{name}-desktop.patch
URL:		http://0pointer.de/lennart/projects/pavumeter/
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.7
Requires:	pulseaudio-libs >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Volume Meter (pavumeter) is a simple GTK+ volume meter for
the PulseAudio sound server.

%description -l pl.UTF-8
PulseAudio Volume Meter (pavumeter) to prosta aplikacja GTK+ do
pomiaru głośności dla serwera dźwięku PulseAudio.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/pavumeter
%{_desktopdir}/pavumeter.desktop
%{_desktopdir}/pavumeter-record.desktop
