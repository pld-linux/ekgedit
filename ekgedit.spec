Summary:	Program to edit ekg user list
Summary(pl):	Program do edycji list znajomych z ekg
Name:		ekgedit
Version:	0.0.1
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://otak.k-k.pl/%{name}/%{name}-sources/%{name}-%{version}.tar.gz
# Source0-md5:	3e58f3520584ac1a6184fb96ccfc6933
URL:		http://otak.k-k.pl/ekgedit/
Requires:	ekg
Requires:	otak
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Program to edit user list from ekg.

%description -l pl
Program do edycji listy znajomych z ekg.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTFIR=$RPM_BUILD_ROOT # typo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-pl NEWS
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/otak/*
