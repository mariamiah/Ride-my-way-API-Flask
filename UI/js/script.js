<script>
function initPage() {
    var headingText=document.getElementById('pageheading');
    headingText.innerHTML="2D->3D Lithophane Generator™";
}
function validform()
{
    var username = document.forms["login"]["username"];
    var password = document.forms["login"]["password"];

    if (username.value == "")
    {
        window.alert("Please enter your name.");
        name.focus();
        return false;
    }

    if (password.value == "")
    {
        window.alert("Please enter your password.");
        name.focus();
        return false;
    }

  return true;
}
  function logout() {
  var req = new XMLHttpRequest();
  req.open("POST", "home.html", true);
  req.withCredentials = true;
  req.send();

  document.getElementById('log_form').style.display = '';
  document.getElementById('logged_user').style.display = 'none';
  document.getElementById('logout_button').style.display = 'none';
  document.getElementById('content').style.display = 'none';
  hide_error();
}
    function myFunction() {
        var pass1 = document.getElementById("pass1").value;
        var pass2 = document.getElementById("pass2").value;
        if (pass1 != pass2) {
            //alert("Passwords Do not match");
            document.getElementById("pass1").style.borderColor = "#E34234";
            document.getElementById("pass2").style.borderColor = "#E34234";
        }
        else {
            alert("Passwords Match!!!");
        }
    }
    document.getElementById("mybutton").onclick = function () {
        location.href = "https://mariamiah.github.io/Ride-My-Way/UI/dashboard.html";
    }
    function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
</script>
