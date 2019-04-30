var dictionary = {
    "myKey": "myValue",
    "secondKey": [1,2,3]
}

for (const [key, value] of Object.entries(dictionary))
    console.log(key, value);