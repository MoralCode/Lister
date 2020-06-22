
form = document.getElementById("lister-subscribe")
submit = form.querySelectorAll('input[type="submit"]')
message = form.getElementsByClassName("message")[0]


function submitForm(e) {
	e.preventDefault()

	// https://stackoverflow.com/a/374677/3033386
	var xhr = new XMLHttpRequest()
	xhr.open(form.method, form.action);
	xhr.onload = function (event) {
		// debugger;

		console.log(event.target);
		responseJson = JSON.parse(event.target.response)


		// <br><span class="error"><strong>Error:</strong> {{ error }} </span><br>
		if (200 <= event.target.status && event.target.status <= 299) {
			message.classList.toggle("error", false)
			message.classList.toggle("success", true)
			message.innerHTML = "Check your email to confirm your subscription!<br>"
		} else {
			message.classList.toggle("error", true)
			message.classList.toggle("success", false)
			message.innerHTML = responseJson.message + "<br>"

		}

	};
	xhr.send(new FormData(form));
}


form.onsubmit = submitForm;