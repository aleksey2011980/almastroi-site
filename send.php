<?php
$chat_id = $_GET['chat_id'] ?? '';
$text = $_GET['text'] ?? '';

$token = "7001009647:AAE9rV84I7zD81b3C2Zs4DBHwgpwZe2eW3k";

$url = "https://api.telegram.org/bot$token/sendMessage";

$response = file_get_contents($url . "?chat_id=" . urlencode($chat_id) . "&text=" . urlencode($text));

echo json_encode(["ok" => true, "response" => $response]);
?>