
using System;
using System.IO;

class FileSystemManager {
    public void DisplayFileData(string filePath) {
        Console.WriteLine("Opening file: " + filePath);
        
        // BUG: The StreamReader is instantiated but never closed or disposed.
        // In a real application, this causes a resource leak and locks the file.
        StreamReader fileReader = new StreamReader(filePath);
        string fileContent = fileReader.ReadToEnd();
        
        Console.WriteLine("--- FILE START ---");
        Console.WriteLine(fileContent);
        Console.WriteLine("--- FILE END ---");
        // missing fileReader.Close() or using block
    }
}
