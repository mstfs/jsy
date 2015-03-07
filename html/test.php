<?php

/**
 * Class SegmentFault
 * Author: Tony
 * Date: 2014-01-22
 */
class SegmentFault{

private $url = 'http://www.yuanyoung.net/';

public function __get($key){
    $members = get_object_vars($this);
    foreach($members as $m){
        if(@$m[$key]){
        return $this->url;
    }
    }
    return $key . ' is not existed!';
   }
}

$sf = new SegmentFault();
echo $sf->url;