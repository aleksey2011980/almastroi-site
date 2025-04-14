<?php
$token = "7001009647:AAE9rV84I7zD81b3C2Zs4DBHwgpwZe2eW3k";
$chat_id = $_GET['chat_id'];
$text = $_GET['text'];

$sendToTelegram = fopen("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$text","r");

if ($sendToTelegram) {
  http_response_code(200);
  echo "OK";
} else {
  http_response_code(500);
  echo "ERROR";
}
?>
