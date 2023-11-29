const { MongoClient, ServerApiVersion } = require("mongodb");

// Replace the placeholder with your Atlas connection string
const uri = "mongodb+srv://Semproject2024:Semproject2024@test-db.dm1ghqi.mongodb.net/";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri,  {
        serverApi: {
            version: ServerApiVersion.v1,
            strict: true,
            deprecationErrors: true,
        }
    }
);

client.connect();
async function run() {
  try {
    await client.connect();

    // Send a ping to confirm a successful connection

    const db = client.db("User");
    const col = db.collection("Details");
    const cursor = col.find();
    for await (const doc of cursor) {
      console.dir(doc);
    }
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
