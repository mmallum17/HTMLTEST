#!/usr/bin/perl
use Modern::Perl;
use Mail::Sendmail;  # required to use the Mail::Sendmail library
# use your address here instead of me@somewhere.com for testing purposes!
my $mailTo      =  'marcusmallum@gmail.com';   # in your CGI, this will be val of param()
# use your address here instead of me@nowhere.com for testing
my $mailFrom    =       'marcusmallum@gmail.com'; # in your CGI, this will be val of param()
my $subjectLine =       "Sample Subject"; # in your CGI, this will be val of param()
my $message     =       "Sample Message!"; # in your CGI, this will be val of param()
my %mail = ( To      => $mailTo,
            From    => $mailFrom,
            Subject => $subjectLine,
            Message => $message,   # must be a string, not an array
    'Content-Type' => 'text/plain'
            );
if ( sendmail %mail )
{
    print "Successfully sent mail to $mailTo.  Check your box!\n";
}
else
{
    print "Error sending mail: $Mail::Sendmail::error \n";
}