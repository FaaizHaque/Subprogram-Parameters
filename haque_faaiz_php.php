<?php

function func1( $a, $b ) #Parameter correspondence
{
     $result = $a - $b;
     print "In func1 result: $result\n";
}

func1(10,5); #Positional
func1($b=10,$a=5); #Keyword

function func2($a = 10, $b = 5) #Default values
{
	$result = $a - $b;
	print "In func2 result: $result\n";
}

func2(); #Default values used
func2(5);


function func3($a, $b ) #Pass by return
{
	$result = $a - $b;
	return $result;
}
$result = func3(3,2);
print "After func3 call result: $result\n";

function func4($x) #Pass by value
{
	$x = 10;
	print "x in func4: $x \n";
}
$x = 5;
func4($x);
print "x after func4 call: $x \n";

function func5(&$x) #Pass by reference
{
	$x = 10;
	print "x in func5: $x \n";
}
$x = 5;
func5($x);
print "x after func5 call: $x \n";

function func6() #Variable Number Of Actual Parameters
{
	var_dump(func_num_args());
	var_dump(func_get_args());
}
$array = array(5, hello, cat );
call_user_func_array('func6',$array);

?>


