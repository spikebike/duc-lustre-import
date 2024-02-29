package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
    "strings"
)

type Record struct {
    Path string `json:"path"`
    Size int    `json:"size"`
}

func main() {
    directorySizes := make(map[string]int)

    // Replace with your list of JSON files
    jsonFiles := []string{"file1.json", "file2.json", ...}

    for _, filename := range jsonFiles {
        file, err := os.Open(filename)
        if err != nil {
            fmt.Println("Error opening file:", err)
            continue
        }
        defer file.Close()

        decoder := json.NewDecoder(file)
        for decoder.More() {
            var record Record
            err := decoder.Decode(&record)
            if err != nil {
                fmt.Println("Error decoding JSON:", err)
                continue
            }

            components := strings.Split(record.Path, "/")
            for i := 1; i <= len(components); i++ {
                prefix := strings.Join(components[:i], "/")
                directorySizes[prefix] += record.Size
            }
        }
    }

    // Example query
    fmt.Println(directorySizes["/rsandhu/csg_data"])

    // ... Code to save 'directorySizes' (consider serialization options)
}


