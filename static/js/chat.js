var socket = io();

var handler = {
	sendMessage: function(message) {
		if (message != "")
			socket.emit('new-message',{ message: message });
	},
	newMessage: function(data) {
		$('ul#history').append('<li><div class="username">' + data['username'] + '</div><div class="message">' + data['message'] + '</div></li>');
	},
	newUser: function(data) {
		$('ul#history').append('<li><div class="alert">' + data['username'] + ' has joined the chat.</div></li>');
		$('ul#online').append('<li class="user" id="' + data['username'] + '">' + data['username'] + '</li>');
	},
	removeUser: function(data) {
		$('ul#history').append('<li><div class="alert">' + data['username'] + ' has left the chat.</div></li>');
		$('li#' + data['username']).remove();
	}
}

socket.on('new-message', (data) => handler.newMessage(data));
socket.on('new-user', (data) => handler.newUser(data));
socket.on('remove-user', (data) => handler.removeUser(data));


$('#message').on('keydown', function(ev) {
	if (ev.key == 'Enter') {
		var message = $('#message').val();
		handler.sendMessage(message)
		$('#message').val("");
	}
});