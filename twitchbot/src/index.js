
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
		username: 'FatalisBot',
		password: 'oauth:r1vinrmmrpts5ymwbm7uq2ti68z2dz',
	},
	channels: ['TaiLowRen', 'Ramez05']
};

const client =  new tmi.client(options);

client.connect();

client.on('connected', (address, port) => {
	client.action('Ramez05', "Pay your dues mortals");
});

client.on('chat', (channel, user, message, self) => {
    if (message == 'KEKW'){
        client.action('Ramez05', 'Hunters who laugh die very fast...');
    } else  if (message == 'death'){
        client.action('Ramez05', `So you long for death ${user['display-name']}` )
    }
});

