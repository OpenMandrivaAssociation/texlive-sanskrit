Name:		texlive-sanskrit
Version:	64502
Release:	1
Summary:	Sanskrit support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/sanskrit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A font and pre-processor suitable for the production of
documents written in Sanskrit. Type 1 versions of the fonts are
available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/sanskrit
%{_texmfdistdir}/fonts/tfm/public/sanskrit
%{_texmfdistdir}/tex/latex/sanskrit
%doc %{_texmfdistdir}/doc/latex/sanskrit
#- source
%doc %{_texmfdistdir}/source/latex/sanskrit

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
