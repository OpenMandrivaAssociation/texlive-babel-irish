%global tl_name babel-irish
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0h
Release:	%{tl_revision}.1
Summary:	Babel support for Irish
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/irish
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-irish.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of Irish
Gaelic in babel. The principal content is translations to Irish of
standard "LaTeX names". (No shortcuts are defined.)

