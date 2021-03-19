%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:           thunarx-python
Version:        0.5.2
Release:        1
License:        GPLv2+
Summary:        Python Bindings for the Thunar Extension Framework
Url:            https://goodies.xfce.org/projects/bindings/thunarx-python
Group:          Development/Python
Source:         https://archive.xfce.org/src/bindings/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(thunarx-3)
BuildRequires:  pkgconfig(python)
Requires:       thunar
Requires:       python3dist(pygobject)
Requires:       typelib(Thunarx)

%description
This package provides the Python bindings for the Thunar Extension framework
which allow one to create Python plugins for Thunar.

%prep
%autosetup -p1

%build
export PYTHON=%{__python}
export PYTHON_LIBS=-lpython%{python_version}
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_libdir}/thunarx-3/python/

find %{buildroot} -name "*.la" -delete

install -Dpm644 examples/README %{buildroot}%{_docdir}/%{name}/examples/README

%files
%license COPYING
%doc README ChangeLog AUTHORS
%doc %{_docdir}/%{name}/examples/
%doc %{_datadir}/gtk-doc/html/%{name}/
%dir %{_libdir}/thunarx-3/python/
%{_libdir}/thunarx-3/thunarx-python.so
