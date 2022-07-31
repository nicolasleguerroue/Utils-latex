<?php 


function extractLine($string, $target, $index=1) { //Extract item in line #'string' 'target' $indexFromTarget

	if(strpos($string, $target) !== FALSE) { //if line is found

		$output=explode($target,$string); //get element

		if($output[$index]=="") { 	
			return "";
		}//End if
		else {
			return $output[$index];
		}//End else

	}//End if

}//End extractLine

echo ">>>> INIT -> ".strval(getcwd())."\n";
$folder="../Parts";
$items = scandir($folder); 			//Get all directories
$files = array();
echo ">>>> LAST -> \n";
print_r($items);

		
for($i=0;$i<count($items);$i++){
    
    if($items[$i]!="." || $items[$i]!=".") {

		echo "Compiling of ".$folder."/".$items[$i]." folder \n";

        if( $items[$i][0]==".")  { //rename
            $number = extractLine($items[$i], ".", 1);
			$name = extractLine($items[$i], ".", 2);
			$newName=$number.".".$name;
            rename($folder."/".$items[$i], $folder."/".$newName);
        }
    }


}//End for




?>