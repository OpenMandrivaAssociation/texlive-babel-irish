Name:		texlive-babel-irish
Version:	30277
Release:	1
Summary:	TeXLive babel-irish package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.r30277.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.doc.r30277.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.source.r30277.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-irish package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-irish/irish.ldf
%doc %{_texmfdistdir}/doc/generic/babel-irish/irish.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-irish/irish.dtx
%doc %{_texmfdistdir}/source/generic/babel-irish/irish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
