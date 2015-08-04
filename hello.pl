use strict;
use warnings;
use LWP::Simple;
sub main{
	print "Hello\n";
	print "Downloading ... \n";
	print get("http://www.caveofprogramming.com/");
}

main()
