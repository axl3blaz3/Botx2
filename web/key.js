
function handle(e) {
	var go = document.getElementById("go");
	var key=e.keycode || e.which;
	if (key ==13 && go.value != ""){
	eel.name_entry(go.value)
	}
}

eel.expose(vPassInput);
function vPassInput(x) {
	alert(x);
}

