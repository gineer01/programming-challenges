#Script to get data from Perforce about files in directory
use warnings;
use strict;

my $fileHandle;
open $fileHandle, '>outputI.txt';

while (<>){
	my $result = `p4 describe -s $_`;
	print $fileHandle $result;
	print $fileHandle "========================================\n"
}