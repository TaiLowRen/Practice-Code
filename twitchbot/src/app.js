const tmi = require('tmi.js');

const options = {
	options: {
		debug: true,
	},
	connection: {
		cluster: 'aws',
		reconnect: true,
	},
	identity: {
		username: 'Fatalis',
		password: 'oauth:ypuak3s032r6g8pdfbo2y3v8ff2c2l',
	},
	channels: ['TaiLowRen']
};

const client =  new tmi.client(options);

client.connect();

client.on('connected', (address, port) => {
	client.action('TaiLowRen', "Fatalis has entered the Chat");
})