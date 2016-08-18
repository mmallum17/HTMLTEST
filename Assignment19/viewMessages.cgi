#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;

print header(), start_html();


open FILE, "<messages.txt" or die $!;
while(<FILE>)
{
    print h1("$_");
    print p("$_");
}
close FILE;

print a(
        { -href => "javascript:history.back()"},
        "Back to website"
    );
print end_html;