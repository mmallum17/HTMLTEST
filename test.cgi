#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings;
use Mail::Sendmail;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;

print header(), start_html();

my $mailTo      =  param('to');
my $mailFrom    =  param('from');
my $subjectLine =  param('subject');
my $message     =  param('message');
my %mail = ( To      => $mailTo,
    From    => $mailFrom,
    Subject => $subjectLine,
    Message => $message,
    'Content-Type' => 'text/plain');

if ( sendmail %mail )
{
    print "Congratulations, we have sent e-mail to $mailTo from $mailFrom!";
}
else
{
    print "You need a valid from address.";
    print "You need a valid to address.";
    print "You need to enter a subject";
    print "You need to enter a message";
    print a(
            { -href => "javascript:history.back()"},
            "Go back and fill in everything"
        );
}
print end_html;

