using System;
using System.IO;

class Loader {
    public void Read(string path) {
        // BUG
        StreamReader r = new StreamReader(path);
        string d = r.ReadToEnd();
        Console.WriteLine(d);
    }
}
// Line 11
// Line 12
