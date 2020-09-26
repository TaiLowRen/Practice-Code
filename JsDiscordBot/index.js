const commando = require('discord.js-commando');  // importing the discord bot package
const bot = new commando.CommandoClient(); // creating the bot
bot.login("") // getting the bot to login


bot.registry.registerGroup('random', 'Random'); // creating a group for randomized commands
/**
 * Place anything random in the group above,
 * such as the drop table, spawn rate,
 * gather rates, size of monster, etc...
 */
bot.registry.registerDefaultCommands();
bot.registry.registerCommandsIn(__dirname + "/commands");
