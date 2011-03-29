# Generated from spruz-0.2.5.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	spruz

Summary:	Useful stuff
Name:		rubygem-%{rbname}

Version:	0.2.5
Release:	1
Group:		Development/Ruby
License:	BSD
URL:		http://flori.github.com/spruz
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
All the stuff that isn't good/big enough for a real library.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f tests

%install
%gem_install

%files
%doc LICENSE
%{_bindir}/enum
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/enum
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spruz
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spruz/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spruz/xt
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spruz/xt/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*.rb

