import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log(reply);
        }
    });
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`Value for ${schoolName}:`, value);
    } catch (err) {
        console.error('Error:', err);
    }
}

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
