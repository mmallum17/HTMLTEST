#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings FATAL => 'all';

say "";
say "Welcome to the Perl Whole Number Guessing Game!";
say "Please enter a number between 1 and 100 and I will tell you if the number you're trying to guess is higher or lower than your guess.";
say "";

my $target = (int rand 100) + 1;
my @attempts;
my $input = -1;
$" = ", ";

while($input != $target)
{
    print "Enter guess #" . ($#attempts + 2) . ": ";
    chomp($input = <>);
    push (@attempts, $input);
    if($input ~~ $target)
    {
        say "";
        say "You guessed the secret number ($target) in " . ($#attempts + 1) . " tries!";
        print "Here were your guesses: ";
        for (my $position = 0; $position < @attempts - 1; $position++)
        {
            print "$attempts[$position], ";
        }
        say "and $attempts[$#attempts]";
    }
    else
    {
        if($input < 1 || $input > 100)
        {
            say "Your guess of $input is out of range and will not be recorded. Try again.";
            pop(@attempts);
        }
        elsif($input > $target)
        {
            say "Your guess of $input is too high. Try lower next time.";
        }
        else
        {
            say "Your guess of $input is too low. Try higher next time.";
        }
        say "";
        print "Your guesses so far: @attempts\n"
    }
}
say "";