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

if ( (sendmail %mail) && !($subjectLine ~~ /^\s*$/) && !($message ~~ /^\s*$/))
{
    print p("Congratulations, we have sent e-mail to $mailTo from $mailFrom!");
    print a(
            { -href => "javascript:history.back()"},
            "Back to website"
        );
}
else
{
    if(!($mailFrom ~~ /.+\@.+\..+/))
    {
        print p({-style => "color: red"},"You need a valid from address.");
    }
    if(!($mailTo ~~  /.+\@.+\..+/))
    {
        print p({-style => "color: red"}, "You need a valid to address.");
    }
    if($subjectLine ~~ /^\s*$/)
    {
        print p({-style => "color: red"}, "You need to enter a subject.");
    }
    if($message ~~ /^\s*$/)
    {
        print p({-style => "color: red"}, "You need to enter a message");
    }
    print a(
            { -href => "javascript:history.back()"},
            "Go back and fix your errors"
        );
}
print end_html;

