#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');
const util = require('util');

const rp = util.promisify(request);

async function getJSON (url) {
  const req = await rp(url);

  try {
    return JSON.parse(req.body);
  } catch (err) {
    throw new Error('Invalid JSON: Received:\n' + req.body);
  }
}

async function * getCharacters (filmURI) {
  try {
    const response = await getJSON(filmURI);
    const charsURIs = response.characters;

    for (const uri of charsURIs) {
      const char = await getJSON(uri);
      yield char.name;
    }
  } catch {
    throw new Error('Couldn\'t retrieve the characters!');
  }
}

async function printCharacters (filmURI) {
  try {
    for await (const name of getCharacters(filmURI)) {
      console.log(name);
    }
  } catch (err) {
    console.log(err);
    throw err;
  }
}

async function main () {
  const id = argv[2];
  const URI = `https://swapi-api.alx-tools.com/api/films/${id}/`;

  try {
    await printCharacters(URI);
  } catch {
    throw new Error('Fatal error: Aborting!');
  }
}

main().catch((err) => { throw err; });
