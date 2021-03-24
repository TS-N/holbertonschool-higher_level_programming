#!/usr/bin/node
const fs = require('fs');
fs.writeFileSync(process.argv[4], (fs.readFileSync(process.argv[2], { encoding: 'utf-8' }) + fs.readFileSync(process.argv[3], { encoding: 'utf-8' })));
