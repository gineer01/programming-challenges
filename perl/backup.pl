#!/usr/bin/perl
use strict;

#Get passwords from command line argument to perl script
my $mainPw = $ARGV[0];
my $backupPw = $ARGV[1];




sub runCommand{
	my ($command) = @_;
	print "Exec command: $command \n";
	system $command;

	if ($? == -1) {
    	print "failed to execute: $!\n";
    }
    elsif ($? & 127) {
    	printf "child died with signal %d, %s coredump\n",
    		($? & 127), ($? & 128) ? 'with' : 'without';
    }
    else {
    	printf "child exited with value %d\n", $? >> 8;
    }
}



sub mount{
	my ($path, $password, $volume) = @_;
	#print "Args: $path $password $volume \n";
	my $command = "/Applications/TrueCrypt.app/Contents/MacOS/TrueCrypt -t -k \"\" --protect-hidden=no --mount $path $volume -p=\"$password\" ";

	if (!(-f $path)) {
		print "Cannot find main copy at $path \n";
		return;
	}

	print "mounting volume at \'$path\' \n";
	runCommand($command);
}



my $mainPath = '../Private/Secure/Temp';
my $mainVolume = '/Volumes/MAIN';
print "\n\n == mounting main copy at \'$mainPath\' ==\n";
mount($mainPath, $mainPw, $mainVolume);

print "Please export LastPass to TrueCrypt drive \n";
print "Press enter to continue with rsync...";
my $input = <STDIN>;

my $backupPath = 'TempBackup';
my $backupVolume = '/Volumes/BACKUP';
print "\n\n == mounting backup copy at \'$backupPath\' ==\n";
mount($backupPath, $backupPw, $backupVolume);

my $command = "rsync -avvu --delete --progress $mainVolume/ $backupVolume/TempBackup/";
print "\n\n == rsync from main to backup == \n";
runCommand($command);

printf "\n\n == Dismount all volumes ==\n";
print "Press enter to dismount all...";
my $input = <STDIN>;
runCommand("/Applications/TrueCrypt.app/Contents/MacOS/TrueCrypt -t -d");
