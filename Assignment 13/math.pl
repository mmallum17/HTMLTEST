#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings FATAL => 'all';

my $firstNumber;
my $secondNumber;
my $thirdNumber;

print 'Enter first number: ';
chomp($firstNumber = <>);
print "Enter second number: ";
chomp($secondNumber = <>);
print "Enter third number: ";
chomp($thirdNumber = <>);

print "SUM: " . ($firstNumber + $secondNumber + $thirdNumber) . "\n";
print "MUL: " . ($firstNumber * $secondNumber * $thirdNumber) . "\n";
print "DIV: " . ($firstNumber / $thirdNumber) . "\n";
print "MOD: " . ($firstNumber % $secondNumber) . "\n";
print "DIF: " . ($firstNumber - $secondNumber) . "\n";

if($firstNumber > $secondNumber)
{
    print "LRG: " . $firstNumber . "\n";
}
else
{
    print "LRG: " . $secondNumber . "\n";
}

if($secondNumber < $thirdNumber)
{
    print "SML: " . $secondNumber . "\n";
}
else
{
    print "SML: " . $thirdNumber . "\n";
}