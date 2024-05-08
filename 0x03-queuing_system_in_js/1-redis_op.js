import { createClient } from "redis";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log(reply);
        }
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, function(err, value) {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log(`Value for ${schoolName}:`, value);
        }
    });
}

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
