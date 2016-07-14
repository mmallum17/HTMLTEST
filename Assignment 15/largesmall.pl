#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings FATAL => 'all';

my $input;
my $large;
my $small;
my $average;
my $sum = 0;
my $count = 0;

say "";
print("Please enter a number(neg value to end): ");
chomp($input = <>);

while ($input >= 0)
{
    $sum += $input;
    if($count == 0)
    {
        $large = $input;
        $small = $input;
    }
    if($input > $large)
    {
        $large = $input;
    }
    if($input < $small)
    {
        $small = $input;
    }
    $count++;
    print("Please enter a number(neg value to end): ");
    chomp($input = <>);
}

if($count == 0)
{
    print "NO NUMBERS ENTERED\n";
}
else
{
    $average = $sum / $count;
    print "$large:$small:$average\n";
}
say "";