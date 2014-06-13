# revision 15878
# category Package
# catalog-ctan /language/sanskrit
# catalog-date 2007-01-14 10:43:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-sanskrit
Version:	20070114
Release:	7
Summary:	Sanskrit support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/sanskrit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit.source.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/sanskrit/skt.map
%{_texmfdistdir}/fonts/source/public/sanskrit/skt10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skt8.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skt9.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktb10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktbs10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktchars.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktdefs.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktf10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktfs10.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/sktligs.mf
%{_texmfdistdir}/fonts/source/public/sanskrit/skts10.mf
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt8.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skt9.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktb10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktf10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/sktfs10.tfm
%{_texmfdistdir}/fonts/tfm/public/sanskrit/skts10.tfm
%{_texmfdistdir}/fonts/type1/public/sanskrit/skt10.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/skt8.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/skt9.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/sktb10.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/sktbs10.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/sktf10.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/sktfs10.pfb
%{_texmfdistdir}/fonts/type1/public/sanskrit/skts10.pfb
%{_texmfdistdir}/tex/latex/sanskrit/ot1skt.fd
%{_texmfdistdir}/tex/latex/sanskrit/skt.sty
%doc %{_texmfdistdir}/doc/latex/sanskrit/readme.txt
%doc %{_texmfdistdir}/doc/latex/sanskrit/sktdoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sanskrit/skt.c
%doc %{_texmfdistdir}/source/latex/sanskrit/sktdoc.skt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070114-2
+ Revision: 755786
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070114-1
+ Revision: 719478
- texlive-sanskrit
- texlive-sanskrit
- texlive-sanskrit
- texlive-sanskrit

