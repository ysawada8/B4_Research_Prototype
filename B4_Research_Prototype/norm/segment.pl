#!/usr/bin/perl

while (<>) {
  chomp;
  if (/^(\w+)(?:\s+(#\w+))?\s+<(.*)>$/) {
		my ($t, $i, $s) = ($1, $2, $3);
			
    #余計な改行を削除する
    if ($t eq "SP_NL") {
      $s =~ s/.+//g;
    }
    #余計な空行を削除する
    if ($t eq "SP_B") {
      $s =~ s/  +//g;
    }
			
    #改行１つ目
    if ($t eq "C_L") {  #"{"の後に改行を入れる
        $s =~ s/{/{\\n/g;
    }
    if ($t eq "C_R") {  #"}"の後に改行を入れる
        $s =~ s/}/}\\n/g;
    }

    #改行２つめ
    if ($t eq "CT_IF") {  #"if"の前に改行を入れる
        $s =~ s/if/\\nif/g;
    }
    if ($t eq "CT_BE") {  #"for", "while"の前に改行を入れる
        $s =~ s/for/\\nfor/g;
        $s =~ s/while/\\nwhile/g;
    }
    if ($t eq "CT_DO") {  #"do"の前に改行を入れる
        $s =~ s/do/\\ndo/g;
    }

	# "$t $i <$s>\n" を表示する．
		print "$t $i <$s>\n";
  }
}
