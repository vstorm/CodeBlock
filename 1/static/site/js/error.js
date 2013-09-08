var i = 3;
var intervalid;
intervalid = setInterval("countdown()", 1000);
function countdown() {
	if (i == 0) {
		window.location.href = "/";
		clearInterval(intervalid);
	}
	document.getElementById("second").innerHTML = i;
	i--;
}
function goBack()
{
	window.history.back();
}