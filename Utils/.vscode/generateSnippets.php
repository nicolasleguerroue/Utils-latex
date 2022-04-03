<?php 


$folder="Utils";
$items = scandir($folder); 			//Get all directories
$files = array();

$globalArray = array();

$regex_number="|}\[\d\]|";
$regex_get_number="|\d|";
$regex_name_command="|{.*?}|";



$regex_renew_command="|renewcommand|";
$regex_new_command="|newcommand|";
$regex_new_env="|newenvironment|";
$regex_new_cbox="|newtcbox|";
$regex_new_theorem="|newtheorem|";

$count=0;


$file_ = fopen(".vscode/output.code-snippets", "w");
fputs($file_, "{\n");

function sortCommand($string) {
    $return =  str_replace("{", "\\" , str_replace("}", "" , $string));
    return $return;
}
function sortTheorem($string) {
    $return =  str_replace("{", "\\" , str_replace("}", "" , $string));
    return $string;
}
function sortSlashCommand($string) {
    $return =  str_replace("{", "" , str_replace("}", "" , $string));
    return $return;
}
function clean($string) {
    $return =  str_replace("\\", "" , str_replace("{", "" , str_replace("}", "" , $string)));
    return $return;
}
function sortEnv($string) {
    $return =  str_replace("{", "" , str_replace("}", "" , $string));
    return $return;
}
function sortSlashEnv($string) {
    $return =  str_replace("{", "" , str_replace("}", "" , $string));
    return $return;
}

function extractLine($string, $target, $index) {

    if(strpos($string, $target) !== FALSE) { //if line is found

        $output=explode($target,$string); //get element

        if($output[$index]=="") { 	
            return "";
        }//End if
        else {
            return $output[$index];
        }//End else

    }//End if
}

