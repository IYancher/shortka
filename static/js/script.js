function myFunction() {

  var copyText = document.getElementById("myInput");

  copyText.select();

  document.execCommand("copy");

  alert("Short URL has been copied");
}