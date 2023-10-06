#!/usr/bin/perl

my $delimiter = "\t";
my $elements = "getUiBackground|getUIColor|BorderedTable";
my $line;
my @lines = ();

## injest lines of single-line code
while ($line = <STDIN>) {
  chomp $line;
  my ($left, $right) = split(/$elements/, $line);  # split the code on desired element names

## sub commas for pipes in colorFromRGB so we can split on commas
  $right =~ s/colorFromRGB\((.*?)\)/"colorFromRGB(" . replace_commas($1) . ")"/ge;

# reform the code line into an array for parsing each code line segment
  push @lines, join("\t", ($left, split(/,/, $right)));

}


## Markdown table header
print <<EOF;
| Directory | Name | Default shape | Image |
|---|:---:|:---:|---|
EOF


foreach $line (@lines) {
  my $alt_name, $dir, $name, $shape, $color = "";
  chomp $line;

  @cols = split(/$delimiter/, $line);
  ($alt_name) = $cols[0] =~ /\"(.+?)\"/;  # for no-dir fields
  ($dir,$name) = $cols[1] =~ /\"(.+\/)(.+)\"/;
  $shape = ($cols[2] =~ /\.([a-zA-Z]+)Shape/) ? $1 : "null";  # find the shape or assign null
  ($color) = "$cols[2]$cols[3]" =~ /colorFromRGB\((.*?)\)/;  # look in both fields
  $color =~ s/\|/,/g;  # transform colorFromRGB back | -> ,

## tintColor is tricky
  $color = tintColor("$cols[2]$cols[3]") if ! $color;  # might have already found the color value

  next if (! $dir && ! ($alt_name || $name));  # nothing to work with
  ($dir,$name) = ("object",$alt_name) if (! $dir && $shape);  # we'll give name the label we found in the leftmost field if no dir exists
  $shape = "null" if ! $shape;
  $color = "null" if ! $color;

  print "| $dir | $name | $shape | $color |\n" if $dir;

}


sub tintColor {
  my $line = shift @_;
  my $count_open, $count_closed, $color_text = "";

  return "" if $line !~ /tintColor/;  # no reason to continue if tintColor isn't even present

  ($color_text) = $line =~ /tintColor\s*\=\s*(.+?)\)*$/;

  $count_open = ($color_text =~ tr/(//);  # count number of '(' in the color string so we can close any strays
  $count_closed = ($color_text =~ tr/)//);  # and ')'

  $color_text .= ")" if $count_open > $count_closed;

  return $color_text;

}


sub replace_commas {
    my ($str) = @_;
    $str =~ s/\,/\|/g;
    return $str;
}



