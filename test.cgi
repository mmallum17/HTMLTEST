#!/usr/bin/perl

use CGI qw/:standard/;
use Modern::Perl;
print header();
print start_html( -title=>'Page Generated with CGI.pm!' );
print h1( 'Hey look, this is a heading!' );
print 'More body text goes here.';
print end_html();

