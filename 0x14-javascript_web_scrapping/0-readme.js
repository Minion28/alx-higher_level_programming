#!/usr/bin/node
//script that reads and prints a file

const a = process.argv[2];
const b = require('fs');
b.readFile(a, 'utf8', (error, data) =>
{
    if (error)
    {
        console.log(error)
    }
    else
    {
        console.log(data);
    }
});