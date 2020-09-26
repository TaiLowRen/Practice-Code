const GoogleSpreadsheet = require('google-spreadsheet');
const { endianness } = require('os');
const { promisify } = require('util');

const creds = require('./client_secret.json');

function printItem(item){
    console.log('Name: ' + item.name);
    console.log('Rarity: ' + item.rarity);
    console.log('Capacity: ' + item.capacity);
    console.log('Value: ' + item.value);
    console.log('Description: ' + item.description);
    console.log('------------------------------------------------------------------------');
}

async function accessSpreadsheet(){
    const doc = new GoogleSpreadsheet('1OjR0DFGKtX4cfYlS5TYTP2YJ4BCz_cdpIWVdb9Whh4A');
    await promisify(doc.useServiceAccountAuth)(creds);
    const info = await promisify(doc.getInfo)();
    const sheet  = info.worksheets[0];

    const rows = await promisify(sheet.getRows)({
        
    });

    rows.forEach(row => {
        printItem(row);
        
    });

}

accessSpreadsheet();