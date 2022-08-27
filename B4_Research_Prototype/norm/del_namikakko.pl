#!/usr/bin/perl

while (<>) {
  chomp;
  if (/^(\w+)(?:\s+(#\w+))?\s+<(.*)>$/) {
		my ($t, $i, $s) = ($1, $2, $3);
			
    #"{"を削除する
    if ($t eq "C_L") {
      $s =~ s/{//g;
    }

    #"}"を削除する
    if ($t eq "C_R") {
      $s =~ s/}//g;
    }

	# "$t $i <$s>\n" を表示する．
		print "$t $i <$s>\n";
  }
}
