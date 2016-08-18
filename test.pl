#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings FATAL => 'all';

my $str = "TEST\n";
open FILE, ">>file.txt" or die $!;
print FILE $str;
close FILE;

open FILE, "<file.txt" or die $!;
while(<FILE>)
{
    print $_;
}
close FILE;