function addInput($line, $name, $type, &$array, $anyArg=False) {

    $returnArray=array();

    $description=extractLine($line, "%", 1);
    if($description=="") {return "";}

    $description=extractLine($description, "#", 0);

    $args=extractLine($line, "#", 1);

    $argArray = array();


    if($args=="") {

        if($anyArg==True) {
        }
    }
    else {
        $argArray  = explode(" ", $args);
    }

    array_push($returnArray, $name);
    array_push($returnArray, $type);
    array_push($returnArray, $description);
    array_push($returnArray, $argArray);

    array_push($array, $returnArray);
}

		
for($i=0;$i<count($items);$i++){
	

    //echo $folder."/".$items[$i]."\n";
    if (is_file($folder."/".$items[$i])==True) { 

        $file = file($folder."/".$items[$i]);
        //echo sizeof($file);

        for($a = 0; $a < count($file); $a++) {  

            $line=$file[$a]; 
            preg_match($regex_number, $line, $match); //Check if command with arg

            if(sizeof($match)>0) { 

                //echo ">>>".$line."";

                //check types
                preg_match($regex_new_command, $line, $match_new_command);
                preg_match($regex_renew_command, $line, $match_renew_command);
                preg_match($regex_new_env, $line, $match_new_env);
                preg_match($regex_new_cbox, $line, $match_new_cbox);
                preg_match($regex_new_theorem, $line, $match_new_theorem);

                if(sizeof($match_renew_command)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    if(sizeof($match_name_command)==0) {continue;}
                    preg_match($regex_get_number, $line, $match_number);
                    
                    $commandName=clean($match_name_command[0]);
                    echo "Renew command [$commandName] with ".$match_number[0]." args \n";
                    addInput($line, $commandName, "command", $globalArray);

                }

                elseif(sizeof($match_new_command)) {
                    
                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    if(sizeof($match_name_command)==0) {continue;}
                    preg_match($regex_get_number, $line, $match_number);
                    $commandName=clean($match_name_command[0]);
                    addInput($line, $commandName, "command", $globalArray);
                    echo "New command [$commandName] with ".$match_number[0]." args \n";

                }

                elseif(sizeof($match_new_env)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_env);
                    if(sizeof($match_name_env)==0) {continue;}
                    $envName=clean($match_name_env[0]);
                    preg_match($regex_get_number, $line, $match_number);
                    echo "New env [$envName] with ".$match_number[0]." args\n";
                    addInput($line, $envName, "env", $globalArray);
                }

                elseif(sizeof($match_new_cbox)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_cbox);
                    if(sizeof($match_name_cbox)==0) {continue;}
                    $cboxName=clean($match_name_cbox[0]);
                    preg_match($regex_get_number, $line, $match_number);
                    echo "New cbox [$cboxName] with ".$match_number[0]." args\n";
                    addInput($line, $cboxName, "env", $globalArray);
                
                }
                elseif(sizeof($match_new_theorem)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_theorem);
                    if(sizeof($match_name_theorem)==0) {continue;}
                    $theoremName=clean($match_name_theorem[0]);
                    preg_match($regex_get_number, $line, $match_number);
                    echo "New theorem [$theoremName] with ".$match_number[0]." args\n";
                    addInput($line, $theoremName, "env", $globalArray);
                
                }
            } 

            else {
                //try to check if another simple command
                //check types
                preg_match($regex_new_command, $line, $match_new_command);
                preg_match($regex_renew_command, $line, $match_renew_command);
                preg_match($regex_new_env, $line, $match_new_env);
                preg_match($regex_new_cbox, $line, $match_new_cbox);
                preg_match($regex_new_theorem, $line, $match_new_theorem);

                if(sizeof($match_renew_command)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    if(sizeof($match_name_command)==0) {continue;}
                    echo "Renew command [$commandName] with any arg \n";
                    $commandName=clean($match_name_command[0]);
                    addInput($line, $commandName, "command", $globalArray, True);
                }

                elseif(sizeof($match_new_command)) {
                    
                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    $commandName=clean($match_name_command[0]);
                    echo "New command [$commandName] with any arg \n";
                    addInput($line, $commandName, "command", $globalArray, True);
                }

                elseif(sizeof($match_new_env)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    $envName=clean($match_name_command[0]);
                    echo "New env [$envName] with any arg \n";
                    addInput($line, $envName, "env", $globalArray, True);
                }
                elseif(sizeof($match_new_cbox)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    $cboxName=clean($match_name_command[0]);
                    echo "New cbox [$cboxName] with any arg \n";
                    addInput($line, $cboxName, "cbox", $globalArray, True);
                }
                elseif(sizeof($match_new_theorem)) {

                    $count++;
                    preg_match($regex_name_command, $line, $match_name_command);
                    $theoremName=clean($match_name_command[0]);
                    echo "New theorem [$theoremName] with any arg \n";
                    addInput($line, $theoremName, "theorem", $globalArray, True);
                }
            }
        }	

	 }//End if


}//End for



$content = "";

for ($item=0; $item < sizeof($globalArray); $item++) { 
    echo ">>> Generating '".$globalArray[$item][0]."' command \n";
    $content .= "\t\t\"".''.$globalArray[$item][2].'": { 
        '."\t".'"scope": "tex, latex",
        '."\t".'"prefix": "\\\\'.$globalArray[$item][0].'",
        '."\t".'"body": ['."\n";
        $tmp_content="";
        if(sizeof($globalArray[$item][3])==0) {
            $tmp_content="\"\\\\".$globalArray[$item][0]."\"";
        }
        else {

            if($globalArray[$item][1]=="theorem") {

                $tmp_content .= "\t\t\t\"\\\begin{".$globalArray[$item][0]."}".'\n${1:content'.'}\n'."\\\\end{".$globalArray[$item][0]."}";
                $tmp_content .= "\"\n\t\t\t],\n";
                $tmp_content .= "\t\t".'"description": "'.$globalArray[$item][2].'"},'."\n";

            }
            else {
                $tmp_content .= "\t\t\t\"\\\\".$globalArray[$item][0];
                for ($i=0; $i < sizeof($globalArray[$item][3]); $i++) { 
                    $tmp_content .= '{${'.($i+1).':'.trim($globalArray[$item][3][$i]).'}}';
                }
                $tmp_content .= "\"\n\t\t\t],\n";
                $tmp_content .= "\t\t".'"description": "'.$globalArray[$item][2].'"},'."\n";
            }
        }
        //echo $tmp_content."\n";
        $content .= $tmp_content;

}
//print_r($globalArray);
echo ">>> items found : $count\n";
fputs($file_, $content);
fputs($file_, "}\n");

fclose($file_);	

?>