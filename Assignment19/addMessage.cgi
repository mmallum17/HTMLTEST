#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;

print header(), start_html();

my $name = param('name');
my $message = param('message');

open (FILE, ">>messages.txt") or die $!;
print FILE $name."\n";
print FILE $message."\n";
close FILE;

print p("Congratulations, $name. We have received your message!");
print a(
        { -href => "javascript:history.back()"},
        "Back to website"
        );
print end_html;