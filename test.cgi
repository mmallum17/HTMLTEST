#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;

print header(), start_html();
my @thing    = param('movie'); # could be a list!
$" = ", ";
if ( !@thing ) {
    print p( "No movies were selected!" );
}
else {
    print p("The movie(s) were @thing");
}


print end_html;

