using System;
using System.IO;

class Loader {
    public void Read(string path) {
        // BUG: Resource leak
        StreamReader r = new StreamReader(path);
        string d = r.ReadToEnd();
        Console.WriteLine(d);
    }
}
// Line 12
// Line 13
// Line 14
