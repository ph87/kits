<!--
http://v2ex.com/t/82318
要求:
写一个php程序, 遍历目录中的 html 文件 (不限制扩展名最好); 
将其中的 class="xxx" 或 class="xxx xxx" 等用随机字符替换;
替换的同时, 生成一个可还原的 php 文件,可将被替换的 html 文件中运行还原!
-->
<?php
	$file_st = glob("*.html");
	$map = [];
	foreach($file_list as $file){
		$file_content = file_get_contents($file);
		preg_match_all('/class\s*=\s*\"(.*?)\"/',
			$file_content, $match_result,
			PREG_SET_ORDER
			);
		if($match_result){
			$encrypt_str = [];
			$encrypt_class_str = [];
			foreach($match_result as $k=>$v){
				$original_class_str[] = $v[0];
				$encrypt_class_str[] = str_replace($v[1], md5($v[1]), $v[0]);
			}
			$map[$file] = array(
				'original_class_str' => $original_class_str,
				'encrypt_class_str' => $encrypt_class_str,
			);
			$processed = str_replace($original_class_str, $encrypt_class_str, $file_content);
			file_put_contents($file, $processed);
		}
	}
	file_put_contents('map.file', serialize($map));
?>

解析：
<?php
	$map = unserialize(file_get_contents('map.file'));
	foreach($map as $file_name=>$map_array){
		$file_content = file_get_contents($file_name);
		$content = str_replace($map_array['encrypt_class_str'],
			$map_array['original_class_str'],
			$file_content);
		file_put_contents($file_name, $content);
	}
?>
