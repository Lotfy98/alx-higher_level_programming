#!/usr/bin/node
//a script that reads and prints the content of a file
const fs = require('fs');

const readFile = (filePath) => {
	try {
		return fs.readFileSync(filePath, 'utf-8');
	} catch (err) {
		return err;
	}
}

const filePath = process.argv[2];

const content = readFile(filePath);

if (content instanceof Error) {
	console.log(content);
}
else {
	console.log(content);
}
