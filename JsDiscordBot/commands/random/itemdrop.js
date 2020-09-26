const { Message } = require('discord.js');
const commando = require('discord.js-commando');  // importing the discord bot package

var rariety;

class ItemDropRate extends commando.Command {
    constructor(client){
        super(client, {
            name: 'attack',
            group: 'random',
            memberName: 'attack',
            description: 'Chance that the attack does the full weapon damage',
        });

    }
    async run(messsage, args){
        var attack = Math.floor(Math.random() * 70) + 1;
        Message.reply("Your attack does " +attack +" damage to the monster." );
    }

}

module.exports = ItemDropRate;