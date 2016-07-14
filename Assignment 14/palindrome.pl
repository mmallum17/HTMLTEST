#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings FATAL => 'all';

my $string;
my $first;
my $second;
my $third;
my $fourth;
my $fifth;
my $sixth;
my $seventh;

say "";
print 'Enter in a 7 character item: ';
chomp($string = <>);

$first = chop $string;
$second = chop $string;
$third = chop $string;
$fourth = chop $string;
$fifth = chop $string;
$sixth = chop $string;
$seventh = chop $string;

if($first ~~ $seventh && $second ~~ $sixth && $third ~~ $fifth)
{
    print "PALINDROME!\n";
}
else
{
    print "NOT A PALINDROME\n";
}
say "";