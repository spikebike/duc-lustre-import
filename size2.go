package main
  
import (
        "fmt"
        "os"
)

// ... (Rest of your Go code)

func saveDirectorySizes(directorySizes map[string]int, filename string) error {
        file, err := os.Create(filename)
        if err != nil {
                return err
        }
        defer file.Close()

        for directory, size := range directorySizes {
                _, err := fmt.Fprintln(file, directory, size) // Write directory and size on a line
                if err != nil {
                        return err
                }
        }

        return nil
}

// Example usage after processing data
err := saveDirectorySizes(directorySizes, "directory_sizes.txt")
if err != nil {
        fmt.Println("Error saving data:", err)
}

