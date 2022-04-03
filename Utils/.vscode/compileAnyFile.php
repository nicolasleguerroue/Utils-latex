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


$folder="../Parts";
$items = scandir($folder); 			//Get all directories
$files = array();

		
for($i=0;$i<count($items);$i++){
	
    
    
    if($items[$i]!="." || $items[$i]!=".") {

		echo "No compiling of ".$folder."/".$items[$i]." folder \n";

        if( $items[$i][0]!=".")  { //rename
            $newName = ".".strval($items[$i]);
            rename($folder."/".$items[$i], $folder."/".$newName);
        }
    }


}//End for




?>