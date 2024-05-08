import { createClient, print} from "redis";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

// Create Hash
client.hset("HolbertonSchools", "Portland", 50, print);
client.hset("HolbertonSchools", "Seattle", 80, print);
client.hset("HolbertonSchools", "New York", 20, print);
client.hset("HolbertonSchools", "Bogota", 20, print);
client.hset("HolbertonSchools", "Cali", 40, print);
client.hset("HolbertonSchools", "Paris", 2, print);

// Display Hash
client.hgetall("HolbertonSchools", function(err, obj) {
    if (err) {
        console.error('Error:', err);
    } else {
        console.log('Hash contents:', obj);
    }
});
