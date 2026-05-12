using System;
using System.IO;

class DataProcessor {
    public void ProcessFile(string fileName) {
        // BUG: StreamReader is not closed
        StreamReader reader = new StreamReader(fileName);
        string content = reader.ReadToEnd();
        Console.WriteLine(content);
    }
}
